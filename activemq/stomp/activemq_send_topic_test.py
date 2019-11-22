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

logDS.init('activemq')
is_stop = False
gindex = 0

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        logDS.info('received an error "%s"' % message)
    def on_message(self, headers, message):
        logDS.info('received a message "%s"' % message)
        #print("headers",headers)
    def on_disconnected(self):
        logDS.info('disconnected.')

def thread_process2(index):
    loop_num = int(sys.argv[1])
    logDS.info("begin %d"%index)
    conn = stomp.Connection([('172.10.3.111', 61613)])
    conn.set_listener('', MyListener())
    conn.start()

    #conn.connect()
    conn.connect('guest', 'guest', wait=True)
    for i in range(loop_num):
        #time.sleep(1)
        headers = {}
        conn.send('/topic/test', 'a test message %d'%i, headers=headers)
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
