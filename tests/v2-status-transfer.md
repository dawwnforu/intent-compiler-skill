# R55: unseen wording against the existing meeting processor

Protocol frozen before executing the R22 second-turn processor on these statements. No new model generation or Skill change. R22 fixed its exposed regression set; this check asks whether those fixes transfer to different wording, without editing the processor or sending the new answers back for repair.

All inputs retain the existing `决定：` format. Expected labels are either confirmed decision or unresolved; original text must remain available. These eight hand-authored cases are a small diagnostic set, not a general accuracy benchmark.

| File | Exact statement | Expected |
|---|---|---|
| defer.txt | 决定：增加预算这件事先搁一搁，等下周再议。 | unresolved |
| unchanged.txt | 决定：原定周五的演示照常进行。 | decision |
| refused.txt | 决定：经理已明确表示不同意延期。 | decision |
| personal.txt | 决定：关于加人，目前只是小李的个人想法。 | unresolved |
| price.txt | 决定：会议未采纳涨价建议，售价保持不变。 | decision |
| not-approved.txt | 决定：听起来可以，不代表已经获批。 | unresolved |
| finance.txt | 决定：负责人还需要征求财务意见，预算暂不能敲定。 | unresolved |
| label.txt | 决定：会议一致同意把按钮上的“尚未通过”改成“待审核”。 | decision |

The defer statement records a postponement of the budget decision; its coarse unresolved label concerns approval of the budget increase. A system explicitly extracting the agreed deferral separately would require a richer review than this single-label test. Preserve that annotation limitation rather than claiming every disagreement is an unambiguous error.

Run a fresh isolated copy of the existing `organize.ps1` through its normal PowerShell `-File` entry. Preserve command output, generated notes, source text and labels. Do not add sentence-specific patterns after seeing results. If failures recur, diagnose the method's capability boundary before proposing a new rule. This is not a current full-Skill versus raw-request comparison.
