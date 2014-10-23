FROM fopnp/base
ADD custom_httpd.py /root/custom_httpd.py
ADD service.pem /root/service.pem
RUN pip3 install httpbin gunicorn
RUN echo 'gunicorn -D --bind :443 --log-syslog --certfile /root/service.pem httpbin:app' >> /startup.sh
RUN echo 'gunicorn --bind :80 --log-syslog httpbin:app' >> /startup.sh
