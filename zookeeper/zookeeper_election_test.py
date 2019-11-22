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

def my_leader_function():
    logDS.info("my_leader_function")
    time.sleep(5)

def thread_process2(index):
    logDS.info("begin %d"%index)
    zk = KazooClient(hosts='172.10.3.111:2181', logger=logDS.logger)
    zk.start()
    root = "/electionpath"
    election = zk.Election(root, "identifier:%d"%0)

    # blocks until the election is won, then calls
    # my_leader_function()
    election.run(my_leader_function)
    print(election.contenders())
    #logDS.info("thread_process2 88")
    #time.sleep(10)
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
        time.sleep(1)
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
