# -*- coding:UTF-8 -*-
from socket import *
import commands
import struct
import time
import string
import thread
import redis
import os
import ctypes
import sys
import threading

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def write_redis():
    #TODO ...
    thread.exit_thread()

def startService():
    thread.start_new_thread(write_redis, ())
    while True:
        time.sleep(10)

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
