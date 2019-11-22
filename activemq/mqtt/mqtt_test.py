# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid
import paho.mqtt.client as mqtt
#import logging
#logging.basicConfig()

import logDS

logDS.init('mqtt')
is_stop = False
gindex = 0

def on_connect(client, userdata, flags, rc):
    logDS.info("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    logDS.info(msg.topic+" "+str(msg.payload))

def thread_process2(index):
    logDS.info("begin %d"%index)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("172.10.3.111", 1883, 60)
    client.loop_forever()
    logDS.info("exit %d"%index)

class thread_process(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
    def run(self):
        thread_process2(self.index)

def startService():
    thread_list = []
    for i in range(1):
        thread = thread_process(i)
        thread.start()
        thread_list.append(thread)

    for t in thread_list:
        t.join()

if __name__ == "__main__":
    print("begin.")
    startService()
    print("exit.")
