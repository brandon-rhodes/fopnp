#!/bin/bash

set -e
cd "$(dirname ${BASH_SOURCE[0]})"

# Generate an SSH identity pubic/private keypair that can be installed
# on all of the playground hosts, so users can SSH between them without
# needing a password.

if ! [ -f base/id_rsa ]
then
    ssh-keygen -f base/id_rsa -N ''
fi

# Copy our requirements.txt file into the "base" image directory.

if ! diff ../py3/requirements.txt ./base/requirements.txt >/dev/null
then
    cp ../py3/requirements.txt ./base/requirements.txt
fi

# Rebuild all of our Docker images.

docker build -t fopnp/base base
docker build -t fopnp/dns dns
docker build -t fopnp/ftp ftp
docker build -t fopnp/mail mail
docker build -t fopnp/www www
