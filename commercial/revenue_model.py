"""Conditional expected-value model in USD; no sales forecast or payment integration."""
import csv
import json
import math
from pathlib import Path

ROOT=Path(__file__).parent

def calculate(p,s):
    rates=['trial_rate','activation_rate','paid_given_active','refund_rate']
    assert all(0<=s[k]<=1 for k in rates) and 0<=p['platform_share']<1
    assert all(v>=0 for k,v in p.items()) and s['views']>=0 and s['days']>0
    active=s['views']*s['trial_rate']*s['activation_rate']
    orders=active*s['paid_given_active'];refunds=orders*s['refund_rate']
    gross=orders*p['price'];retained=gross*(1-s['refund_rate'])
    creator=retained*(1-p['platform_share'])
    tools=orders*p['creator_tool_per_order']+active*p['creator_tool_per_active']
    support=active*p['minutes_per_active']/60+orders*p['minutes_per_order']/60+refunds*p['minutes_per_refund']/60
    months=s['days']/30
    fixed_cash=p['monthly_cash']*months
    fixed_hours=p['initial_hours']+(p['maintenance_hours_month']+p['recruitment_hours_month'])*months
    economic=creator-tools-fixed_cash-(support+fixed_hours)*p['hourly_value']
    c=s['paid_given_active']
    unit=(p['price']*(1-s['refund_rate'])*(1-p['platform_share'])-p['creator_tool_per_order']
          -(p['minutes_per_order']+s['refund_rate']*p['minutes_per_refund'])/60*p['hourly_value']
          -(p['creator_tool_per_active']+p['minutes_per_active']/60*p['hourly_value'])/c) if c else None
    break_even=math.ceil((fixed_cash+fixed_hours*p['hourly_value'])/unit) if unit and unit>0 else None
    funnel=s['trial_rate']*s['activation_rate']*c
    return {'days':s['days'],'views':s['views'],'activated_expected':active,'orders_expected':orders,'refunds_expected':refunds,
      'gross_usd':gross,'platform_usd':retained*p['platform_share'],'creator_revenue_usd':creator,'creator_tools_usd':tools,
      'fixed_cash_usd':fixed_cash,'support_hours':support,'fixed_hours':fixed_hours,
      'support_time_value_usd':support*p['hourly_value'],'fixed_time_value_usd':fixed_hours*p['hourly_value'],
      'cash_contribution_before_payout_usd':creator-tools-fixed_cash,'economic_result_usd':economic,
      'unit_contribution_after_trial_support_usd':unit,'break_even_orders':break_even,
      'break_even_views':math.ceil(break_even/funnel) if break_even is not None and funnel else None}

def support_thresholds(p,s):
    """Variable contribution only: equality is zero, not full business break-even."""
    calculate(p,s)
    c=s['paid_given_active'];w=p['hourly_value']/60;r=s['refund_rate']
    after_order=p['price']*(1-r)*(1-p['platform_share'])-p['creator_tool_per_order']-(p['minutes_per_order']+r*p['minutes_per_refund'])*w
    active_cost=p['creator_tool_per_active']+p['minutes_per_active']*w
    return {'activation_support_zero_contribution_minutes':(c*after_order-p['creator_tool_per_active'])/w if w and c else None,
      'post_order_support_zero_contribution_minutes':(p['price']*(1-r)*(1-p['platform_share'])-p['creator_tool_per_order']-active_cost/c)/w-r*p['minutes_per_refund'] if w and c else None,
      'conversion_zero_contribution':active_cost/after_order if after_order>0 else None,
      'positive_possible_with_conversion_at_most_one':bool(after_order>0 and active_cost/after_order<1),
      'note':'Positive only below time ceilings / above conversion threshold; negative ceilings or conversion >=1 mean infeasible under these assumptions. Fixed research, upkeep and cash still need coverage.'}

