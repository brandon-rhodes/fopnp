#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/djbank/wsgi.py
# Standard, unchanged WSGI callable produced by Django.
# ----------------------------------------------------------------------
"""
WSGI config for djbank project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djbank.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
