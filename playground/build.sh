#!/bin/sh
#
# Run "docker build" for each of the images that need to be created
# before the network playground can then be launched with "launch.sh".

set -e -x
cd $(dirname "$0")

# Make sure Docker is installed.

if [ ! -x /usr/bin/docker ]
then
    sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \
                     --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
    echo deb https://apt.dockerproject.org/repo ubuntu-trusty main \
         | sudo dd of=/etc/apt/sources.list.d/docker.list
    sudo apt-get update
    sudo apt-get -y install docker-engine
fi

# Our user must have rights to the "docker" group.

if ! echo "$(groups)" | grep -q docker
then
    sudo adduser vagrant docker
    exec newgrp docker < ./build.sh
fi

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

docker build -t fopnp/base base
docker build -t fopnp/dns dns
docker build -t fopnp/ftp ftp
docker build -t fopnp/mail mail
docker build -t fopnp/www www
