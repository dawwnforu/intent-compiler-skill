'use strict';
(() => {
  const data = window.pilotDemoData;
  let language = 'zh';
  let view = 'final';
  const starter = {
    zh: '请从我已连接的 Agensi 加载 Intent Compiler — Everyday Ideas to Usable Work，读取其 SOURCE.json 并报告实际来源。找不到或来源不同就先告诉我，不另装同名 Skill、不替换正式安装。然后使用它处理我接下来用自己的话提出的任务；先核对实际工具和授权。',
    en: 'Load Intent Compiler — Everyday Ideas to Usable Work from my connected Agensi account. Read SOURCE.json and report the actual source. If missing or different, tell me; do not install another copy or replace my formal installation. Then use it for the task I describe next in my own words, checking available tools and authorization.'
  };
  const labels = {
    zh: {initial: 'R99 / C 组 · 实际初次交接原文', final: 'R99 / C 组 · 实际修改后说明原文', copied: '已尝试复制，文字也已选中。请粘贴核对；未复制时可手动复制，不必更改权限。', manual: '未能自动复制。已选中下方文字，请手动复制；不需要修改浏览器权限。'},
    en: {initial: 'R99 / arm C · actual initial handoff', final: 'R99 / arm C · actual revised brief', copied: 'Copy requested; the text is also selected. Paste to check, or copy it manually. No permission change is needed.', manual: 'Automatic copy was unavailable. The text is selected; copy it manually. No permission change is needed.'}
  };
  const readingAid = {
    zh: {initial: '原件阅读提示：此时名为“跳跳”，围巾浅绿。目的仍是帮助新同学报名；独立链接、静态替代与不自动旋转等决定已保留。以下为实际原文。', final: '原件阅读提示：名称改为“芽芽”，围巾改成暖黄；报名目的与其他有效选择保留。格式、资产和真实报名地址仍待定。以下为实际原文。'},
    en: {initial: 'Reading aid by the developer, not a separate English model output: the character is Tiaotiao with a pale-green scarf. Help newcomers register; keep an independent registration link, a static fallback and no automatic rotation. The original Chinese handoff follows.', final: 'Reading aid by the developer, not a separate English model output: rename the character Yaya and change the scarf to warm yellow. Preserve registration, the fallback, reduced-motion behavior and other confirmed choices. Format, assets and the real registration URL remain unresolved. The original Chinese brief follows.'}
  };
  function showArtifact() {
    document.querySelector('#artifact').textContent = data[view];
    document.querySelector('#artifact-label').textContent = labels[language][view];
    document.querySelector('#artifact-summary').textContent = readingAid[language][view];
    document.querySelector('#download').href = view === 'initial' ? 'initial-handoff.md' : 'final-brief.md';
    document.querySelectorAll('[data-view]').forEach(button => button.setAttribute('aria-pressed', String(button.dataset.view === view)));
  }
  function translate() {
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-zh][data-en]').forEach(node => { node.textContent = node.dataset[language].replace(/\\n/g, '\n'); });
    const toggle = document.querySelector('#language');
    toggle.textContent = language === 'zh' ? 'English' : '中文';
    toggle.setAttribute('aria-label', language === 'zh' ? 'Switch to English' : '切换到中文');
    document.querySelector('#starter').value = starter[language];
    document.querySelector('#copy-status').textContent = '';
    showArtifact();
  }
  document.querySelector('#request').textContent = data.requestExcerpt;
  document.querySelector('#change').textContent = data.changeExcerpt;
  document.querySelectorAll('[data-view]').forEach(button => button.addEventListener('click', () => { view = button.dataset.view; showArtifact(); }));
  document.querySelector('#language').addEventListener('click', () => { language = language === 'zh' ? 'en' : 'zh'; translate(); });
  document.querySelector('#copy').addEventListener('click', async () => {
    try {
      if (!navigator.clipboard?.writeText) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(document.querySelector('#starter').value);
      document.querySelector('#starter').focus();
      document.querySelector('#starter').select();
      document.querySelector('#copy-status').textContent = labels[language].copied;
    } catch {
      document.querySelector('#starter').focus();
      document.querySelector('#starter').select();
      document.querySelector('#copy-status').textContent = labels[language].manual;
    }
  });
  translate();
})();