def main():
    config=json.loads((ROOT/'revenue-inputs.json').read_text(encoding='utf-8'))
    p={k:v['value'] for k,v in config['parameters'].items()}
    rows=[{'scenario':name,**calculate(p,s['values'])} for name,s in config['scenarios'].items()]
    sensitivity=[];base=config['scenarios']['base_30']['values']
    for price in [19,39,79]:
        for conversion in [.05,.15,.30]:
            sensitivity.append({'price':price,'paid_given_active':conversion,**calculate({**p,'price':price},{**base,'paid_given_active':conversion})})
    support_sensitivity=[]
    for conversion in [.05,.15,.30]:
        for refund in [0,.10,.30]:
            for post_order in [5,20]:
                trial_p={**p,'price':19,'minutes_per_order':post_order}
                trial_s={**base,'paid_given_active':conversion,'refund_rate':refund}
                support_sensitivity.append({'price':19,'paid_given_active':conversion,'refund_rate':refund,
                  'post_order_minutes':post_order,**support_thresholds(trial_p,trial_s)})
    zero=calculate(p,{**base,'paid_given_active':0})
    assert zero['orders_expected']==0 and zero['creator_revenue_usd']==0 and zero['economic_result_usd']<0 and zero['break_even_orders'] is None
    for row in rows:
        scenario=config['scenarios'][row['scenario']]['values']
        assert math.isclose(row['creator_revenue_usd']+row['platform_usd'],row['gross_usd']*(1-scenario['refund_rate']))
    full_refund=calculate(p,{**base,'refund_rate':1})
    assert full_refund['creator_revenue_usd']==0 and full_refund['platform_usd']==0
    assert calculate({**p,'price':0},base)['break_even_orders'] is None
    # Test a known boundary independently of the hypotheses users will replace with observations.
    check_p={**p,'price':19,'platform_share':.3,'hourly_value':20,'creator_tool_per_order':.2,
      'creator_tool_per_active':.05,'minutes_per_order':20,'minutes_per_refund':15}
    check_s={**base,'paid_given_active':.15,'refund_rate':.1}
    ceiling=support_thresholds(check_p,check_s)['activation_support_zero_contribution_minutes']
    assert math.isclose(ceiling,1.9215) and math.isclose(calculate({**check_p,'minutes_per_active':ceiling},check_s)['unit_contribution_after_trial_support_usd'],0,abs_tol=1e-9)
    assert calculate({**check_p,'minutes_per_active':ceiling+.01},check_s)['unit_contribution_after_trial_support_usd']<0
    assert calculate({**check_p,'minutes_per_active':ceiling-.01},check_s)['unit_contribution_after_trial_support_usd']>0
    assert support_thresholds({**check_p,'minutes_per_order':60},check_s)['activation_support_zero_contribution_minutes']<0
    assert support_thresholds(p,{**base,'paid_given_active':0})['activation_support_zero_contribution_minutes'] is None
    assert support_thresholds({**p,'hourly_value':0},base)['activation_support_zero_contribution_minutes'] is None
    assert not support_thresholds(p,{**base,'refund_rate':1})['positive_possible_with_conversion_at_most_one']
    try:calculate(p,{**base,'refund_rate':1.1})
    except AssertionError:pass
    else:raise AssertionError('Invalid rate must fail')
    for name,data in [('revenue-scenarios.csv',rows),('revenue-sensitivity.csv',sensitivity),('revenue-support-thresholds.csv',support_sensitivity)]:
        with (ROOT/name).open('w',newline='',encoding='utf-8-sig') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
    (ROOT/'revenue-results.json').write_text(json.dumps({'scenarios':rows,'sensitivity':sensitivity,'support_thresholds_19_usd':support_sensitivity,
      'actual_payout_usd':None,'payout_status':'Not queried or verified; these are estimates before settlement, not an account balance.',
      'checks':'zero sales, full refund, no positive contribution, conservation, invalid-rate and support-threshold boundary checks pass',
      'limits':'Fractional orders are conditional expectations, not observed buyers; payout timing, taxes and unavailable fees are not forecast.'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    for row in rows:print(row['scenario'],round(row['orders_expected'],2),round(row['economic_result_usd'],2),row['break_even_orders'])

if __name__=='__main__':main()
