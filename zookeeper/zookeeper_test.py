# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
from kazoo.client import KazooClient
import logging
logging.basicConfig()

if __name__ == "__main__":
    print("begin.")
    zk = KazooClient(hosts='172.10.3.111:2181')
    zk.start()
    mypath = "/my/favorite"
    #zk.ensure_path(mypath)
    if zk.exists(mypath):
        print(mypath, "exist")
        data, stat = zk.get(mypath)
        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
    else:
        print(mypath, "not exist")
    zk.stop()
    print("exit.")
