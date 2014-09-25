
from flask import Flask, make_response, redirect, request, url_for
app = Flask(__name__)

design = ('<html><head><title>{title}</title>'
          '<link rel="stylesheet" type="text/css" href="/static/style.css">'
          '</head><body><h1>{title}</h1>{body}</body>')
loginform = ('<form method="post"><label>User: <input name="username"></label>'
             '<label>Password: <input name="password" type="password"></label>'
             '<button type="submit">Log in</button></form>')
mainpage = ('<p>Your transactions:</p><ul>{items}</ul>'
            '<form method="post" action="/logout">'
            '<button type="submit">Logout</form>')

@app.route('/')
def index():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    return design.format(title='Welcome, ' + username, body=mainpage)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        title = 'Welcome'
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print('X', username, password)
        if username == 'brandon' and password == 'atigdng':
            response = redirect(url_for('index'))
            response.set_cookie('username', username)
            return response
        title = 'Please try again'
    return design.format(title=title, body=loginform)

@app.route('/logout', methods=['POST'])
def logout():
    response = redirect(url_for('login'))
    response.set_cookie('username', 'LOGGED-OUT')
    return response

if __name__ == '__main__':
    app.debug = True
    app.run()
