# -*- coding: utf-8 -*-
import sys
import os
import requests
import urllib
import StringIO
import json
import time

headerV = {}
jsonList = []
totolPage = 1
pageIndex = 1
nextJson = 0
errorFile = "http_error.txt"

def loadJsonPost(url, file):
    global headerV
    global totolPage
    global pageIndex
    global nextJson
    print('url', url)
    try:
        r = requests.post(url, headers = headerV)
        print('r.content', len(r.content))
        reJson = json.loads(r.content)
        #print(reJson)
        print('reJson', reJson['data']['total'],reJson['data']['page'])
        #sys.exit(1)
        totolPage = int(reJson['data']['total'])
        pageIndex = int(reJson['data']['page'])
        pageIndex += 1
        if pageIndex > totolPage:
            nextJson = 1
            pageIndex = 1
    except Exception,ex:
        nextJson = 1
        pageIndex = 1
        print 'error',Exception,ex
        with open(errorFile, 'ab') as f:
            f.write(url)
            f.write('\r\n')
        return

    with open(file, 'wb') as f:
        f.write(r.content)
    if r.status_code != 200 or len(r.content) == 0:
        print('load error', url)
        return
    print('save to', file)

def loadProcess():
    global pageIndex
    global nextJson
    for url in jsonList:
        while nextJson == 0:
            urlT = url + "&page=" + str(pageIndex)
            file = 'json/%s.json'%(str(int(time.time()*1000)))
            loadJsonPost(urlT, file)
        nextJson = 0

def init():
    global headerV
    with open('config/cookie.json', 'rb') as file:
        cookieJson = json.load(file)
        headerV['User-Agent'] = str(cookieJson['User-Agent'])
        headerV['Cookie'] = str(cookieJson['Cookie'])
    #print('headerV',headerV)

    global jsonList
    with open('config/getListWithPage.json', 'rb') as file:
        listJsonT = json.load(file)
        for urlT in listJsonT:
            jsonList.append(str(urlT['url']))
    print('jsonList',len(jsonList))
    
    pathT = 'json'
    if os.path.exists(pathT) == False:
        os.makedirs(pathT)
    pathT = 'picture'
    if os.path.exists(pathT) == False:
        os.makedirs(pathT)

    if os.path.exists(errorFile) == True:
        os.remove(errorFile)
    
def startService():
    init()
    loadProcess()

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
    
       
