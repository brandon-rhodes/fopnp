#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter11/manage.py
# The "manage.py" file produced by Django for the "djbank" application:
# ----------------------------------------------------------------------
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djbank.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
