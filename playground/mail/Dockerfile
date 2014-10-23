FROM fopnp/base
RUN apt-get install -y dovecot-imapd dovecot-pop3d postfix
RUN apt-get install -y mailutils
RUN sed -i /myhostname/d /etc/postfix/main.cf
RUN sed -i /mydestination/d /etc/postfix/main.cf
RUN echo 'myhostname = mail.example.com' >> /etc/postfix/main.cf
RUN echo 'mydestination = mail.example.com, example.com, localhost.localdomain, localhost' >> /etc/postfix/main.cf
ADD service.pem /root/service.pem
ADD sample-mbox /var/mail/brandon
RUN chown brandon.brandon /var/mail/brandon
RUN cp /var/mail/brandon /root/var.mail.brandon.backup
RUN echo 'echo example.com > /etc/mailname' >> /startup.sh
RUN echo '/etc/init.d/postfix start' >> /startup.sh
RUN echo 'dovecot -F' >> /startup.sh
