# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid
from kazoo.client import KazooClient
#import logging
#logging.basicConfig()

import logDS

logDS.init('logDS_%s.log'%uuid.uuid4())
is_stop = False
gindex = 0

def thread_process2(index):
    logDS.info("begin %d"%index)
    zk = KazooClient(hosts='172.10.3.111:2181', logger=logDS.logger)
    zk.start()
    node = "/my/lockpath"
    lock = zk.Lock(node, "my-identifier")
    with lock:  # blocks waiting for lock acquisition
        # do something with the lock
        logDS.info("get the lock %d"%index)
        global gindex
        if gindex != index:
            logDS.error("error xxxx %d %d" % (gindex, index))
        gindex = gindex+1
        if index == 0:
            time.sleep(10)
    zk.stop()
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
        time.sleep(0.01)
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
