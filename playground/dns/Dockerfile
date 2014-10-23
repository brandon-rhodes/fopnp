FROM fopnp/base
RUN apt-get install -y dnsmasq
RUN echo 'user=root' >> /etc/dnsmasq.conf
RUN echo 'mx-host=example.com,mail.example.com,50' >> /etc/dnsmasq.conf
RUN echo 'exec dnsmasq --no-daemon --log-queries --no-resolv --no-hosts --addn-hosts=/root/hosts' >> /startup.sh
ADD hosts /root/hosts
ADD mx-entries /etc/dnsmasq.d/mx-entries
