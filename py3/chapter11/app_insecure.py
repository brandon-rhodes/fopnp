
from flask import Flask, redirect, render_template, request, url_for
import bank

app = Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    payments = bank.get_payments_of(bank.open_database(), username)
    message = request.args.get('message')
    return render_template('index.html', payments=payments, message=message,
                           username=username)

@app.route('/pay', methods=['GET', 'POST'])
def pay():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    account = request.form.get('account', '').strip()
    dollars = request.form.get('dollars', '').strip()
    message = request.form.get('message', '').strip()
    if request.method == 'POST':
        if account and dollars and dollars.isdigit() and message:
            db = bank.open_database()
            bank.add_payment(db, username, account, dollars, message)
            db.commit()
            return redirect(url_for('index', message='Payment successful'))
        complaint = ('Dollars must be an integer' if not dollars.isdigit()
                     else 'Please fill in all three fields')
    else:
        complaint = None
    return render_template('pay.html', complaint=complaint, account=account,
                           dollars=dollars, message=message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if request.method == 'POST':
        if username == 'brandon' and password == 'atigdng':
            response = redirect(url_for('index'))
            response.set_cookie('username', username)
            return response
    return render_template('login.html', username=username)

@app.route('/logout')
def logout():
    response = redirect(url_for('login'))
    response.set_cookie('username', '')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
