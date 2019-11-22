# -*- coding: utf-8 -*-
import sys
import os
import time
import re
import requests

rootpath = 'G:\\dennis\\python_test\\http_load_pic\\baidu_pic\\'

def startService():
    url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%AE%B8%E5%B7%8D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&word=%E8%AE%B8%E5%B7%8D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn=0&rn=60&gsm=f0'
    url = ("%s&%ld=")%(url, long(time.time()*1000))
    respose=requests.get(url)
    with open(rootpath+'respose.content','wb') as f:
        f.write(respose.content)
    
    urls=re.findall(r'\"thumbURL\".*?"(.*?)"',respose.content,re.S)
    #urls = list(set(urls))
    #urls.sort()
    print(len(urls))
    with open(rootpath+'urls3.txt','wb') as f:
        for i in range(len(urls)):
            f.write(urls[i])
            f.write('\r\n')
    
    for i in range(len(urls)):
        url = urls[i]
        name = rootpath + url[url.rfind("/"):]
        respose=requests.get(url)
        with open(name,'wb') as f:
            f.write(respose.content)

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
