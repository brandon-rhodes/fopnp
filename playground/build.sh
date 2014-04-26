#!/bin/bash

set -e
cd "$(dirname ${BASH_SOURCE[0]})"

if ! [ -f base/id_rsa ]
then
    ssh-keygen -f base/id_rsa -N ''
fi

cat ../py3/requirements.txt | grep -v pygeo > ./base/requirements.txt.new
if diff ./base/requirements.txt ./base/requirements.txt.new >/dev/null
then
    rm ./base/requirements.txt.new
else
    mv ./base/requirements.txt.new ./base/requirements.txt
fi

docker build -t fopnp/base base
docker build -t fopnp/dns dns
docker build -t fopnp/ftp ftp
docker build -t fopnp/mail mail
docker build -t fopnp/www www
