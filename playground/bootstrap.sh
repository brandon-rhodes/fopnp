#!/bin/bash

set -e -x

cd /home/vagrant

if [ ! -d fopnp ]
then
    sudo -u vagrant git clone https://github.com/brandon-rhodes/fopnp.git
fi

sudo -u vagrant ln -fs ../fopnp/playground/ssh-config .ssh/config
sudo -u vagrant ln -fs fopnp/playground/launch.sh .

sudo -u vagrant ./fopnp/playground/build.sh
sudo -u vagrant ./fopnp/playground/launch.sh
