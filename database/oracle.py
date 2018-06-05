# -*- coding:UTF-8 -*-
from socket import *
import commands
import struct
import time
import string
import thread
import cx_Oracle
import os
import ctypes
import sys
import threading

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

def write_oracle():
    oraclehost = '127.0.0.1'
    oracleport = 1521
    oracleuser = 'root'
    oraclepassword = '123456'
    oracledatabase = 'ORCL'

    conn = 0
    curs = 0
    try:
        dsn=cx_Oracle.makedsn(oraclehost, oracleport, oracledatabase)
        conn=cx_Oracle.connect(oracleuser, oraclepassword, dsn)
        curs=conn.cursor()
    except Exception,ex:
        print 'write_oracle connect 00 %s:%s'%(Exception,ex)
    while True:
        try:
            conn.ping()
        except Exception,ex:
            print 'write_oracle ping %s:%s'%(Exception,ex)
            try:
                dsn=cx_Oracle.makedsn(oraclehost, oracleport, oracledatabase)
                conn=cx_Oracle.connect(oracleuser, oraclepassword, dsn)
                curs=conn.cursor()
                time.sleep(1)
            except Exception,ex:
                print 'write_oracle connect %s:%s'%(Exception,ex)
                time.sleep(1)
            continue
        try:
            if len(write_oracle_list) > 0:
                #print 'ok can write to oracle'
                sql_str = ''
                param=[]
                for i in range(10):
                    t1 = time.localtime(time.time())
                    sql_str = u'insert into %s (id,test1,test2,timestamp,url) values (%d,\'%s\',\'%s\',to_timestamp(\'%s\',\'yyyy-mm-dd hh24:mi:ss\'),\'%s\') '\
                             %('test',i,'test1','test2',time.strftime('%Y-%m-%d %H:%M:%S',t1),'http://test.com')
                    curs.execute(sql_str)
                    conn.commit()      
        except Exception,ex:
            print 'write_oracle 44 %s:%s'%(Exception,ex)
            lock_oracle.release()
            try:
                dsn=cx_Oracle.makedsn(oraclehost, oracleport, oracledatabase)
                conn=cx_Oracle.connect(oracleuser, oraclepassword, dsn)
                curs=conn.cursor()
            except Exception,ex:
                print 'write_oracle 55 %s:%s'%(Exception,ex)
        time.sleep(1)
    if curs and curs.connection:
        curs.close()
    if conn and conn.open:
        conn.close()
    thread.exit_thread()

def startService():
    thread.start_new_thread(write_oracle, ())
    while True:
        time.sleep(10)

if __name__=='__main__':
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
