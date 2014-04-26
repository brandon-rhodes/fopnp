FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y bind9-host curl mtr nmap openssh-server tcpdump
RUN apt-get install -y bridge-utils
ADD id_rsa     /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/*
RUN echo 'UserKnownHostsFile /dev/null' >> /etc/ssh/ssh_config
RUN echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config
ADD startup.sh /startup.sh
CMD ["/etc/init.d/ssh", "start", "-D"]
