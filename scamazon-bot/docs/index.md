<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Scamazon Bot™ Documentation</title>
  <link rel="stylesheet" href="styles.css"> <!-- Optional: link to your CSS -->
</head>
<body>
  <header>
    <h1>🧠 Scamazon Bot™ Documentation</h1>
    <p><strong>Welcome to the official documentation for <em>Scamazon Bot™</em></strong>, the most advanced refund engineering system on the internet. This project is built for strategists who understand timing, tone, and policy — not fraud.</p>
  </header>

  <section>
    <h2>🎖️ Tier System Overview</h2>
    <table>
      <thead>
        <tr>
          <th>Tier</th>
          <th>Module</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>🟢 Tier 1</td><td>Basic Refund Bot</td><td>CLI refund triggers and excuses</td></tr>
        <tr><td>🔵 Tier 2</td><td>Strategic Flow Engine</td><td>Return timing logic and category profiles</td></tr>
        <tr><td>🟣 Tier 3</td><td>CLI Planner</td><td>Refund calendar, tone selector, and trigger mapping</td></tr>
        <tr><td>🔴 Tier 4</td><td>AI Dashboard</td><td>ChatGPT excuse generator, refund probability meter, encrypted Vault logs, and Amazon scraper</td></tr>
      </tbody>
    </table>
  </section>

  <section>
    <h2>🚀 Getting Started</h2>
    <ol>
      <li>Clone the repo:
        <pre><code>git clone https://github.com/refundghost/scamazon-bot.git
cd scamazon-bot</code></pre>
      </li>
      <li>Install dependencies:
        <pre><code>pip install flask openai cryptography beautifulsoup4 requests</code></pre>
      </li>
      <li>Generate encryption key:
        <pre><code>from vault_crypto import generate_key
generate_key()</code></pre>
      </li>
      <li>Run the Tier 4 dashboard:
        <pre><code>cd tier4_dashboard
python app.py</code></pre>
      </li>
    </ol>
    <p>Visit: <a href="http://localhost:5000">http://localhost:5000</a></p>
  </section>

  <section>
    <h2>🔐 Tier 4 Access</h2>
    <p>Tier 4 tools require login credentials stored in <code>users.json</code>. These tools include:</p>
    <ul>
      <li>Refund-by-design logic engine</li>
      <li>ChatGPT excuse rewriting</li>
      <li>Refund probability meter</li>
      <li>Encrypted Vault log system</li>
      <li>Admin panel for refund stats</li>
      <li>Amazon scraper for auto-fill</li>
    </ul>
  </section>

  <section>
    <h2>📦 Modules Included</h2>
    <ul>
      <li><code>forward_engineering.py</code>: Refund logic engine</li>
      <li><code>chatgpt_api.py</code>: ChatGPT excuse generator</li>
      <li><code>vault_log.py</code>: Encrypted refund log system</li>
      <li><code>vault_crypto.py</code>: Fernet encryption for logs</li>
      <li><code>amazon_scraper.py</code>: Auto-fill item metadata from Amazon</li>
      <li><code>app.py</code>: Flask web app with login, dashboard, and chatbot</li>
    </ul>
  </section>

  <section>
    <h2>🛡️ Philosophy</h2>
    <p><strong>We win because we know the rules.</strong></p>
    <p>Scamazon Bot doesn’t fake claims. It uses timing, tone, and platform logic to engineer refund outcomes that are already embedded in Amazon’s own structure.</p>
  </section>

  <section>
    <h2>🧠 Credits</h2>
    <p>Created by <strong>refundghost</strong>. Engineered for refund strategists, not scammers.</p>
  </section>

  <section>
    <h2>🛡️ Disclaimer</h2>
    <p>This tool is for educational and research purposes only. It does not promote or condone fraudulent activity. Use responsibly and within the bounds of applicable laws and platform policies.</p>
  </section>

  <section>
    <h2>✅ Final Steps</h2>
    <ol>
      <li>Save this as <code>docs/index.md</code></li>
      <li>Commit and push:
        <pre><code>git add docs/index.md
git commit -m "Add GitHub Pages landing page"
git push origin main</code></pre>
      </li>
      <li>Go to your repo’s <strong>Settings → Pages</strong></li>
      <li>Set source to <code>docs/</code> folder</li>
    </ol>
    <p>Your site will be live at: <a href="https://refundghost.github.io/scamazon-bot">https://refundghost.github.io/scamazon-bot</a></p>
  </section>
</body>
</html>
