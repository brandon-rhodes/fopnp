#!/usr/bin/env python3
#
# Re-run session.txt and optionally update it inline.

import os
import re
from subprocess import PIPE, Popen, STDOUT

prompt = '$ '

def main():
    session_txt = open('session.txt', encoding='utf-8')
    results = []
    banner = '_' * 72

    lines = iter(session_txt)
    for line in lines:
        if line.strip() == banner:
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
           'PATH': os.environ['PATH']}
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
    output = re.sub(rb'Message-ID: <[\d.]+@guinness>',
                    b'Message-ID: <20140325211401.9307.43420@guinness>',
                    output)
    results.append(output.decode('utf-8'))

    open('session_out.txt', 'w', encoding='utf-8').write(''.join(results))

if __name__ == '__main__':
    main()
