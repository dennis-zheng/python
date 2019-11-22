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

is_new = False
cv = threading.Condition(threading.RLock())

def thread_process2(index):
    global is_new
    for i in range(10000):
        cv.acquire()
        if False == is_new:
            cv.wait()
        is_new = False
        cv.release()
        logDS.info("thread_process2 %d %d"%(index,i))
    logDS.info("thread_process2 exit %d"%(index))

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
        self.flag = False
    def run(self):
        thread_process2(self.index)
        self.flag = True

    def status(self):
        return self.flag

def check_thread_staus(thread_list):
    for t in thread_list:
        if False == t.status():
            return False
    return True

def startService():
    thread_list = []
    for i in range(4):
        thread = thread_process(i)
        thread.start()
        time.sleep(1)
        thread_list.append(thread)

    global is_new
    index = 0
    while False == check_thread_staus(thread_list):
    #for i in range(1000):
        #time.sleep(2)
        cv.acquire()
        is_new = True
        if False:
            cv.notify_all()
        else:
            cv.notify()
        if index%10000 == 0:
            logDS.info("xxxxxxxxxxxxxxxxxxxxxxxxxxx %d" % (index))
        cv.release()
        index = index+1
    logDS.info("xxxxxxxxxxxxxxxxxxxxxxxxxxx notify finished %d" % (index))

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
