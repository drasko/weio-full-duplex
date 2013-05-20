# -*- coding: utf-8 -*-
"""
    Simple sockjs-tornado application. By default will listen on port 8080.
"""
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.options

import sockjs.tornado

import subprocess
import json

import time

import tornado.gen

import thread



import StringIO
import string, sys



#old_stdout = sys.stdout
#sys.stdout = weiostdout = StringIO.StringIO()
weiostdout = StringIO.StringIO()


#old_stdout = sys.stderr
#sys.stderr = weiostderr = StringIO.StringIO()
weiostderr = StringIO.StringIO()


STDOUT = STDERR = False


class StdoutConnection(sockjs.tornado.SockJSConnection):
    def on_open(self, info):
        global STDOUT
        logging.info("stdout Socket OPEN")
        STDOUT = True

        tornado.ioloop.PeriodicCallback(self.send_stdout, 10).start()

    def send_stdout (self) :
        out = weiostdout.read()
        #out = "HELLO STDOUT"
        self.send(json.dumps(out))


class StderrConnection(sockjs.tornado.SockJSConnection):
    def on_open(self, info):
        global STDERR
        logging.info("stderr Socket OPEN")
        STDERR = True

        tornado.ioloop.PeriodicCallback(self.send_stderr, 10).start()
    
    def send_stderr (self) :
        out = weiostderr.read()
        #out = "HELLO STDERR"
        self.send(json.dumps(out))



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


def MainProgram():
    while (STDOUT is False and STDERR is False) :
        pass

    i = 0
    while (1) :
        print(i)
        weiostdout.write(i)
        i = i+1
        time.sleep(1)


if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    TestRouter = sockjs.tornado.SockJSRouter(TestConnection, '/test')
    StdoutRouter = sockjs.tornado.SockJSRouter(StdoutConnection, '/stdout')
    StderrRouter = sockjs.tornado.SockJSRouter(StderrConnection, '/stderr')

    app = tornado.web.Application(TestRouter.urls + StdoutRouter.urls + StderrRouter.urls)
    app.listen(8082)

    logging.info(" [*] Listening on 0.0.0.0:8082/test")


    thread.start_new_thread(MainProgram, ())

    ioloop = tornado.ioloop.IOLoop.instance()
    ioloop.start()
