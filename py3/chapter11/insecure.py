
import bank
from flask import Flask, redirect, request, url_for
app = Flask(__name__)

design = ('<html><head><title>{title}</title>'
          '<link rel="stylesheet" type="text/css" href="/static/style.css">'
          '</head><body><h1>{title}</h1>{body}</body>')
loginform = ('<form method="post"><label>User: <input name="username"></label>'
             '<label>Password: <input name="password" type="password"></label>'
             '<button type="submit">Log in</button></form>')
mainpage = ('<p>Your transactions:</p><ul>{items}</ul>'
            '<form method="post" action="/pay">'
            '<label>To account: <input name="account"></label>'
            '<label>Amount: <input name="amount"></label>'
            '<button type="submit">Send money</button>'
            '</form>'
            '<form method="post" action="/logout">'
            '<button type="submit">Logout</button></form>')
payment = '<li>${p.dollars} to account {p.credit}<br>{p.message}'

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    payments = bank.get_payments_of(bank.open_database(), '101')
    body = mainpage.format(items=''.join(payment.format(p=p) for p in payments))
    return design.format(title='Welcome, ' + username, body=body)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        title = 'Welcome'
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'brandon' and password == 'atigdng':
            response = redirect(url_for('index'))
            response.set_cookie('username', username)
            return response
        title = 'Please try again'
    return design.format(title=title, body=loginform)

@app.route('/logout', methods=['POST'])
def logout():
    response = redirect(url_for('login'))
    response.set_cookie('username', '')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
