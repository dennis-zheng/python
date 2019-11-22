# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
from kazoo.client import KazooClient
from kazoo.client import KazooState
import logging
logging.basicConfig()

if __name__ == "__main__":
    print("begin.")

    zk = KazooClient(hosts='172.10.3.111:2181')
    @zk.add_listener
    def my_listener(state):
        if state == KazooState.LOST:
            print("LOST")
        elif state == KazooState.SUSPENDED:
            print("SUSPENDED")
        else:
            print("Connected")
    print("start 00.")
    zk.start()
    print("start 11.")

    mypath = "/my/favorite"
    node = "%s/node" % (mypath)

    @zk.ChildrenWatch(mypath)
    def watch_children(children):
        print("Children are now: %s" % children)

    @zk.DataWatch(mypath)
    def watch_node(data, stat):
        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    while True:
        time.sleep(10)
    print("exit.")
