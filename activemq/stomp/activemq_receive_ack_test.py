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
conn = 0

def exitDS():
    global is_stop
    is_stop = True
    exit()

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        logDS.info('received an error "%s"' % message)
    def on_message(self, headers, message):
        logDS.info('received a message "%s"' % message)
        global conn
        for i in range(10):
            time.sleep(1)
            logDS.info('sleep %ds' % i)
        conn.ack(headers["message-id"], 0)
        #print(headers)

        #print("headers",headers)
    def on_disconnected(self):
        logDS.info('disconnected.')
        exitDS()

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
    global is_stop
    global conn
    try:
        conn = stomp.Connection([('172.10.3.111', 61613)])
        conn.set_listener('', MyListener())
        #conn.set_listener('stats', StatsListener())
        #conn.set_listener('print', PrintingListener())
        conn.start()
        #conn.connect()
        user = 'guest%d'%index
        password = user
        conn.connect(user, password, wait=True)
        #conn.subscribe('/queue/test', index)
        conn.subscribe('/queue/test', index, ack="client")
        while False == is_stop:
            time.sleep(2)
        conn.disconnect()
    except Exception as ex:
        logDS.error('thread_process2 %s:%s' % (Exception, ex))
        exitDS()

    logDS.info("exit %d"%index)

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        thread_process2(self.index)

def startService():
    thread_num = int(sys.argv[1])
    thread_list = []
    for i in range(thread_num):
        thread = thread_process(i)
        thread.start()
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
