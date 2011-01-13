#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 11 - bottle_app.py
# A simple web application built using the Bottle micro-framework.

import base64, bottle
bottle.debug(True)
app = bottle.Bottle()

@app.route('/encode')
@bottle.view('bottle_template.html')
def encode():
    mystring = bottle.request.GET.get('mystring')
    if mystring is None:
        bottle.abort(400, 'This form requires a "mystring" parameter')
    return dict(mystring=mystring, myb=base64.b64encode(mystring))

@app.route('/')
@bottle.view('bottle_template.html')
def index():
    return dict(mystring=None)

bottle.run(app=app, host='localhost', port=8080)
