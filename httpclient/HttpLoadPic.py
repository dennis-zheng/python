# -*- coding: UTF-8 -*-
import sys
import os
import time
import requests

def startService():
    try:
        pic_url = sys.argv[1]
        pic = requests.get(url=pic_url)
    except Exception,ex:
        print 'load: ',Exception,":",ex
    if pic.status_code == 200:
        name = pic_url[pic_url.rfind('/')+1:]
        with open(name, 'wb') as file:
            file.write(pic.content)

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()