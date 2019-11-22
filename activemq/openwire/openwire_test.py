# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid

#import logging
#logging.basicConfig()

import logDS

logDS.init('openwire')
is_stop = False
gindex = 0


def thread_process2(index):
    logDS.info("begin %d"%index)
    
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
