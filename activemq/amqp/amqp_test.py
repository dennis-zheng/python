# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid
#from __future__ import print_function, unicode_literals
from proton import Message
from proton.handlers import MessagingHandler
from proton.reactor import Container

import logDS

logDS.init('amqp')
is_stop = False
gindex = 0

class HelloWorld(MessagingHandler):
    def __init__(self, address):
        #super(HelloWorld, self).__init__()
        self.address = address

    def on_start(self, event):
        conn = event.container.connect()
        event.container.create_receiver(conn, self.address)
        event.container.create_sender(conn, self.address)

    def on_sendable(self, event):
        event.sender.send(Message(body="Hello World!"))
        event.sender.close()

    def on_message(self, event):
        print(event.message.body)
        event.connection.close()

def thread_process2(index):
    logDS.info("begin %d"%index)
    Container(HelloWorld("examples")).run()
    logDS.info("exit %d"%index)

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        thread_process2(self.index)

def startService():
    thread_list = []
    for i in range(1):
        thread = thread_process(i)
        thread.start()
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
