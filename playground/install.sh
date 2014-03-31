#!/bin/bash
#
# Install the dependencies needed to run our Mininet and all of its
# services on Ubuntu.

sudo apt-get install dnsmasq dovecot-imapd dovecot-pop3d mininet
stop dovecot
mv /etc/dovecot/dovecot.conf /etc/dovecot/dovecot-OFF.conf
