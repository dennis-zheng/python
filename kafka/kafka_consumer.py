import os
import sys
import getopt
import logging
from kafka import KafkaConsumer

topic = 'dennis-topic'
group_id = 'dennis-group'

def usage():
    logging.info("usage:.")
    pass

def getopt_init():
    global topic
    global group_id
    try:
        opts, args = getopt.getopt(sys.argv[1:], 't:g:h', ['topic=', 'group_id=', 'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-t', '--topic'):
            topic = arg
        elif opt in ('-g', '--group_id'):
            group_id = arg
        else:
            usage()
            sys.exit(2)
    logging.info("topic=%s, group-id=%s" % (topic, group_id))

def consumer_process():
    consumer = KafkaConsumer(topic,
                             group_id=group_id,
                             bootstrap_servers=['127.0.0.1:9092'])
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        logging.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                    message.offset, message.key,
                                                    message.value))

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    getopt_init()
    consumer_process()


if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")