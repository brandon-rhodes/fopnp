#!/usr/bin/env python

import re
import sys

def shift_up(match):
    y = int(match.group(1))
    y -= 3
    return 'y="{}"'.format(y)

if __name__ == '__main__':
    path = sys.argv[1]
    with open(path) as f:
        body = f.read()

    lines = body.splitlines(True)
    for i, line in enumerate(lines):
        if '<filter' in line:
            #line = line.replace('height="1.504"', 'height="1.2"')
            #line = line.replace('y="-0.252"', 'y="1.0"')
            pass
        if 'stdD' in line:
            line = line.replace('stdDeviation="4.2"', 'stdDeviation="2.2"')
        if 'url(#filter_blur)' in line:
            line = line.replace('fill-opacity:1', 'fill-opacity:0.2')
            #line = re.sub(r'y="(\d+)"', shift_up, line)
        if 'sansserif' in line:
            line = line.replace('sansserif', 'Inconsolata')
            line = re.sub(r'y="(\d+)"', shift_up, line)
        lines[i] = line

    with open(path, 'w') as f:
        f.write(''.join(lines))
