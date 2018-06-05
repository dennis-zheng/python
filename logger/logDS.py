# -*- coding: utf-8 -*-

import time
import sys
import os
import logging
import inspect
import threading

lock = threading.Lock()
logger = 0
handler = 0
logName = 0

def isFileExit():
    this_file = inspect.getfile(inspect.currentframe())
    dirpath = os.path.abspath(os.path.dirname(this_file))
    log_name = '%s_%s.log'%(logName, time.strftime('%Y%m%d',time.localtime(time.time())))
    file_path = os.path.join(dirpath, 'log/', log_name)
    if os.path.exists(file_path) == False:
        return False
    return True
   

def init(name): 
    global logger
    global handler
    global logName
    try: 
        logName = name
        logger = logging.getLogger('[%s]'%logName)
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        log_name = '%s_%s.log'%(logName, time.strftime('%Y%m%d',time.localtime(time.time())))
        dirpath = os.path.join(dirpath, 'log/')
        if os.path.exists(dirpath) == False:
            os.makedirs(dirpath)  
        handler = logging.FileHandler(os.path.join(dirpath, log_name))
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)    
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    except Exception,ex:
        print 'log init error %s:%s'%(Exception,ex)

def reinit(): 
    global handler
    logger.removeHandler(handler)
    handler.close()
    this_file = inspect.getfile(inspect.currentframe())
    dirpath = os.path.abspath(os.path.dirname(this_file))
    log_name = '%s_%s.log'%(logName, time.strftime('%Y%m%d',time.localtime(time.time())))
    handler = logging.FileHandler(os.path.join(dirpath, 'log/', log_name))     
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
def log(level, log):
    if isFileExit() == False:
        reinit()
    lock.acquire()
    try: 
        logger.log(level,log)
    except Exception,ex:
        reinit()
        print 'log log %s:%s'%(Exception,ex)
    lock.release()

def info(log):
    if isFileExit() == False:
        reinit()
    lock.acquire()
    try: 
        logger.info(log)
    except Exception,ex:
        reinit()
        print 'log info %s:%s'%(Exception,ex)
    lock.release()

def warning(log):
    if isFileExit() == False:
        reinit()
    lock.acquire()
    try: 
        logger.warning(log)
    except Exception,ex:
        reinit()
        print 'log warning %s:%s'%(Exception,ex)
    lock.release()

def error(log):
    if isFileExit() == False:
        reinit()
    lock.acquire()
    try: 
        logger.error(log)
    except Exception,ex:
        reinit()
        print 'log error %s:%s'%(Exception,ex)
    lock.release()
    
if __name__ == "__main__":
    print '__main__ begin....'
    init('logDS')
    log(20, 'test log')
    log(30, 'test log')
    log(40, 'test log')
    info('test info')
    warning('test warning')
    error('test error')
    print '__main__ end....'
