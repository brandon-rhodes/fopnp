#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/app_improved.py
# A payments application with basic security improvements added.

import bank, uuid
from flask import (Flask, abort, flash, get_flashed_messages,
                   redirect, render_template, request, session, url_for)

app = Flask(__name__)
app.secret_key = 'saiGeij8AiS2ahleahMo5dahveixuV3J'

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if request.method == 'POST':
        if (username, password) in [('brandon', 'atigdng'), ('sam', 'xyzzy')]:
            session['username'] = username
            session['csrf_token'] = uuid.uuid4().hex
            return redirect(url_for('index'))
    return render_template('login.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    payments = bank.get_payments_of(bank.open_database(), username)
    return render_template('index.html', payments=payments, username=username,
                           flash_messages=get_flashed_messages())

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))
    account = request.form.get('account', '').strip()
    dollars = request.form.get('dollars', '').strip()
    memo = request.form.get('memo', '').strip()
    complaint = None
    if request.method == 'POST':
        if request.form.get('csrf_token') != session['csrf_token']:
            abort(403)
        if account and dollars and dollars.isdigit() and memo:
            db = bank.open_database()
            bank.add_payment(db, username, account, dollars, memo)
            db.commit()
            flash('Payment successful')
            return redirect(url_for('index'))
        complaint = ('Dollars must be an integer' if not dollars.isdigit()
                     else 'Please fill in all three fields')
    return render_template('pay2.html', complaint=complaint, account=account,
                           dollars=dollars, memo=memo,
                           csrf_token=session['csrf_token'])

if __name__ == '__main__':
    app.debug = True
    app.run()
