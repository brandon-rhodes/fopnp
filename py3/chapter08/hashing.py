#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter08/hashing.py
# Hashes are a great way to divide work.

import hashlib

def alpha_shard(word):
    """Do a poor job of assigning data to servers by using first letters."""
    if word[0] < 'g':           # abcdef
        return 'server0'
    elif word[0] < 'n':         # ghijklm
        return 'server1'
    elif word[0] < 't':         # nopqrs
        return 'server2'
    else:                       # tuvwxyz
        return 'server3'

def hash_shard(word):
    """Assign data to servers using Python's built-in hash() function."""
    return 'server%d' % (hash(word) % 4)

def md5_shard(word):
    """Assign data to servers using a public hash algorithm."""
    data = word.encode('utf-8')
    return 'server%d' % (hashlib.md5(data).digest()[-1] % 4)

if __name__ == '__main__':
    words = open('/usr/share/dict/words').read().split()
    for function in alpha_shard, hash_shard, md5_shard:
        d = {'server0': 0, 'server1': 0, 'server2': 0, 'server3': 0}
        for word in words:
            d[function(word.lower())] += 1
        print(function.__name__[:-6])
        for key, value in sorted(d.items()):
            print('   {} {} {:.2}'.format(key, value, value / len(words)))
        print()
