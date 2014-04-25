FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y curl mtr nmap openssh-server tcpdump
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys
ADD startup.sh /startup.sh
CMD ["/bin/bash", "/startup.sh"]
