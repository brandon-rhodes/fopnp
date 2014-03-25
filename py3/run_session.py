#!/usr/bin/env python3
#
# Re-run session.txt and optionally update it inline.

import os
from subprocess import PIPE, Popen, STDOUT

prompt = '$ '

def main():
    session_txt = open('session.txt', encoding='utf-8')
    results = []

    lines = iter(session_txt)
    for line in lines:
        if line.startswith(prompt):
            break
        results.append(line)

    commands = []
    while True:
        command = line[2:]
        commands.append(command)
        for line in lines:
            if line.startswith(prompt):
                break
        else:
            break

    shell_input = ''.join(commands).encode('ascii')
    env = {'PS1': '$ ', 'PATH': os.environ['PATH']}
    p = Popen([
        '/bin/sh',
        '-i',  # interactive: print PS1 prompt before each line
        '-v',  # verbose: echo commands, even without an input tty
        ], stdin=PIPE, stdout=PIPE, stderr=STDOUT, env=env)
    output, code = p.communicate(shell_input)
    results.append(output.decode('utf-8'))

    open('session2.txt', 'w', encoding='utf-8').write(''.join(results))

if __name__ == '__main__':
    main()
