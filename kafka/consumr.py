from kafka import KafkaConsumer
import json
import pandas as pd


consumer = KafkaConsumer(
    'testtest',

    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


# df=pd.read_csv("./Google-Playstore.csv")

# features=list(df.columns)

for message in consumer:
    print(f"Received: {message.value}")
    # if message.value['number'] == 4:
    #     break


# exit(0)