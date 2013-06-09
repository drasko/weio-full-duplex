from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

#import thread
import threading

from user import *

from WeioUserApi import *

class TestConnection(SockJSConnection):
    def on_message(self, msg):
        logging.info("Handshake successful")

    def on_open(self, info):
        logging.info("ON_OPEN")





if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    TestRouter = SockJSRouter(TestConnection, '/test')

    app = web.Application(TestRouter.urls)
    app.listen(8081)

    logging.info(" [*] Listening on 0.0.0.0:8081/test")

    WeioUserSetup()

    for key in attach.procs :
        print key
        #thread.start_new_thread(attach.procs[key].procFnc, attach.procs[key].procArgs)
        t = threading.Thread(target=attach.procs[key].procFnc, args=attach.procs[key].procArgs)
        t.daemon = True
        t.start()

    ioloop.IOLoop.instance().start()
