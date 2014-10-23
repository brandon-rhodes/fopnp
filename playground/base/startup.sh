#!/bin/bash
# Foundations of Python Network Programming
#
# Start up services on this particular host.  Each kind of host that
# exists in the networking playground will append additional commands to
# this startup script using RUN commands in their Dockerfiles.

if tail -1 "$0" | grep -q /etc/init.d/ssh
then
    ssh_options="-D"  # if no commands follow "ssh", run it in foreground
fi

/etc/init.d/rsyslog start
/etc/init.d/ssh start $ssh_options
