import os
import logging
from kafka import KafkaProducer
from kafka.errors import KafkaError

def main():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'])
    future = producer.send('dennis-topic', b'raw_bytes')
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        logging.exception()
        pass
    logging.info("topic=%s, partition=%d, offset=%d" % (record_metadata.topic, record_metadata.partition, record_metadata.offset))

if __name__ == "__main__":
    print("main enter.")
    main()
    print("main exit.")