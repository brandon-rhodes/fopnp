#!/bin/bash
#
# Install the dependencies needed to run our Mininet and all of its
# services on Ubuntu.

if [ "$(id -u)" != "0" ]
then
    echo 'Error: "install.sh" must be run as root; try: sudo ./install.sh'
    exit 2
fi

apt-get install dnsmasq dovecot-imapd dovecot-pop3d mininet telnetd

/etc/init.d/openbsd-inetd stop
update-rc.d openbsd-inetd disable

stop dovecot
mv /etc/dovecot/dovecot.conf /etc/dovecot/dovecot-OFF.conf
