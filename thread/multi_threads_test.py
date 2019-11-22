# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid

import logDS
logDS.init('%s'%uuid.uuid4())
is_stop = False
gindex = 0

def thread_process2(index):
    for i in range(100000):
        logDS.info("thread_process2 %d %d"%(index,i))
        if i%10000==0:
            logDS.show("thread_process2 %d %d"%(index,i), True)

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        thread_process2(self.index)

def startService():
    thread_list = []
    for i in range(10):
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
