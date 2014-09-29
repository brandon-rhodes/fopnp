#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/djbank/admin.py
# Admin site setup for our Django application.

from django.contrib import admin
from .models import Payment

admin.site.register(Payment)
