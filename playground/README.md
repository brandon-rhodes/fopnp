:[Return to the Table of Contents](https://github.com/brandon-rhodes/fopnp#readme)

# The Network Playground

To help readers of *Foundations of Python Network Programming* who want
to explore client and server programming on a network where they have
complete control and can capture packets wherever they wish, I have
created 5 Docker images together with a script that configures them as a
12-machine network that roughly resembles the Internet in miniature.

  * Four machines `h1`, `h2`, `h3`, and `h4` represent the kind of
    network clients that you might use at home or in a coffee shop.

  * Those machines live behind “broadband modems” `modemA` and `modemB`
    that do network address translation (NAT) so that outbound, but not
    inbound, connections can be made to the rest of the network.

  * The modems are connected to the rest of the world through a pair of
    routers `isp` and `backbone`.

  * At the other end of the world is the `example.com` machine room
    whose gateway, named `example`, routes packets to three machines
    `ftp`, `mail`, and `www`.  Each machine can each be addressed either
    using a short hostname like `ftp` or else a fully qualified name
    like `ftp.example.com`.

.. image:: https://raw.githubusercontent.com/brandon-rhodes/fopnp/m/diagrams/playground.png

The network services running on the machines are:

  * All hosts
    * SSH on port 22
  * `backbone`
    * DNS on port 53
  * `ftp.example.com`
    * FTP on port 21
    * Telnet on port 23
  * `mail.example.com`
    * SMTP on port 25
    * POP3 on port 110
    * POP3S on port 995
    * IMAP on port 143
    * IMAPS on port 993
  * `www.example.com`
    * HTTP on port 80
    * HTTPS on port 443

You can verify that these ports are open by connecting to them
individually or else by running `nmap` — which is available on every
machine in the network — against one of the other hosts.

## Launching the Playground

?

    $ ./play.sh h1

    root@h1:/# pwd
    /

    root@h1:/# traceroute backbone
    traceroute to backbone (10.1.1.1), 30 hops max, 60 byte packets
     1  192.168.1.1 (192.168.1.1)  0.193 ms  0.117 ms  0.120 ms
     2  isp (10.25.1.1)  0.572 ms  0.176 ms  0.186 ms
     3  backbone (10.1.1.1)  0.250 ms  0.210 ms  0.302 ms

## Building the Playground

If you want to build the playground yourself instead of using the
pre-packaged virtual machine image, there are three basic steps.

  * Either install Docker on a 64-bit Linux machine if your own or boot
    a virtual machine that has Docker installed and running.  I myself
    often use [boot2docker](https://github.com/boot2docker/boot2docker).
    You will also need `git` on the machine.

  * Check out this source code repository.

        $ git clone https://github.com/brandon-rhodes/fopnp.git
        $ cd fopnp/playground

  * Build the five Docker images.

        $ ./build.sh

  * Start the images and configure the network fabric between them.

        $ ./launch.sh

Once the above steps are completed, you should be able to get a root
prompt on any of the machines by using the `play.sh` script.

    $ ./play.sh h1

    root@h1:/# pwd
    /

    root@h1:/# traceroute www.example.com
    traceroute to www.example.com (10.130.1.4), 30 hops max, 60 byte packets
     1  192.168.1.1 (192.168.1.1)  0.294 ms  0.167 ms  0.183 ms
     2  isp (10.25.1.1)  1.002 ms  0.220 ms  0.218 ms
     3  backbone (10.1.1.1)  0.358 ms  0.259 ms  0.256 ms
     4  example.com (10.130.1.1)  0.500 ms  0.286 ms  0.355 ms
     5  www.example.com (10.130.1.4)  0.722 ms  0.662 ms  0.475 ms
