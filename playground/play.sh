#!/bin/sh

if [ -z "$1" -o -n "$2" ]
then
    cat <<'EOF'
usage: play.sh HOST

Hosts available in the playground:
    h1, h2, h3      Hosts behind broadband modemA
    h4              Host behind broadband modemB
    modemA, modemB  Broadband modems doing NAT
    isp, backbone   Internet routers
    example         The gateway machine of example.com
    ftp, mail, www  Servers behind the example.com gateway

               backbone
              /        \
           isp          example
          /   \        /   |   \
     modemA   modemB  ftp mail www
    /  |  \     |
    h1 h2 h3    h4

EOF
    exit
fi

exec docker exec -it $1 /bin/bash
