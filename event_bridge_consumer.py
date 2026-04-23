from kafka import KafkaConsumer, KafkaProducer
from const import *


class EventBridgeConsumer:
    def __init__(self, input_topic, output_topic):
        self.input_topic = input_topic
        self.output_topic = output_topic
        bootstrap_server = BROKER_ADDR + ':' + BROKER_PORT

        # Option 1: only consume new events.
        self.consumer = KafkaConsumer(bootstrap_servers=[bootstrap_server])

        # Option 2: consume old events (uncomment to test).
        # self.consumer = KafkaConsumer(
        #     bootstrap_servers=[bootstrap_server],
        #     auto_offset_reset='earliest'
        # )

        self.producer = KafkaProducer(bootstrap_servers=[bootstrap_server])
        self.consumer.subscribe([self.input_topic])

    def process_event(self, event_value):
        decoded_msg = event_value.decode('utf-8')
        return f'Processed event: {decoded_msg}'

    def run(self):
        for msg in self.consumer:
            processed_msg = self.process_event(msg.value)
            print('Consumed from ' + self.input_topic + ': ' + msg.value.decode('utf-8'))
            print('Publishing to ' + self.output_topic + ': ' + processed_msg)
            self.producer.send(self.output_topic, value=processed_msg.encode('utf-8'))
            self.producer.flush()
