# -*- coding: utf-8 -*-
import ctypes
import StringIO
import time
import requests
import struct
import threading

isLoad_ = 0
lockLoad_ = threading.RLock()

handle_ = 0

class StructBuf(ctypes.Structure):
    def __init__(self):
        pass
    _fields_ = [('buf',ctypes.c_char*255)]

class StructInfo(ctypes.Structure):
    def __init__(self):
        pass
    _fields_ = [('id',ctypes.c_int), ('idF',ctypes.c_float), ('buf',ctypes.c_char*255), ('size',ctypes.c_int)]

class PythonLoad(object):
    def __init__(self):
        global isLoad_
        global lockLoad_
        global handle_
        lockLoad_.acquire;
        if isLoad_ == 0 or handle_ == 0:
            handle_ = ctypes.cdll.LoadLibrary("./PythonLoadDll.dll")
        isLoad_ = isLoad_ + 1
        self.isLoad = isLoad_
        lockLoad_.release;
        ret = handle_.PythonLoadDll_init(self.isLoad)
        time.sleep(0.5)
        print 'finish PythonLoad', isLoad_, handle_

    def Process(self, index):
        global handle_
        info = StructInfo()
        #info.buf = StructBuf()
        buf = 'test buf'
        retList = []
        try:
            print 'handle_', handle_
            re = handle_.PythonLoadDll_process(self.isLoad, index, buf, len(buf), ctypes.pointer(info))
            print 'Process:',info.id, info.idF, info.buf, info.size
            retList.append(face_info)
        except Exception,ex:
            print 'Process %s:%s'%(Exception,ex)
        return retList
       
load = PythonLoad()
load.Process(1)