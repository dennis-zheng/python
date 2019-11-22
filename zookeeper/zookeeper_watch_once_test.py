# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
from kazoo.client import KazooClient
import logging
logging.basicConfig()

def my_func(event):
    # check to see what the children are now
    print("event", event)

if __name__ == "__main__":
    print("begin.")
    zk = KazooClient(hosts='172.10.3.111:2181')
    zk.start()
    mypath = "/my"
    #zk.ensure_path(mypath)
    if zk.exists(mypath):
        print(mypath, "exist")
        data, stat = zk.get(mypath)
        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
        children = zk.get_children("%s/favorite"%(mypath), watch=my_func)
        print("children",children)
    else:
        print(mypath, "not exist")
    while True:
        time.sleep(10)
    zk.stop()
    print("exit.")
