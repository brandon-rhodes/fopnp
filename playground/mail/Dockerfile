FROM fopnp/base
RUN apt-get install -y dovecot-imapd dovecot-pop3d postfix
RUN apt-get install -y mailutils
ADD service.pem /root/service.pem
ADD sample-mbox /var/mail/brandon
RUN chown brandon.brandon /var/mail/brandon
RUN echo dovecot >> /startup.sh
RUN echo /bin/sleep 999999 >> /startup.sh
CMD ["/startup.sh"]
