# -*- coding: utf-8 -*-
import sys
import os
import StringIO
import time
import requests
import struct
import urllib
import struct
import StringIO
import json

def normal():
    listT  = []
    for i in range(10):
        if i%2 == 0:
            listT.append(i)
    print(listT)
    for i in range(10):
        if i%2 == 1:
            listT.append(i)
    print(listT)
    listT.sort(cmp=None, key=None, reverse=False)
    print(listT)

def with_multi():
    listT  = []
    for i in range(10):
        if i%2 == 0:
            listT.append(("AA%02d"%i, i))
    print(listT)
    print('******************************************************')
    for i in range(10):
        if i%2 == 1:
            listT.append(("BB%02d"%i, i))
    print(listT)
    print('******************************************************')
    #listT.sort(cmp=cmpDict)
    listT.sort(cmp=lambda x,y: cmp(x[1],y[1]),reverse=True)
    print(listT)

def with_dict():
    listT  = []
    for i in range(10):
        if i%2 == 0:
            dictT = {}
            dictT["string"]="AA%02d"%i
            dictT["num"]=i
            listT.append(dictT)
    print(listT)

    print('******************************************************')
    for i in range(10):
        if i%2 == 1:
            dictT = {}
            dictT["string"]="BB%02d"%i
            dictT["num"]=i
            listT.append(dictT)
    print(listT)

    print('string ******************************************************')
    #listT.sort(cmp=cmpDict)
    listT.sort(cmp=lambda x,y: cmp(x['string'], y['string']),reverse=True)
    print(listT)

    print('num ******************************************************')
    #listT.sort(cmp=cmpDict)
    listT.sort(cmp=lambda x,y: cmp(x['num'], y['num']),reverse=True)
    print(listT)
    
    print('json ******************************************************')
    print(json.dumps(listT))

def startService():
    #normal()
    #with_multi()
    with_dict()

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
       