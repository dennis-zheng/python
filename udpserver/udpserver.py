# -*- coding:UTF-8 -*-
from socket import *
import struct
import time
import string
import thread
import threading
import os
import ctypes
import sys
from SocketServer import ThreadingUDPServer

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def process():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(('', int(sys.argv[1])))
    while True:
        data, addr = udp_socket.recvfrom(4096)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'receive %d ' % (len(data)))
        print(addr)
        print("data", data[-10:])
        udp_socket.sendto(data, addr)
    thread.exit_thread()

def startService():
    thread.start_new_thread(process, ())
    while True:
        time.sleep(10)

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
