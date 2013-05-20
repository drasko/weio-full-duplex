# -*- coding: utf-8 -*-
"""
    Simple sockjs-tornado application. By default will listen on port 8080.
"""
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options
import tornado.gen

import sockjs.tornado

import subprocess
import json

import time

import thread

def WeioGetConfig() :
    command = "/sbin/ifconfig"
    output = "PLACEHOLDER"

    try :
        output = subprocess.check_output(command)
    except :
        output = "ERR_CFG"
	
    print output
    return output


class TestConnection(sockjs.tornado.SockJSConnection):
    def on_message(self, msg):
        logging.info("Button pressed")
        #msg = WeioGetConfig()

        wcfg = {};
        wcfg['id'] = 1
        wcfg['name'] = 'Drasko DRASKOVIC'
        wcfg['size'] = 190
		 
        self.send(json.dumps(wcfg))

    def on_open(self, info):
		 logging.info("Socket OPEN")

def MainProgram() :
    for a in range(1000) :
        print(str(a))
        time.sleep(0.5)


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    TestRouter = sockjs.tornado.SockJSRouter(TestConnection, '/test')

    app = tornado.web.Application(TestRouter.urls)
    app.listen(8082)

    logging.info(" [*] Listening on 0.0.0.0:8082/test")

    thread.start_new_thread(MainProgram, ())

    tornado.ioloop.IOLoop.instance().start()
