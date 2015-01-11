#!/bin/sh
#
# Run "docker build" for each of the images that need to be created
# before the network playground can then be launched with "launch.sh".

set -e
cd $(dirname "$0")

# Generate an SSH identity pubic/private keypair that can be installed
# on all of the playground hosts, so users can SSH between them without
# needing a password.

if [ ! -f base/id_rsa ]
then
    ssh-keygen -f base/id_rsa -N ''
fi

# Copy our requirements.txt file into the "base" image directory.
# Preserve ("-p") attributes so that it does not look like we have
# modified the file every time, lest we trigger a Docker rebuild.

cp -p ../py2/requirements.txt ./base/requirements2.txt
cp -p ../py3/requirements.txt ./base/requirements.txt

# Rebuild all of our Docker images.

docker build --no-cache=true -t fopnp/base base
docker build -t fopnp/dns dns
docker build -t fopnp/ftp ftp
docker build -t fopnp/mail mail
docker build -t fopnp/www www
