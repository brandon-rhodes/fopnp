FROM ubuntu:14.04
RUN apt-get update
RUN apt-get install -y bind9-host cython3 curl dnsutils libxml2-dev libxslt-dev lsof mtr ncftp nmap openssh-server python3-lxml python3-pip python3-zmq strace telnet traceroute tcpdump zlib1g-dev

# Install all third-party Python 3 packages used in the book

ADD requirements.txt /root/requirements.txt
RUN pip3 install -r /root/requirements.txt

# Prevent SSH from complaining about unknown hosts

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
CMD ["/etc/init.d/ssh", "start", "-D"]
