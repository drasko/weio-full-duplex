from tornado import web, ioloop
from sockjs.tornado import SockJSRouter, SockJSConnection

import sys
import json

#import thread
import threading

from user import *

sys.path.append(r'./')
from weioLib.weioUserApi import *

from weio_main import *

class TestConnection(SockJSConnection):
    def on_message(self, msg):
        logging.info("Handshake successful")

        data = {};
        data['id'] = 1
        data['name'] = 'Drasko DRASKOVIC'
        data['size'] = 777
		 
        self.send(json.dumps(data))

    def on_open(self, info):
        logging.info("ON_OPEN")



if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    TestRouter = SockJSRouter(TestConnection, '/test')

    app = web.Application(TestRouter.urls)
    app.listen(8082)

    logging.info(" [*] Listening on 0.0.0.0:8082/test")

    WeioUserSetup()

    for key in attach.procs :
        print key
        #thread.start_new_thread(attach.procs[key].procFnc, attach.procs[key].procArgs)
        t = threading.Thread(target=attach.procs[key].procFnc, args=attach.procs[key].procArgs)
        t.daemon = True
        t.start()

    ioloop.IOLoop.instance().start()


