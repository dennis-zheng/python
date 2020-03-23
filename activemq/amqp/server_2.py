import time
import glob
import sys
import os
import threading
import uuid
import optparse
from proton import Message, Url
from proton.handlers import MessagingHandler
from proton.reactor import Container

import logDS

logDS.init('amqp')
is_stop = False
gindex = 0

class Server(MessagingHandler):
    def __init__(self, url, address, index):
        super(Server, self).__init__()
        self.url = url
        self.address = address
        self.index = index

    def on_start(self, event):
        print("Listening on", self.url, self.index)
        self.container = event.container
        self.conn = event.container.connect(self.url)
        self.receiver = event.container.create_receiver(self.conn, self.address)
        self.server = self.container.create_sender(self.conn, None)

    def on_message(self, event):
        print("Received", event.message, self.index)
        self.server.send(Message(address=event.message.reply_to, body="%s_%d"%(event.message.body.upper(), self.index),
                            correlation_id=event.message.correlation_id))

parser = optparse.OptionParser(usage="usage: %prog [options]")
parser.add_option("-a", "--address", default="172.10.3.111:5672/examples",
                  help="address from which messages are received (default %default)")
opts, args = parser.parse_args()

url = Url(opts.address)

def thread_process2(index):
    logDS.info("begin %d"%index)
    try:
        Container(Server(url, url.path, index)).run()
    except KeyboardInterrupt:
        pass
    logDS.info("exit %d"%index)

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        thread_process2(self.index)

def startService():
    thread_list = []
    for i in range(2):
        thread = thread_process(i)
        thread.start()
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
