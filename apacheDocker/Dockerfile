# Apache Reverse Proxy



# Get base Ubuntu image

FROM ubuntu



# Install Apache

RUN apt-get update

RUN apt-get install -y apache2

RUN a2enmod ssl



# Environement variables

ENV APACHE_RUN_USER www-data

ENV APACHE_RUN_GROUP www-data

ENV APACHE_LOG_DIR /var/log/apache2



# Add new config file

ADD ./000-default.conf /etc/apache2/sites-available/



# Add .key and .cert files for server to access
ADD ./172.17.0.3.key /etc/apache2/ssl
ADD ./172.17.0.3.cert /etc/apache2/ssl

RUN service apache2 restart

EXPOSE 5000



ENTRYPOINT ["/usr/sbin/apache2"]



MAINTAINER Andrew Tully, ariimoose@gmail.com
