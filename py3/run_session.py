#!/usr/bin/env python3
#
# Re-run session.txt and optionally update it inline.

import os
import re
from subprocess import PIPE, Popen, STDOUT

prompt = '$ '

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    session_txt = open('session.txt', encoding='utf-8')
    results = []
    banner = ' ' * 40 + '~' * 32

    lines = iter(session_txt)
    for line in lines:
        if line.rstrip() == banner:
            continue
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
    env = {'LANG': 'en_US.UTF-8', 'PS1': banner + '\n' + '$ ',
           'PATH': os.environ['PATH'], 'PYTHONPATH': '../monkeys',
           'PYTHONDONTWRITEBYTECODE': '1'}
    p = Popen([
        '/bin/sh',
        '-i',  # interactive: print PS1 prompt before each line
        '-v',  # verbose: echo commands, even without an input tty
        ], stdin=PIPE, stdout=PIPE, stderr=STDOUT, env=env)
    output, code = p.communicate(shell_input)
    output = output.replace(b'$ \n', b'')
    output = re.sub(rb'Date: .*',
                    b'Date: Tue, 25 Mar 2014 17:14:01 -0400',
                    output)
    results.append(output.decode('utf-8'))

    open('session.txt', 'w', encoding='utf-8').write(''.join(results))

if __name__ == '__main__':
    main()
