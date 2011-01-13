#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 16 - ssh_commands.py
# Running separate commands instead of using a shell

import paramiko

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return

client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect('127.0.0.1', username='test')  # password='')

for command in 'echo "Hello, world!"', 'uname', 'uptime':
    stdin, stdout, stderr = client.exec_command(command)
    stdin.close()
    print repr(stdout.read())
    stdout.close()
    stderr.close()

client.close()
