FROM httpd:2.4
# RUN apt-get update -y
# RUN apt-get install -y apache2
# RUN a2enmod proxy
# RUN a2enmod proxy_http
COPY apache/httpd.conf /usr/local/apache2/conf/httpd.conf
ENV APACHE_LOG_DIR /var/log/apache2
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]
