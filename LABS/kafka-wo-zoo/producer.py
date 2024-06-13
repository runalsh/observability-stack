from kafka import KafkaProducer
from datetime import datetime
import time

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'my-topic'

# Initialize the Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
producer = KafkaProducer()

while True:
    # Create the message
    message = 'Hello World! ' + str(datetime.now().time())
    # Send the message, encoding it to bytes
    producer.send(topicName, value=message.encode('utf-8'))
    # Ensure all buffered records are sent
    producer.flush()
    # Optional: add a sleep to prevent sending messages too quickly
    # time.sleep(0.01)