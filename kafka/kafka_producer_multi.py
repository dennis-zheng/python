import os
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError
import threading

topic = 'dennis-topic'
group_id = 'dennis-group'
bootstrap_servers = ['127.0.0.1:9092']

def thread_process(index, loop):
    logging.info("enter thread %d" % (index))

    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    for i in range(loop):
        text = "raw_bytes_%d_%d" % (index, i)
        future = producer.send(topic, text.encode('utf-8'))
        #future = producer.send(topic, key=b'foo', value=text.encode('utf-8'))
        try:
            record_metadata = future.get(timeout=10)
            logging.info("topic=%s, partition=%d, offset=%d" % (record_metadata.topic, record_metadata.partition, record_metadata.offset))
        except KafkaError:
            # Decide what to do if produce request failed...
            logging.exception()
            pass

    logging.info("exit thread %d" % (index))


def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("main enter.")
    thread_list = []
    for index in range(2):
        t = threading.Thread(target=thread_process, args=(index, 10))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    logging.info("main exit.")

if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")