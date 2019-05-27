# forever200

## About

Forever 200 is a super simple application that's purpose to provide a peak into the unsolicited traffic that is always going around the internet.

This was a simple project of mine just to experiment with Docker and haproxy. The code is intended to execute as the Docker container described, where all dependencies are packaged together.

To faciliate this Forever 200 makes use of at least a few components.

1)A raw TCP socket open. The TCP socket will respond "HTTP/1.1 200 Ok" to every request it receives (forever200_socket.py)

2)Memcache. The http bodies+headers received will be placed into memcache. Memcache is set to hold 101 entries, and then it just rolls over

3)HAproxy. Ha proxy will work as a reverse proxy, it will pass through all requests to "/home" to a homepage where you can view the requests

4)A Python site that lives on the aforementioned /home. It will query memcache and render a nice page. (home.py)

## Application Flow

The TCP Stream looks a bit like this:

                                                               |-----YES---->Route to bottle Server
                                                               |
                                                               |
                                                               |
Inbound port 80 -------> HAPROXY--Does Request contain /home?--|
                                                               |
                                                               |
                                                               |
                                                               |-----NO---->Route to Raw socket, return 200 ok

The HA proxy listens on publicIP:Port80
Bottle Server/Raw Socket can listen on any port on the loopback interface.

## Files

The Raw Socket Server: forever200_socket.py. Can be instantiated without arguments.

home.py: the "/home" server. runs on bottle.

## Dependencies

python-memcached
bottle
haproxy
memcached
paste

python requirements are available in requirements.txt. non-python dependencies are shown in the DockerFile

## Building and executing the docker file

`docker build --no-cache -t forever200`

`docker container run -d -p 80:80 forever200`