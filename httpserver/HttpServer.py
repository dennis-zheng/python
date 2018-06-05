# -*- coding: utf-8 -*-
import web
import time
import glob
import sys
import os
import inspect
sys.path.append("method")

def FindMethodList(method_list):
    path = './method/*.py'
    for filepath in glob.glob(path):
        filename = filepath.split("\\")[-1]
        filename = filename.split(".")[0]
        #print filename
        method_list.append("/httpserver/" + filename)
        method_list.append(filename + "." + filename)

def startService():
    this_file = inspect.getfile(inspect.currentframe())
    dirpath = os.path.abspath(os.path.dirname(this_file))
    os.chdir(dirpath)
    
    method_list = []
    FindMethodList(method_list)
    
    method_tuple = tuple(method_list)
    app = web.application(tuple(method_list), globals())
    app.run()

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
