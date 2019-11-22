# -*- coding: utf-8 -*-
import sys
import os
import re
import requests
import time

rootpath = 'G:\\dennis\\python_test\\http_load_pic\\baidu_pic\\'

def getPage(url):
    return requests.get(url, timeout=10)

def loadPic(urls):
    for i in range(len(urls)):
        url = urls[i]
        name = rootpath + url[url.rfind("/"):]
        respose=requests.get(url)
        with open(name,'wb') as f:
            f.write(respose.content)

def parseResponse(respose):
    urls=re.findall(r'\"thumbURL\".*?"(.*?)"',respose.content,re.S)
    listNum=re.findall(r'\"listNum\".*?:(.*?),',respose.content,re.S)
    return urls,int(listNum[0])

def startService():
    listNum = 1
    index = 0
    while index < listNum:
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%AE%B8%E5%B7%8D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E8%AE%B8%E5%B7%8D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force='
        url = ("%s&pn=%d&rn=30&gsm=%0x&%ld=")%(url, index, index, long(time.time()*1000))
        #print(url)
        respose=getPage(url)
        urls,listNum = parseResponse(respose)
        print(index, len(urls), listNum)
        loadPic(urls)
        index += 30

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
