#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - sftp.py
# Fetching files with SFTP

import functools
import paramiko

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('127.0.0.1', username='test')  # password='')

def my_callback(filename, bytes_so_far, bytes_total):
    print 'Transfer of %r is at %d/%d bytes (%.1f%%)' % (
        filename, bytes_so_far, bytes_total, 100. * bytes_so_far / bytes_total)

sftp = client.open_sftp()
sftp.chdir('/var/log')
for filename in sorted(sftp.listdir()):
    if filename.startswith('messages.'):
        callback_for_filename = functools.partial(my_callback, filename)
        sftp.get(filename, filename, callback=callback_for_filename)

client.close()
