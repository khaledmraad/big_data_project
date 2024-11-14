from kafka import KafkaConsumer
from json import loads
import time
import json

import kafka.hdfs_test as hdfs_test



    
consumer = KafkaConsumer(
    'testtest',

    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)





for message in consumer:
    message = message.value
    hdfs_test.write_to_hdfs(str(message))
    print(message)