# Flask container
#
# Version 1.0

# Get Ubuntu as base image
FROM ubuntu

#get python stuff to run flask apps
RUN apt-get install -y python-flask python-pymongo 

#add flask app into this container
ADD app.py /

#opening port for flask
EXPOSE 5000

#starts container
ENTRYPOINT python app.py


 
