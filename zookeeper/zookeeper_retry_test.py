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
    result = zk.retry(zk.get, mypath)
    print("result",result)
    zk.stop()
    print("exit.")
