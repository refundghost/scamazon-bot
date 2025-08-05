
document.querySelectorAll('pre code').forEach((block) => {
  const button = document.createElement('button');
  button.className = 'copy-button';
  button.textContent = '📋 Copy';
  block.parentNode.insertBefore(button, block);
  button.addEventListener('click', () => {
    navigator.clipboard.writeText(block.textContent);
    button.textContent = '✅ Copied!';
    setTimeout(() => button.textContent = '📋 Copy', 2000);
  });
});
