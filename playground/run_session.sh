#!/bin/bash

cd "$(dirname ${BASH_SOURCE[0]})"
sudo -u brandon \
    PATH=/home/brandon/usr/3.4/bin:/bin:/usr/bin \
    python3 ../py3/run_session.py
