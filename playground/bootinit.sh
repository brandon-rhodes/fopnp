#!/bin/bash
#
# Given the presence of a working "boot2docker-cli" tool, use it to
# create a "boot2docker-vm" and then transform it into a "playground-vm"
# ready for release.

set -e

boot2docker-cli init

VBoxManage modifyvm boot2docker-vm --natpf1 h1,tcp,127.0.0.1,2201,,2201
VBoxManage modifyvm boot2docker-vm --natpf1 h2,tcp,127.0.0.1,2202,,2202
VBoxManage modifyvm boot2docker-vm --natpf1 h3,tcp,127.0.0.1,2203,,2203
VBoxManage modifyvm boot2docker-vm --natpf1 h4,tcp,127.0.0.1,2204,,2204

boot2docker-cli start
$(boot2docker-cli shellinit)

boot2docker-cli ssh /bin/sh <<'EOF'

    cd /var/lib/boot2docker
    sudo wget ftp://ftp.nl.netbsd.org/vol/2/metalab/distributions/tinycorelinux/4.x/x86/tcz/bridge-utils.tcz
    sudo mkdir fopnp
    sudo chown docker.staff fopnp
    git clone https://github.com/brandon-rhodes/fopnp.git
    sudo cp fopnp/playground/bootlocal.sh .
    fopnp/playground/build.sh

EOF

boot2docker-cli stop || sleep 1
VBoxManage modifyvm boot2docker-vm --name playground-vm
