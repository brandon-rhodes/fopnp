FROM fopnp/base
RUN apt-get install -y telnetd vsftpd
RUN mkdir -p /var/run/vsftpd/empty
ADD ftp.crt /root/ftp.crt
ADD ftp.key /root/ftp.key
RUN sed -i /^rsa_cert/s:=.*:=/root/ftp.crt: /etc/vsftpd.conf
RUN sed -i /^rsa_priv/s:=.*:=/root/ftp.key: /etc/vsftpd.conf
RUN echo 'write_enable=YES' >> /etc/vsftpd.conf
RUN echo '/etc/init.d/openbsd-inetd start' >> /startup.sh
RUN echo '/usr/sbin/vsftpd' >> /startup.sh
