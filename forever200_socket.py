#!/usr/bin/python
import socketserver
import memcache


class MyMemCacheClient():
    """
    A little something-something to handle working with the memcached server. 
    Mostly about delivering an easy way for the program to update the memcached
    The keypair will be a 0 indexed number, with the upper bound being max entries. 
    On boot it will listen to inbound connections and insert the http data into key pair 0, and increment all the way.
    if max value is reached, it rolls over and starts again
    """


    def __init__(self):
        self.memCacheServer = "127.0.0.1:1337"
        self.maxEntries = 100 # 24+0 = 25
        self.mc = memcache.Client([self.memCacheServer], debug=0)
        self.currIndex = 0


    def updateCache(self, value):
        if self.currIndex < self.maxEntries:
            self.mc.set(str(self.currIndex), value)
            self.currIndex = self.currIndex + 1
            return None
        if self.currIndex == self.maxEntries:
            self.currIndex = 0
            self.mc.set(str(self.currIndex), value)
            

    def returnCache(self):
        
        data = []
        i = 0
        while i < self.maxEntries:
            #try:
            data.append(self.mc.get(str(i)))
            #except:
              #  print "no data in range"
            i = i + 1
        return data
            





class MyTCPHandler(socketserver.BaseRequestHandler):
    
    ####Init Memcached Client Handler####
    
    

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(2096)
        #print "{} wrote:".format(self.client_address[0])
        self.request.sendall(b'HTTP/1.1 200 Ok\n\r\n\r\n')
        self.parser_master()

    def parser_master(self):
        #Route data payloads to parsers
        for i in self.data.splitlines():
            #print i
            i = i.decode('utf-8').split(" ", 1)
            print(i)
        mcClient.updateCache(self.data)


    #mc = memcache.client()








if __name__ == "__main__":
    
    global mcClient
    mcClient = MyMemCacheClient()

    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
    server.server_close()

