"""Introspect Python's SSL library and list its features and options.

This script was not included in the text of the book itself, but was a
useful enough tool to me while I was writing the book that I thought I
should leave it sitting around in the source code repository.

- Brandon Rhodes, for Foundations of Python Network Programming,
                      Third Edition

"""
try:
    import ssl
except ImportError:
    ssl = None

def main():
    if ssl is None:
        print('This Python is not compiled with SSL support')
        return
    names = dir(ssl)
    print()
    display(names, ' protocol ', lambda s: s.startswith('PROTOCOL_'))
    display(names, ' verify_mode ', lambda s: s.startswith('CERT_'))
    display(names, ' verify_flags ', lambda s: s.startswith('VERIFY_'))
    display(names, ' options ', lambda s: s.startswith('OP_'))
    display(names, ' feature availability ', lambda s: s.startswith('HAS_'))

def display(names, title, test):
    items = [(fix(getattr(ssl, name)), name) for name in names if test(name)]
    print(title.center(72, '-'))
    for value, name in sorted(items):
        print('{:27} {:10}  {:>32}'.format(name, value, bin(value)[2:]))
    print()

def fix(value):
    """Turn negative 32-bit numbers into positive numbers."""
    return (value + 2 ** 32) if (value < 0) else value

if __name__ == '__main__':
    main()
