
========================
 The Network Playground
========================

The ``network.sh`` script in this directory uses the Mininet library to
build an example “playground” network which can be used to run the code
examples in the book against many different kinds of server.  Installing
the network’s dependencies and then building the network should require
only two commands under Ubuntu::

    $ sudo ./install.sh
    $ sudo ./network.sh -i

The ``h1`` and ``h2`` machines for which ``network.sh`` will launch
xterms when it is given the ``-i`` option are both located on the same
LAN in the playground — the one behind the firewall ``modemA`` that does
NAT before releasing their packets out into the wild:

.. image:: https://raw.githubusercontent.com/brandon-rhodes/fopnp/m/diagrams/playground.png

See the ``session.txt`` file for examples of how each script from the
book behaves when run against the hosts in the playground.
