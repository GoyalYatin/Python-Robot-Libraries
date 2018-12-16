from kafka import KafkaProducer
from kafka import KafkaConsumer
import logging
import config as cons


def insert_message_in_kafka(message, topic):
    """
    Produce messages to the given topic
    """
    p = KafkaProducer(bootstrap_servers=cons.bootstrap_servers)
    result = p.send(topic, message)
    p.flush()
    logging.info(result)
    return result


def consume_from_kafka(topic):
    """
    Consume messages from the given topic
    """
    c = KafkaConsumer(bootstrap_servers=cons.bootstrap_servers, auto_offset_reset=cons.auto_offset_reset,
                      consumer_timeout_ms=cons.consumer_timeout_ms)
    c.subscribe([topic])
    output = list()
    for message in c:
        output.append(message.value)
    c.close()
    logging.info("consumer closed")
    return output
