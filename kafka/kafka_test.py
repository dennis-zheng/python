import os
from kafka import KafkaConsumer

def main():
    consumer = KafkaConsumer('dennis-topic',
                             group_id='my-group',
                             bootstrap_servers=['127.0.0.1:9092'])
    for message in consumer:
        # message value and key are raw bytes -- decode if necessary!
        # e.g., for unicode: `message.value.decode('utf-8')`
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                             message.offset, message.key,
                                             message.value))

if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")