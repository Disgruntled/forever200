FROM ubuntu:latest
# gets the base image

COPY * forever200/

RUN apt-get update 
RUN apt-get install haproxy -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install memcached -y
RUN apt-get install sudo -y
RUN pip3 install -r forever200/requirements.txt



# Runs this command 

CMD /bin/bash forever200/start.sh

