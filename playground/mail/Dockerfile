FROM fopnp/base
RUN apt-get install -y dovecot-imapd dovecot-pop3d postfix
RUN apt-get install -y mailutils
ADD service.pem /root/service.pem
ADD sample-mbox /var/mail/brandon
RUN chown brandon.brandon /var/mail/brandon
RUN echo 'echo mail.example.com > /etc/mailname' >> /startup.sh
RUN echo '/etc/init.d/postfix start' >> /startup.sh
RUN echo 'dovecot -F' >> /startup.sh
CMD ["/startup.sh"]
