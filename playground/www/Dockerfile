FROM fopnp/base
ADD custom_httpd.py /root/custom_httpd.py
ADD service.pem /root/service.pem
RUN echo 'exec /usr/bin/python3 /root/custom_httpd.py /root/service.pem /usr/share/doc/python' >> /startup.sh
