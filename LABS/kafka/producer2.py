import datetime
import time
import uuid
from json import dumps

import schedule
from faker import Faker
from kafka import KafkaProducer

servers=['localhost:9091', 'localhost:9092', 'localhost:9093']
topic = 'topic'

producer = KafkaProducer(bootstrap_servers=servers)
producer = KafkaProducer()

def gendata():

    faker = Faker()

    data = {'id' : str(uuid.uuid4()), 'timestamp': str(datetime.datetime.now()), 'name': faker.name(), 
    'country': faker.country(), 'job': faker.job(), 'image': faker.image_url()}
    prod = KafkaProducer(bootstrap_servers=servers,value_serializer = lambda x:dumps(x).encode('utf-8'))
    print(data)
    prod.send(topic=topic, value=data)
    prod.flush()

if __name__ == "__main__":
    gendata()
    schedule.every(1).seconds.do(gendata)

    while True:
        schedule.run_pending()
        time.sleep(0.1)