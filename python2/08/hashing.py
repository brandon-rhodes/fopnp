#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 8 - hashing.py
# Hashes are a great way to divide work.

import hashlib

def alpha_shard(word):
    """Do a poor job of assigning data to servers by using first letters."""
    if word[0] in 'abcdef':
        return 'server0'
    elif word[0] in 'ghijklm':
        return 'server1'
    elif word[0] in 'nopqrs':
        return 'server2'
    else:
        return 'server3'

def hash_shard(word):
    """Do a great job of assigning data to servers using a hash value."""
    return 'server%d' % (hash(word) % 4)

def md5_shard(word):
    """Do a great job of assigning data to servers using a hash value."""
    # digest() is a byte string, so we ord() its last character
    return 'server%d' % (ord(hashlib.md5(word).digest()[-1]) % 4)

words = open('/usr/share/dict/words').read().split()

for function in alpha_shard, hash_shard, md5_shard:
    d = {'server0': 0, 'server1': 0, 'server2': 0, 'server3': 0}
    for word in words:
        d[function(word.lower())] += 1
    print function.__name__[:-6], d
