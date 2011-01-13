#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 8 - queuecrazy.py
# Small application that uses several different message queues

import random, threading, time, zmq
zcontext = zmq.Context()

def fountain(url):
    """Produces a steady stream of words."""
    zsock = zcontext.socket(zmq.PUSH)
    zsock.bind(url)
    words = [ w for w in dir(__builtins__) if w.islower() ]
    while True:
        zsock.send(random.choice(words))
        time.sleep(0.4)

def responder(url, function):
    """Performs a string operation on each word received."""
    zsock = zcontext.socket(zmq.REP)
    zsock.bind(url)
    while True:
        word = zsock.recv()
        zsock.send(function(word))  # send the modified word back

def processor(n, fountain_url, responder_urls):
    """Read words as they are produced; get them processed; print them."""
    zpullsock = zcontext.socket(zmq.PULL)
    zpullsock.connect(fountain_url)

    zreqsock = zcontext.socket(zmq.REQ)
    for url in responder_urls:
        zreqsock.connect(url)

    while True:
        word = zpullsock.recv()
        zreqsock.send(word)
        print n, zreqsock.recv()

def start_thread(function, *args):
    thread = threading.Thread(target=function, args=args)
    thread.daemon = True  # so you can easily Control-C the whole program
    thread.start()

start_thread(fountain, 'tcp://127.0.0.1:6700')
start_thread(responder, 'tcp://127.0.0.1:6701', str.upper)
start_thread(responder, 'tcp://127.0.0.1:6702', str.lower)
for n in range(3):
    start_thread(processor, n + 1, 'tcp://127.0.0.1:6700',
                 ['tcp://127.0.0.1:6701', 'tcp://127.0.0.1:6702'])
time.sleep(30)
