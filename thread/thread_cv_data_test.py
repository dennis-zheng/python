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

class DATA_LIST:
    def __init__(self):
        self.data_list = []
        self.lock = threading.RLock()
        pass

    def push_back(self, data):
        self.lock.acquire()
        self.data_list.insert(0,data)
        self.lock.release()

    def pop_front(self):
        data = 0
        self.lock.acquire()
        if len(self.data_list) > 0:
            data = self.data_list.pop()
        self.lock.release()
        return data

data_cache = DATA_LIST()

def thread_process2(index):
    global is_stop
    global is_new
    global data_cache
    indexT = 0
    while True:
        data = data_cache.pop_front()
        if data == 0:
            # must before cv.wait
            if is_stop:
                break
            cv.acquire()
            if False == is_new:
                cv.wait()
            is_new = False
            cv.release()
        indexT = indexT + 1
        if indexT%10000 == 0:
            logDS.info("thread_process2 %d %d %s"%(index, indexT ,data))
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
    thread_num = int(sys.argv[1])
    loop_time = int(sys.argv[2])
    thread_list = []
    for i in range(thread_num):
        thread = thread_process(i)
        thread.start()
        thread_list.append(thread)

    global is_stop
    global is_new
    global data_cache
    index = 0
    for i in range(loop_time):
        #time.sleep(2)
        data_cache.push_back("%d"%index)
        index = index + 1
        if index%10000 == 0:
            logDS.info("xxxxxxxxxxxxxxxxxxxxxxxxxxx %d" % (index))
        continue
        cv.acquire()
        is_new = True
        if False:
            cv.notify_all()
        else:
            cv.notify()
        cv.release()

    logDS.info("xxxxxxxxxxxxxxxxxxxxxxxxxxx notify finished %d" % (index))

    is_stop = True
    cv.acquire()
    is_new = True
    cv.notify_all()
    cv.release()

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    logDS.show("begin.", True)
    startService()
    logDS.show("exit.", True)
