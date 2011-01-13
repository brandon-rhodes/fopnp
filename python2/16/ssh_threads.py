#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - ssh_threads.py
# Running two remote commands simultaneously in different channels

import threading
import paramiko

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('127.0.0.1', username='test')  # password='')

def read_until_EOF(fileobj):
    s = fileobj.readline()
    while s:
        print s.strip()
        s = fileobj.readline()

out1 = client.exec_command('echo One;sleep 2;echo Two;sleep 1;echo Three')[1]
out2 = client.exec_command('echo A;sleep 1;echo B;sleep 2;echo C')[1]
thread1 = threading.Thread(target=read_until_EOF, args=(out1,))
thread2 = threading.Thread(target=read_until_EOF, args=(out2,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

client.close()
