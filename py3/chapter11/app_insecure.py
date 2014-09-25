
from flask import Flask, make_response, redirect, request, url_for
from jinja2 import Template

import bank
from templates import design_html, login_html, index_html, pay_html

app = Flask(__name__)
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
    message = request.args.get('message')
    body = Template(index_html).render(items=''.join(lines), message=message)
    title = 'Welcome, ' + username
    return Template(design_html).render(title=title, body=body)

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
            return redirect(url_for('index', message='Payment successful'))
    return Template(design_html).render(title='Welcome, ' + username,
                                        body=pay_html)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if request.method == 'GET':
        title = 'Welcome'
    elif request.method == 'POST':
        if username == 'brandon' and password == 'atigdng':
            response = redirect(url_for('index'))
            response.set_cookie('username', username)
            return response
        title = 'Please try again'
    form = Template(login_html).render(username=username)
    return Template(design_html).render(title=title, body=form)

@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.set_cookie('username', '')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
