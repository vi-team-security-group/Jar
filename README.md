<!DOCTYPE html>
<html lang="bg">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ЖАР – Официална Документация</title>
  <style>
    body {
      font-family: sans-serif;
      line-height: 1.6;
      background: #f8f9fa;
      color: #222;
      max-width: 900px;
      margin: auto;
      padding: 2rem;
    }
    h1, h2, h3 {
      color: #d84315;
    }
    code {
      background: #eee;
      padding: 0.2em 0.4em;
      border-radius: 4px;
      font-size: 0.95em;
    }
    .section {
      margin-bottom: 2rem;
    }
    nav {
      background: #fff;
      border-bottom: 2px solid #d84315;
      padding: 1rem 0;
    }
    nav a {
      margin-right: 1.5rem;
      text-decoration: none;
      color: #d84315;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <nav>
    <a href="#intro">Начало</a>
    <a href="#syntax">Синтаксис</a>
    <a href="#examples">Примери</a>
    <a href="#interop">Интеграции</a>
    <a href="#contact">Контакти</a>
  </nav>

  <h1 id="intro">ЖАР – Българският език за програмиране</h1>
  <div class="section">
    <p><strong>ЖАР</strong> е съвременен програмен език със синтаксис на български език. Лесен за обучение, силно типизиран и подходящ за реални уеб и IoT приложения.</p>
  </div>

  <h2 id="syntax">Основен синтаксис</h2>
  <div class="section">
    <p>Пример на ЖАР код:</p>
    <pre><code>начало
    дай "Здравей, свят!"
край</code></pre>
    <p>Ключови думи: <code>начало</code>, <code>дай</code>, <code>ако</code>, <code>иначе</code>, <code>край</code></p>
  </div>

  <h2 id="examples">Примери</h2>
  <div class="section">
    <p>Функция за събиране на две числа:</p>
    <pre><code>функция събери(а, б)
    върни а + б
край</code></pre>
  </div>

  <h2 id="interop">Интеграция с други езици</h2>
  <div class="section">
    <ul>
      <li>✅ Python – чрез import на jar.run()</li>
      <li>🧪 HTML/PHP – чрез &lt;jar&gt; таг</li>
      <li>🔜 JavaScript – планиран transpiler</li>
      <li>🔜 C/C++ – за вградени системи</li>
    </ul>
  </div>

  <h2 id="contact">Контакти и принос</h2>
  <div class="section">
    <p>GitHub: <a href="https://github.com/yourusername/jar-lang">github.com/yourusername/jar-lang</a></p>
    <p>Имейл: <code>jar@yourdomain.com</code></p>
  </div>

</body>
</html>
