#!/bin/bash
# Foundations of Python Network Programming

# Copy SSH credentials into "brandon" account.  (If this is done in the
# Dockerfile instead, the files cannot actually be read by the "brandon"
# user; see Docker issue 1295.)

mkdir -p /home/brandon/.ssh
cp /root/.ssh/id_rsa          /home/brandon/.ssh/id_rsa
cp /root/.ssh/id_rsa.pub      /home/brandon/.ssh/id_rsa.pub
cp /root/.ssh/authorized_keys /home/brandon/.ssh/authorized_keys
chown -R brandon.brandon /home/brandon
chmod -R og-rwx /home/brandon/.ssh

# Start up services on this particular host.  Each of the more specific
# containers that build atop "base" will append additional commands to
# this startup script.  If no other commands get appended, then we
# arrange for this shell to stay alive forever instead of exiting,
# because exiting would terminate the container.

sleep_for_ten_years () {
    sleep 315360000
}

if tail -1 "$0" | grep -q /etc/init.d/ssh
then
    trap sleep_for_ten_years EXIT
fi

/etc/init.d/rsyslog start
/etc/init.d/ssh start
