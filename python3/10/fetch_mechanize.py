#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 10 - fetch_mechanize.py
# Submitting a form and retrieving a page with mechanize

import mechanize
br = mechanize.Browser()
br.open('http://www.weather.gov/')
br.select_form(predicate=lambda(form): 'zipcity' in form.action)
br['inputstring'] = 'Phoenix, AZ'
response = br.submit()
content = response.read()
open('phoenix.html', 'w').write(content)
