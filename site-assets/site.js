document.querySelectorAll('pre > code').forEach(code => {
  const pre = code.parentElement;
  const wrap = document.createElement('div'); wrap.className = 'code-wrap';
  const bar = document.createElement('div'); bar.className = 'code-bar';
  const label = document.createElement('span'); label.textContent = code.className.replace('language-', '') || 'code';
  const button = document.createElement('button'); button.className = 'copy'; button.type = 'button'; button.textContent = 'Copy code';
  button.addEventListener('click', async () => {
    const status = document.getElementById('copy-status');
    try {
      if (!navigator.clipboard) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(code.textContent);
      button.textContent = 'Copied!'; status.textContent = 'Code copied. Paste it into your editor or terminal.';
    } catch (_) {
      const selection = window.getSelection(); const range = document.createRange(); range.selectNodeContents(code); selection.removeAllRanges(); selection.addRange(range);
      status.textContent = 'Code selected. Press Ctrl+C (or Command+C) to copy.';
    }
    setTimeout(() => {button.textContent = 'Copy code'; status.textContent = '';}, 3500);
  });
  pre.before(wrap); wrap.append(bar, pre); bar.append(label, button);
});
document.querySelectorAll('table').forEach(table => {const wrap = document.createElement('div'); wrap.className = 'table-wrap'; table.before(wrap); wrap.append(table);});
