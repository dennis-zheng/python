# -*- coding:UTF-8 -*-
from socket import *
import commands
import struct
import time
import string
import thread
import threading
import os
import ctypes
import sys
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

ClientConnectList = []
lockClientConnect = threading.RLock()

class ClientConnect(Protocol):
    def __init__(self):
        self.m_data = ''
        self.lastTime = time.time()

    def connectionMade(self):
        global ClientConnectList
        lockClientConnect.acquire()
        ClientConnectList.append(self)
        lockClientConnect.release()
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'connect from',self.transport.client
        pass
    def connectionLost(self, reason):
        global ClientConnectList
        lockClientConnect.acquire()
        try:
            ClientConnectList.remove(self)
        except Exception,ex:
            print 'ClientConnect ClientConnectList.remove %s:%s'%(Exception,ex)
        lockClientConnect.release()
        print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),'disconnect from',self.transport.client
        pass
    def dataReceived(self, data):
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), 'receive %d '%(len(data)))
        self.lastTime = time.time()
        Msg = 'echo:' + data
        self.transport.write(data)
        time.sleep(0.5)

    def checkConnect(self):
        ret = 0
        if time.time() - self.lastTime > 60.0:
            ret = 1
            pass
        return ret
        
def chechClientConnect():
    global ClientConnectList
    while True:
        lockClientConnect.acquire()
        for clientCon in ClientConnectList: 
            if clientCon.checkConnect():
                clientCon.transport.loseConnection()
        lockClientConnect.release()
        time.sleep(10)
    thread.exit_thread()

def startService():
    thread.start_new_thread(chechClientConnect, ())

    factory_con = Factory()
    factory_con.protocol = ClientConnect
    reactor.listenTCP(int(sys.argv[1]), factory_con)
    reactor.run()

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
