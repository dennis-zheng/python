# -*- coding: utf-8 -*-
import sys
import os
import requests
import urllib
import StringIO
import json
cookiesV = ''

headerV = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
headerV['Cookie'] = "Qs_lvt_9522=1551662717%2C1551756204%2C1552017788%2C1552121844%2C1552464732; Qs_pv_9522=3737430363283388000%2C1154052424793061000%2C3117785265590423000%2C3935994883197703000%2C1599256646303652000; localhost20140506=5brtk341jh5vcm591mrcjbpbs6; b45701b213834cd0b2d81c366da2d9af=WyIxMTI1Mjk4NzI3Il0; stored_company=78374; stored_iworker=%7B%22access_token%22%3A%22179b425f-8d57-4e61-98e8-4a894ad3375e%22%2C%22refresh_token%22%3A%227950c3d1-e11c-45c6-9c30-5996e4cbe140%22%2C%22expires_date%22%3A1559021933%2C%22rememberme%22%3A0%7D; login_from_6_1_1=1; iworker_email=dx.zheng%40tongguantech.com; login_fullname_iworker=%E9%83%91%E5%A4%A7%E6%98%9F"

def loadPicture(url, file):
    r = requests.get(url,headers = headerV)
    print(r.headers)
    #headerV['Cookie'] = r.headers['Set-Cookie']
    with open(file, 'wb') as f:
        f.write(r.content)
    if r.status_code != 200 or len(r.content) == 0:
        print('load error', url)
        return
    print('save to', file)

def loadPicturePost(url, file):
    print('headerV',headerV)
    r = requests.post(url, headers = headerV)
    print('r.content', len(r.content))
    with open(file, 'wb') as f:
        f.write(r.content)
    
    if r.status_code != 200 or len(r.content) == 0:
        print('load error', url)
        return
    print('save to', file)

def startService():
    #url = 'https://www.iworker.cn/'
    #url = 'https://www.iworker.cn/ajax/interval_request/cid:78374/uid:308372/r:496'
    url = 'https://www.iworker.cn/ajax/interval_request/cid:78374/uid:308371/r:496'
    #file = 'main.txt'
    file = 'r.json'
    loadPicture(url, file)
    return

    #url = 'http://172.10.0.4:8888/live'
    #url = 'https://longhua.iwowa.club/dict/getMacro.json'
    #url = 'https://longhua.iwowa.club/face/facePicture/getListWithPage.json?page=1&pageSize=20&sn=&provinceCode=440000&cityCode=440300&areaCode=440309&blockCode=4403090022&buildingCode=44030900220080&unitCode=4403090022008001&startTime=&endTime=&doorId=&checkFlag=&findNoFace=&positionType=&phone='
    #url = 'https://longhua.iwowa.club/face/facePicture/getListWithPage.json?page=2&pageSize=20&sn=DS-2CD2T2XYZUV-ABCDEF20181119AACHC70952117&provinceCode=440000&cityCode=440300&areaCode=440309&blockCode=4403090022&buildingCode=44030900220064&unitCode=4403090022006401&startTime=&endTime=&doorId=&checkFlag=&findNoFace=&positionType=&phone='
    url = 'https://longhua.iwowa.club/face/facePicture/getListWithPage.json?page=1&pageSize=20&sn=DS-2CD2T2XYZUV-ABCDEF20181119AACHC70952117&provinceCode=440000&cityCode=440300&areaCode=440309&blockCode=4403090022&buildingCode=44030900220064&unitCode=4403090022006401&startTime=2019-05-01+00%3A00%3A00&endTime=2019-05-02+00%3A00%3A00&doorId=&checkFlag=&findNoFace=&positionType=&phone='
    file = 'getListWithPage.json'
    loadPicturePost(url, file)

if __name__ == "__main__":
    os.system('title '+sys.path[0]+'\\'+sys.argv[0][sys.argv[0].rfind(os.sep)+1:])
    startService()
    
       
