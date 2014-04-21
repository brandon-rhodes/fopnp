#!/usr/bin/env python3
#
# Re-run session.txt and replace its contents with fresh output.  You
# probably want to run this from inside of the project's playground, or
# most of the commands in session.txt will return errors about bad IP
# addresses or hostnames.

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
        command = line[len(prompt):]
        commands.append(command)
        for line in lines:
            if line.startswith(prompt):
                break
        else:
            break

    shell_input = ''.join(commands).encode('ascii')
    env = {'LANG': 'en_US.UTF-8', 'PS1': banner + '\n' + prompt,
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
    results.append(output.decode('utf-8')
        .replace("/bin/sh: 0: can't access tty; job control turned off\n", ''))

    open('session.txt', 'w', encoding='utf-8').write(''.join(results))

if __name__ == '__main__':
    main()
