# -*- coding: utf-8 -*-
import socket
import commands
import struct
import time
import string
import thread
import os
import ctypes
import sys
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, ClientFactory, Factory
import json
import threading

ClientList = []
lockClientList = threading.RLock()

def send_msg():
    global ClientList
    global lockClientList

    data = 'this is client test'
    while True:
        lockClientList.acquire()
        try:
            if data != 0:
                for sockDS in ClientList:
                    sockDS.sendData(data)
        except Exception,ex:
            print 'send_msg %s:%s'%(Exception,ex)
        lockClientList.release()
        time.sleep(2)
    thread.exit_thread()   

class ClientConnect(Protocol):
    def __init__(self):
        self.m_data = ''
        self.lastTime = time.time()
        pass
    def connectionMade(self):
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'connect from',self.transport
        global ClientList
        global lockClientList
        lockClientList.acquire()
        ClientList.append(self)
        lockClientList.release()
        pass
    def connectionLost(self, reason):
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'disconnect from',self.transport
        global ClientList
        global lockClientList
        lockClientList.acquire()
        try:
            ClientList.remove(self)
        except Exception,ex:
            print 'ClientList.remove %s:%s'%(Exception,ex)
        lockClientList.release()
        pass
    def dataReceived(self, data):
        self.lastTime = time.time()
        print 'recv:',data
        pass
    def sendData(self, data):
        try:
            self.transport.write(data)
        except Exception,ex:
            print 'sendData %s:%s'%(Exception,ex)
        pass

class ClientConnectImp(ClientFactory):
    def startedConnecting(self, connector):
        pass 
    def buildProtocol(self, addr):       
        return ClientConnect()  
    def clientConnectionLost(self, connector, reason):
        connector.connect()
        pass  
    def clientConnectionFailed(self, connector, reason):
        connector.connect()
        pass

def startService():
    thread.start_new_thread(send_msg, ())

    reactor.connectTCP(sys.argv[1], int(sys.argv[2]), ClientConnectImp())
    reactor.run()

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
