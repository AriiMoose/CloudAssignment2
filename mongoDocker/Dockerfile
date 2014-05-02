# MongoDB
#
# Version 1.0

# Use Ubuntu as the base image
FROM ubuntu

# 10gen official apt source to source list
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
RUN echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/10gen.list

# Divert initctl 
RUN dpkg-divert --local --rename --add /sbin/initctl && rm -f /sbin/initctl && ln -s /bin/true /sbin/initctl


# Install MongoDB
RUN apt-get update
RUN apt-get install mongodb-10gen

# Data director for MongoDB
RUN mkdir -p /data/db

# Expose Mongo port and define entrypoint
EXPOSE 27017
ENTRYPOINT ["usr/bin/mongod"]

# Specify maintainer
MAINTAINER Andrew Tully, ariimoose@gmail.com
