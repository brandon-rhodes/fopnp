#!/bin/bash

set -e -x

cd /home/vagrant

if [ ! -d fopnp ]
then
    git clone https://github.com/brandon-rhodes/fopnp.git
fi

ln -fs ../fopnp/playground/ssh-config .ssh/config
ln -fs fopnp/playground/launch.sh .

./fopnp/playground/build.sh
./fopnp/playground/launch.sh
