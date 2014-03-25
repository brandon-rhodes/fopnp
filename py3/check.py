#!/usr/bin/env python3
#
# Check listings for sanity

import os

base = 'https://github.com/brandon-rhodes/fopnp/blob/m/py3/'

def main():
    for dirpath, dirnames, filenames in os.walk('.'):
        if dirpath == '.':
            continue
        if dirpath.startswith('./'):
            dirpath = dirpath[2:]
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            path = os.path.join(dirpath, filename)
            content = open(path).read()
            url = base + path
            if '\n# {}\n'.format(url) not in content:
                print(path)

if __name__ == '__main__':
    main()
