import sys
from event_bridge_consumer import EventBridgeConsumer


try:
    input_topic = sys.argv[1]
    output_topic = sys.argv[2]
except:
    print('Usage: python3 consumer_bridge.py <input_topic_name> <output_topic_name>')
    exit(1)

bridge_consumer = EventBridgeConsumer(input_topic, output_topic)
bridge_consumer.run()
