# -*- coding:UTF-8 -*-
from socket import *
import commands
import struct
import time
import string
import thread
import MySQLdb
import os
import ctypes
import sys
import threading

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def write_db(): 
    dbhost = '127.0.0.1'
    dbport = 3306
    dbuser = 'root'
    dbpassword = '123456'
    dbdatabase = 'test'

    dbconn = 0
    cur = 0
    try:
        dbconn = MySQLdb.connect(dbhost, dbuser, dbpassword, dbdatabase, dbport, charset='utf8')
        cur = dbconn.cursor()
    except Exception,ex:
        print 'write_db connect 00 %s:%s'%(Exception,ex)
    while True:
        try:
            dbconn.ping()
        except Exception,ex:
            print 'write_db ping %s:%s'%(Exception,ex)
            print Exception,":",ex
            try:
                if cur and cur.connection:
                    cur.close()
                if dbconn and dbconn.open:
                    dbconn.close()
                dbconn = MySQLdb.connect(dbhost, dbuser, dbpassword, dbdatabase, dbport, charset='utf8')
                cur = dbconn.cursor()
                time.sleep(1)
            except Exception,ex:
                print Exception,":",ex
                time.sleep(1)
            continue
        try:
            for i in range(10):
                t1 = time.localtime(time.time())
                param.append([i,'test1','test2',time.strftime('%Y-%m-%d %H:%M:%S',t1),'http://test.com'])
            if True:
                sql_str = u'insert into %s' %'test'
                sql_str = sql_str + u'(id,test1,test2,timestamp,url) values (%d,%s,%s,%s,%s);'
                cur.executemany(sql_str,param)
        except Exception,ex:
            print 'write_db',Exception,":",ex
            try:
                if cur and cur.connection:
                    cur.close()
                if dbconn and dbconn.open:
                    dbconn.close()
                dbconn = MySQLdb.connect(dbhost, dbuser, dbpassword, dbdatabase, dbport, charset='utf8')
                cur = dbconn.cursor()
            except Exception,ex:
                print 'write_db 55 %s:%s'%(Exception,ex)
        time.sleep(1)
    if cur and cur.connection:
        cur.close()
    if dbconn and dbconn.open:
        dbconn.close()
    thread.exit_thread()

def startService():
    thread.start_new_thread(write_db, ())
    while True:
        time.sleep(10)

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
