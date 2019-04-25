# -*- coding: utf-8 -*-
import sys
import os
import re
import requests
import time
from concurrent.futures import ThreadPoolExecutor
pool=ThreadPoolExecutor(8) #创建1个程池中，容纳线程个数为30个；

rootpath = 'G:\\dennis\\python_test\\http_load_pic\\baidu_pic\\'

flagNum = False
listNum = 1

def getPage(url):
    return requests.get(url, timeout=10).text

def loadPic(urls):
    #print(len(urls))
    for i in range(len(urls)):
        url = urls[i]
        name = rootpath + url[url.rfind("/"):]
        respose=requests.get(url)
        with open(name,'wb') as f:
            f.write(respose.content)

def parseResponse(respose):
    global listNum
    global flagNum
    urls=re.findall(r'\"thumbURL\".*?"(.*?)"',respose.result(),re.S)
    listNumT=re.findall(r'\"listNum\".*?:(.*?),',respose.result(),re.S)
    listNum = int(listNumT[0])
    if flagNum == False:
        flagNum = True
        print("set flagNum True")
    pool.submit(loadPic(urls))
    print(len(urls),listNum)

def startService():
    index = 0
    while index < listNum:
        url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%AE%B8%E5%B7%8D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E8%AE%B8%E5%B7%8D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force='
        url = ("%s&pn=%d&rn=30&gsm=%0x&%ld=")%(url, index, index, int(time.time()*1000))
        #print(url)
        pool.submit(getPage,url).add_done_callback(parseResponse)
        print(index)
        while flagNum == False:
            time.sleep(1)
        #respose=getPage(url)
        #urls,listNum = parseResponse(respose)
        #print(index, len(urls), listNum)
        #loadPic(urls)
        #pool.submit(loadPic(urls))
        index += 30
    while 0:
        time.sleep(1000)
    print("exit main.")

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
