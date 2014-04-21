# SMTP server.

import asyncore
import smtpd
import ssl

class MySMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print((peer, mailfrom, rcpttos, data))

def main():
    MySMTPServer(('0.0.0.0', 25), None)
    asyncore.loop()

if __name__ == '__main__':
    main()
