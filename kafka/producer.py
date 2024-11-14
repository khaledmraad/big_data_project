from kafka import KafkaProducer
import json
import pandas as pd


producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# df=pd.read_csv("./Google-Playstore.csv")


with open('./Google-Playstore.csv', 'r') as file:
    for i, line in enumerate(file):
        message = {'number': i, 'message': line}
        producer.send('testtest', value=message)



# features=list(df.columns)

# print(features)

# line_nbre=df.shape[0]

# test=df.iloc[:5]

# for i in range(5):
#     message = {'number': i, 'message': test.iloc[i].to_dict()}
#     producer.send('testtest', value=message)
    

producer.flush()
producer.close()

