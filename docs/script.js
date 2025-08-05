
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

function runSimulator() {
  const type = document.getElementById("itemType").value;
  const reason = document.getElementById("refundReason").value;
  const days = parseInt(document.getElementById("daysElapsed").value);
  let risk = "Medium";
  let strategy = "Use polite tone with clear reasoning.";

  if (type === "Electronics" && days <= 10) {
    risk = "Low";
    strategy = "Say item is defective. Mention you're within return window.";
  } else if (reason === "Missing item" && days <= 3) {
    risk = "Low";
    strategy = "State package arrived with missing contents. Ask for replacement.";
  } else if (days > 25) {
    risk = "High";
    strategy = "Use guilt-based language or reference prime membership.";
  }

  document.getElementById("simResult").innerHTML = `
    <strong>Risk Level:</strong> ${risk}<br/>
    <strong>Recommended Strategy:</strong> ${strategy}
  `;
}
