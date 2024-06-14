import time
from kafka import KafkaConsumer
import psycopg2
consumer = KafkaConsumer('topic', bootstrap_servers=['localhost:9091','localhost:9092','localhost:9093'])
conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='db',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()
for message in consumer:
    time.sleep(0.1) 
    print (message)
    # cur.execute(
    #     """
    #     INSERT INTO people(transaction_id, user_id, timestamp, amount, currency, city, country, merchant_name, payment_method, 
    #     ip_address, affiliateId, voucher_code)
    #     VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #     """, (transaction["transactionId"], transaction["userId"], datetime.fromtimestamp(transaction["timestamp"]).strftime('%Y-%m-%d %H:%M:%S'),
    #           transaction["amount"], transaction["currency"], transaction["city"], transaction["country"],
    #           transaction["merchantName"], transaction["paymentMethod"], transaction["ipAddress"],
    #           transaction["affiliateId"], transaction["voucherCode"])
    # )
    # conn.commit()
# cur.close()
# conn.close()