
design_html = """\
<html>
  <head>
    <title>{{ title }}</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
  </head>
  <body>
    <h1>{{ title }}</h1>
    {{ body }}
  </body>
</html>
"""

login_html = """\
<form method="post">
  <label>User: <input name="username" value="{{ username }}"></label>
  <label>Password: <input name="password" type="password"></label>
  <button type="submit">Log in</button>
</form>
"""

index_html = """\
{% if message %}
  <div class="message">{{ message }}<a href="/">&times;</a></div>
{% endif %}
<p>Your transactions</p>
<ul>{{ items }}</ul>
<a href="/pay">Make payment</a> | <a href="/logout">Log out</a>
"""

pay_html = """\
<form method="post" action="/pay">
  <label>To account: <input name="account"></label>
  <label>Dollars: <input name="dollars"></label>
  <label>Message: <input name="message"></label>
  <button type="submit">Send money</button> | <a href="/">Cancel</a>
</form>
"""
