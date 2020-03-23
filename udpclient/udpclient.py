# -*- coding: utf-8 -*-
from socket import *
import struct
import time
import string
import thread
import os
import ctypes
import sys
from SocketServer import ThreadingUDPServer
import threading

def send_msg():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    #udp_socket.bind(('', int(sys.argv[1])))
    addr = (sys.argv[1], int(sys.argv[2]))

    dataT = 'this is client test'
    data = dataT
    #for i in range(500):
    #    data = dataT + data
    while True:
        udp_socket.sendto(data, addr)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'send %d ' % (len(data)))
        time.sleep(2)
    thread.exit_thread()

def startService():
    thread.start_new_thread(send_msg, ())

    while True:
        time.sleep(10)

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
