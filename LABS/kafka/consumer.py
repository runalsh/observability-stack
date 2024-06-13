import time
from kafka import KafkaConsumer
consumer = KafkaConsumer('topic', bootstrap_servers=['localhost:9091','localhost:9092','localhost:9093'])
for message in consumer:
    time.sleep(0.1) 
    print (message)