
============
 Playground
============

The ``network.py`` script in this directory uses the Mininet library to
build an example “playground” network which can be used to run the code
examples in the book against many different kinds of server.  Installing
the network’s dependencies and then building the network should require
only two commands under Ubuntu::

    $ sudo ./install.sh
    $ sudo ./network.py -i

The ``h1`` and ``h2`` machines for which the Mininet will launch xterms
are located on the same LAN, behind a firewall ``modemA`` that does NAT
before releasing their packets out into the wild:

.. image:: https://raw.githubusercontent.com/brandon-rhodes/fopnp/m/diagrams/playground.png

See the ``session.txt`` file for examples of how each script from the
book behaves when run against the hosts in the playground.
