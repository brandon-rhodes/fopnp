FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y lsof man-db mtr nmap openssh-server strace traceroute
RUN apt-get install -y bind9-host curl dnsutils ftp telnet tcpdump zlib1g-dev
RUN apt-get install -y python-dev python3-dev python-pip python3-pip
RUN apt-get install -y python-crypto python-cssselect python-lxml python-zmq
RUN apt-get install -y python3-crypto python3-lxml python3-zmq

# Install all third-party Python packages used in the book

ADD requirements2.txt /root/requirements2.txt
RUN pip install -r /root/requirements2.txt

ADD requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# Support SSH between hosts without a password,
# and prevent SSH from prompting about unknown hosts

ADD id_rsa     /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/*
RUN echo 'UserKnownHostsFile /dev/null' >> /etc/ssh/ssh_config
RUN echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config

# Allow login to playground servers via SSH, preventing (in auth.log):
#    Cannot open /proc/self/loginuid: Read-only file system
#    set_loginuid failed

RUN sed -i /loginuid/s/^/#/ /etc/pam.d/sshd

# Accept certificates signed by our own CA

ADD ca.crt /usr/local/share/ca-certificates/ca.crt
RUN update-ca-certificates

# Give user "brandon" the password "abc123" on all hosts

RUN useradd -d /home/brandon -m -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' -s /bin/bash brandon

# Run SSH by default

ADD startup.sh /startup.sh
CMD ["/startup.sh"]
