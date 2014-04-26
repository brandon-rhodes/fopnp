FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y bind9-host curl mtr ncftp nmap openssh-server python3-pip telnet tcpdump

ADD id_rsa     /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/*
RUN echo 'UserKnownHostsFile /dev/null' >> /etc/ssh/ssh_config
RUN echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config

ADD ca.crt /usr/local/share/ca-certificates/ca.crt
RUN update-ca-certificates

RUN useradd -d /home/brandon -m -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' brandon

ADD requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

ADD startup.sh /startup.sh
CMD ["/etc/init.d/ssh", "start", "-D"]
