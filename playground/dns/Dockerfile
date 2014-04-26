FROM fopnp/base
RUN apt-get install -y dnsmasq
RUN echo 'user=root' >> /etc/dnsmasq.conf
RUN echo 'mx-host=example.com,mail.example.com,50' >> /etc/dnsmasq.conf
RUN echo 'exec dnsmasq --keep-in-foreground --no-resolv --no-hosts --addn-hosts=/root/hosts' >> /startup.sh
ADD hosts /root/hosts
CMD ["/startup.sh"]
