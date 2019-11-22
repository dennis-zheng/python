# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid
import stomp
#import logging
#logging.basicConfig()

import logDS

logDS.init('activemq.log')
is_stop = False
gindex = 0


class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)
    def on_message(self, headers, message):
        print('received a message "%s"' % message)

class StatsListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('StatsListener received an error "%s"' % message)
    def on_message(self, headers, message):
        print('StatsListener received a message "%s"' % message)

class PrintingListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('PrintingListener received an error "%s"' % message)
    def on_message(self, headers, message):
        print('PrintingListener received a message "%s"' % message)

def thread_process2(index):
    logDS.info("begin %d"%index)
    conn = stomp.Connection([('172.10.3.111', 61613)])
    conn.set_listener('', MyListener())
    #conn.set_listener('stats', StatsListener())
    #conn.set_listener('print', PrintingListener())
    conn.start()
    #conn.connect()
    conn.connect('guest', 'guest', wait=True)
    conn.subscribe('/queue/test', 123)
    for i in range(2):
        conn.send('/queue/test', 'a test message %d'%i)
    #conn.send(body=' '.join(sys.argv[1:]), destination='/queue/test')
    time.sleep(2)
    conn.disconnect()
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
