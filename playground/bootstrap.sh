#!/bin/bash

set -e

cd /home/vagrant
git clone https://github.com/brandon-rhodes/fopnp.git
./fopnp/playground/build.sh
./fopnp/playground/launch.sh

# TODO: play.sh link?
