from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    event = {"event": "test_event", "timestamp": time.time()}
    producer.send("test_topic", event)
    print(f"Produced: {event}")
    time.sleep(1)
