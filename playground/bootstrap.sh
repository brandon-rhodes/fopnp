#!/bin/bash

set -e

cd /home/vagrant

git clone https://github.com/brandon-rhodes/fopnp.git

ln -s ../fopnp/playground/ssh-config .ssh/config
ln -s fopnp/playground/launch.sh .

./fopnp/playground/build.sh
./fopnp/playground/launch.sh
