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
    node = "%s/node2"%(mypath)
    node = "/electionpath"
    #zk.ensure_path(node)
    if zk.exists(node):
        print(node, "exist")
        zk.delete(node, recursive=True)
    else:
        print(node, "not exist")
    zk.stop()
    print("exit.")
