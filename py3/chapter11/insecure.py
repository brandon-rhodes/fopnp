
import bank
from flask import Flask, redirect, request, url_for
app = Flask(__name__)

design = ('<html><head><title>{title}</title>'
          '<link rel="stylesheet" type="text/css" href="/static/style.css">'
          '</head><body><h1>{title}</h1>{body}</body>')
loginform = ('<form method="post"><label>User: <input name="username"></label>'
             '<label>Password: <input name="password" type="password"></label>'
             '<button type="submit">Log in</button></form>')
mainpage = ('<p>Your transactions</p><ul>{items}</ul>'
            '<a href="/pay">Make payment</a> | <a href="/logout">Log out</a>')
paypage = ('<form method="post" action="/pay">'
           '<label>To account: <input name="account"></label>'
           '<label>Dollars: <input name="dollars"></label>'
           '<label>Message: <input name="message"></label>'
           '<button type="submit">Send money</button>'
           ' | <a href="/">Cancel</a></form>')
payment = '<li>${p.dollars} to account {p.credit}<br>{p.message}'

def format_payment(username, payment):
    prep = 'from' if (username == payment.credit) else 'to'
    other = payment.debit if (username == payment.credit) else payment.credit
    return ('<li class="{prep}">${p.dollars} {prep} <b>{other}</b> for:'
            ' <i>{p.message}</i>'.format(prep=prep, other=other, p=payment))

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    payments = bank.get_payments_of(bank.open_database(), username)
    lines = [format_payment(username, payment) for payment in payments]
    body = mainpage.format(items=''.join(lines))
    return design.format(title='Welcome, ' + username, body=body)

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    if request.method == 'POST':
        account = request.form.get('account')
        dollars = request.form.get('dollars')
        message = request.form.get('message')
        if account and dollars and dollars.isdigit() and message:
            db = bank.open_database()
            bank.add_payment(db, username, account, dollars, message)
            db.commit()
            return redirect(url_for('index'))
    body = paypage.format()
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

@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.set_cookie('username', '')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
