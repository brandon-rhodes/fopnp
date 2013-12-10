#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - lancelot_tests.py
# Test suite that can be run against the Lancelot servers.

from funkload.FunkLoadTestCase import FunkLoadTestCase
import socket, os, unittest, lancelot

SERVER_HOST = os.environ.get('LAUNCELOT_SERVER', 'localhost')

class TestLancelot(FunkLoadTestCase):
    def test_dialog(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((SERVER_HOST, lancelot.PORT))
        for i in range(10):
            question, answer = lancelot.qa[i % len(launcelot.qa)]
            sock.sendall(question)
            reply = lancelot.recv_until(sock, '.')
            self.assertEqual(reply, answer)
        sock.close()

if __name__ == '__main__':
    unittest.main()
