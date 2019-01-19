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

class StructInfo(ctypes.Structure):
    _fields_ = [
        ('id',ctypes.c_int), 
        ('idF',ctypes.c_float)
    ]

class StructBuf(ctypes.Structure):
    _fields_ = [
        ('buf',ctypes.c_char*256),
         ('size',ctypes.c_int)
    ]

class StructMultiBuf(ctypes.Structure):
    _fields_ = [
        ('buf',ctypes.c_char_p*100),
        ('size', ctypes.c_int*100), 
        ('count', ctypes.c_int)
    ]

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
        buf = 'test buf'
        try:
            #print 'handle_', handle_
            print (buf, len(buf))
            re = handle_.PythonLoadDll_process(self.isLoad, index, buf, len(buf))
            print ('Process:',re)
        except Exception,ex:
            print 'Process %s:%s'%(Exception,ex)
       
    def ProcessInfo(self, index):
        global handle_
        info = StructInfo()
        info.id = 11
        info.idF = 11.22
        try:
            print(info)
            re = handle_.PythonLoadDll_processInfo(self.isLoad, index, ctypes.pointer(info))
            print ('ProcessInfo:',re)
        except Exception,ex:
            print 'ProcessInfo %s:%s'%(Exception,ex)

    def ProcessBuf(self, index):
        global handle_
        info = StructBuf()
        info.buf = 'test buf'
        info.size = len(info.buf)
        try:
            print(info)
            re = handle_.PythonLoadDll_processBuf(self.isLoad, index, ctypes.pointer(info))
            print ('ProcessBuf:',re)
        except Exception,ex:
            print 'ProcessBuf %s:%s'%(Exception,ex)

    def ProcessMultiBuf(self, index):
        global handle_
        info = StructMultiBuf()
        info.count = 4
        for i in range(info.count):
            info.buf[i] = 'test buf %d'%(i)
            #info.buf[i] = ctypes.c_char_p('test buf %d'%(i)) #the same
            info.size[i] = len(info.buf[i])
        try:
            print(info)
            re = handle_.PythonLoadDll_processMultiBuf(self.isLoad, index, ctypes.pointer(info))
            print ('ProcessBufMulti:',re)
        except Exception,ex:
            print 'ProcessBufMulti %s:%s'%(Exception,ex)

    def ProcessOut(self, index):
        global handle_
        buf = ctypes.create_string_buffer(256)
        #buf = (ctypes.c_char*256)()
        size = (ctypes.c_int)()
        try:
            re = handle_.PythonLoadDll_processOut(self.isLoad, index, ctypes.pointer(buf), ctypes.pointer(size))
            print ('Process:',re)
            print(buf.value, size.value)
        except Exception,ex:
            print 'Process %s:%s'%(Exception,ex)

    def ProcessBufOut(self, index):
        global handle_
        info = StructBuf()
        try:
            print(info)
            re = handle_.PythonLoadDll_processBufOut(self.isLoad, index, ctypes.pointer(info))
            print ('ProcessBufOut:',re)
            print(info)
            print(info.buf, info.size)
        except Exception,ex:
            print 'ProcessBufOut %s:%s'%(Exception,ex)

    def ProcessMultiBufOut(self, index):
        global handle_
        info = StructMultiBuf()
        for i in range(100):
            info.buf[i] = '%s'%(ctypes.create_string_buffer(256))#ctypes.create_string_buffer(256*(i+1)).value#StructBuf().buf
            #print(info.buf[i])
        try:
            print(info)
            re = handle_.PythonLoadDll_processMultiBufOut(self.isLoad, index, ctypes.pointer(info))
            print ('ProcessMultiBufOut:',re)
            print(info)
            print(info.count)
            for i in range(info.count):
                print(info.buf[i], info.size[i])
        except Exception,ex:
            print 'ProcessMultiBufOut %s:%s'%(Exception,ex)

    def ProcessRe(self, index):
        global handle_
        handle_.PythonLoadDll_processRe.restype = ctypes.c_float
        try:
            re = handle_.PythonLoadDll_processRe(self.isLoad, index)
            print ('ProcessRe:',re)
        except Exception,ex:
            print 'ProcessRe %s:%s'%(Exception,ex)

load = PythonLoad()
load.Process(1)
print("========================================================================")
load.ProcessInfo(2)
print("========================================================================")
load.ProcessBuf(3)
print("========================================================================")
load.ProcessMultiBuf(4)
print("========================================================================")
load.ProcessOut(44)
print("========================================================================")
load.ProcessBufOut(5)
print("========================================================================")
load.ProcessMultiBufOut(6)
print("========================================================================")
load.ProcessRe(7)
print("========================================================================")