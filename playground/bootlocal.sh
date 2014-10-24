#!/bin/sh
#
# This script is not necessary if you have Docker and want to try out
# the network playground.  In that case, simply run "./build.sh" and
# then "./launch.sh" and finally something like "./play.sh h1" in this
# directory and you should be off and running.
#
# The purpose of this script, by contrast, is to run the second of the
# above commands inside of the "boot2docker" virtual machine image that
# this project distributes to make the network playground easy to launch
# for people without Linux or any Docker experience.  When placed in the
# special location "/var/lib/boot2dockern/bootlocal.sh" and marked as
# executable inside of a "boot2docker" virtual machine, this script will
# start up the playground whenever the machine is booted.

exec &> /var/lib/boot2docker/bootlocal.log
rm -f /home/docker/'boot2docker, please format-me'
touch /home/docker/playground-is-starting-up

# Install the "brctl" command, which will disappear every time the
# "boot2docker" image is rebooted, directly from an image we keep here
# in the persistent directory.  (Letting "./launch.sh" do the install
# would instead try to download it afresh every time we boot.)

cd /var/lib/boot2docker
sudo -u docker tce-load -i bridge-utils.tcz

# Launch the machine images and configure the network.

cd fopnp/playground
sh -v ./launch.sh

# Masquerade incoming connections that then pass across our "docker0"
# bridge and into one of the virtual hosts, so that "h1" through "h4"
# can accept SSH connections from the outside world without needing
# default routes pointing toward the real outside world.

iptables --table nat --append POSTROUTING --out-interface docker0 -j MASQUERADE

# Give the user a convenient symlink to the "fopnp" repository.  We do
# this last, as a signal to the user that the playground has finished
# being set up.

ln -s /var/lib/boot2docker/fopnp /home/docker
ln -s /var/lib/boot2docker/fopnp/playground/play.sh /home/docker/play.sh
rm -f /home/docker/playground-is-starting-up
