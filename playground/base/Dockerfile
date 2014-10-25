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

# Prevent SSH from prompting about unknown hosts.

RUN echo 'UseDNS no' >> /etc/ssh/sshd_config
RUN echo 'UserKnownHostsFile /dev/null' >> /etc/ssh/ssh_config
RUN echo 'StrictHostKeyChecking no' >> /etc/ssh/ssh_config

# Allow login to playground servers via SSH, preventing (in auth.log):
#    Cannot open /proc/self/loginuid: Read-only file system
#    set_loginuid failed

RUN sed -i /loginuid/s/^/#/ /etc/pam.d/sshd

# Accept certificates signed by our own CA

ADD ca.crt /usr/local/share/ca-certificates/ca.crt
RUN update-ca-certificates

# Give users "root" and "brandon" the password "abc123" on all hosts

RUN usermod -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' root
RUN useradd -d /home/brandon -G sudo -m -p '$6$sHTmsDVi$Spmhni61IjBGDsQBS/rYj1k4Do3u2HlI5qtCrPGn4mvqzogdagSjq0KqfeMXFpI2bqkg9OVOuZHEJOxtN.byy0' -s /bin/bash brandon

# Allow SSH login as root with a password.

RUN sed -i /PermitRootLogin/s/without-password/yes/ /etc/ssh/sshd_config

# Support SSH between hosts without a password.

RUN mkdir -p   /root/.ssh
ADD id_rsa     /root/.ssh/id_rsa
ADD id_rsa.pub /root/.ssh/id_rsa.pub
ADD id_rsa.pub /root/.ssh/authorized_keys
RUN chmod -R og-rwx /root/.ssh

# Allow "brandon" to "sudo" without a password.

RUN sed -i '/sudo/s/ALL$/NOPASSWD: ALL/' /etc/sudoers

# Prevent a minor error message from filling /var/log/auth.log from SSH:
# "Unable to open env file: /etc/default/locale: No such file or directory"

RUN update-locale

# Run SSH by default

ADD startup.sh /startup.sh
CMD ["/startup.sh"]
