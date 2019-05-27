#!/usr/bin/python
from bottle import Bottle, run

from forever200_socket import MyMemCacheClient


global mc

if __name__ == "__main__":


    mc = MyMemCacheClient()
    app = Bottle()

    @app.route('/home')
    def index():
        
        i = 0
        mcData = mc.returnCache()

        for i in range(len(mcData)):
            mcData[i] = "<p><b>%s:</b>%s</p>" % (str(i), mcData[i])

        return mcData

    run(app, server='paste',host="0.0.0.0", port=8080)
