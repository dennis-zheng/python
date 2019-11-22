# -*- coding: utf-8 -*-
import time
import glob
import sys
import os
import threading
import uuid
import pika
#import logging
#logging.basicConfig()

import logDS

logDS.init('amqp')
is_stop = False
gindex = 0


def thread_process2(index):
    logDS.info("begin %d"%index)
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('172.10.3.111',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    #connection = pika.SelectConnection(pika.ConnectionParameters(host='172.10.3.111'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
    print(" [x] Sent 'Hello World!'")
    connection.close()
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
