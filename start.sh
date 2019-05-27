#!/bin/bash


#This script is the CMD of the docker file. it simply runs all the components (haproxy,memcached, and the two python scripts)

set -m

haproxy -- forever200/haproxy.cfg &

memcached -u haproxy -d -p 1337

sudo -u haproxy python3 forever200/forever200_socket.py &
sudo -u haproxy python3 forever200/home.py &

fg %1
