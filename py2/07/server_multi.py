#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - server_multi.py
# Using multiple threads or processes to serve several clients in parallel.

import sys, time, lancelot
from multiprocessing import Process
from server_simple import server_loop
from threading import Thread

WORKER_CLASSES = {'thread': Thread, 'process': Process}
WORKER_MAX = 10

def start_worker(Worker, listen_sock):
    worker = Worker(target=server_loop, args=(listen_sock,))
    worker.daemon = True  # exit when the main process does
    worker.start()
    return worker

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[2] not in WORKER_CLASSES:
        print >>sys.stderr, 'usage: server_multi.py interface thread|process'
        sys.exit(2)
    Worker = WORKER_CLASSES[sys.argv.pop()]  # setup() wants len(argv)==2

    # Every worker will accept() forever on the same listening socket.

    listen_sock = lancelot.setup()
    workers = []
    for i in range(WORKER_MAX):
        workers.append(start_worker(Worker, listen_sock))

    # Check every two seconds for dead workers, and replace them.

    while True:
        time.sleep(2)
        for worker in workers:
            if not worker.is_alive():
                print worker.name, "died; starting replacement worker"
                workers.remove(worker)
                workers.append(start_worker(Worker, listen_sock))
