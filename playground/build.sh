#!/bin/bash

set -e
cd "$(dirname ${BASH_SOURCE[0]})"

if ! [ -f base/id_rsa ]
then
    ssh-keygen -f base/id_rsa -N ''
fi

docker build -t fopnp/base base
docker build -t fopnp/dns dns
docker build -t fopnp/ftp ftp
docker build -t fopnp/www www
