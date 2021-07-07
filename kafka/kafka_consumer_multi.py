import os
import logging
from kafka import KafkaConsumer
import threading
import time

topic = 'dennis-topic'
group_id = 'dennis-group'
bootstrap_servers = ['127.0.0.1:9092']


def thread_process(index, index2):
    logging.info("enter thread %d:%d" % (index, index2))
    group_id_tmp = "%s_%d" % (group_id, index)
    consumer = KafkaConsumer(topic,
                             group_id=group_id_tmp,
                             bootstrap_servers=bootstrap_servers)
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        logging.info("%s:%d:%d:%s:%d key=%s value=%s" % (message.topic, message.partition,
                                            message.offset, group_id_tmp, index2,
                                            message.key, message.value))
    logging.info("exit thread %d:%d" % (index, index2))


def is_any_thread_alive(threads):
    return True in [t.is_alive() for t in threads]

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("main enter.")
    thread_list = []
    for index in range(2):
        for index2 in range(1):
            t = threading.Thread(target=thread_process, args=(index, index2), daemon=True) #
            t.start()
            thread_list.append(t)

    while is_any_thread_alive(thread_list):
        time.sleep(0)
    #for t in thread_list:
    #    t.join()

    logging.info("main exit.")

if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")