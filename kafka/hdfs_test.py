import pyhdfs
import uuid
from kafka import KafkaConsumer
import json
import csv


hdfs = pyhdfs.HdfsClient(hosts="localhost:50070" , user_name="root")

userhomedir = hdfs.get_home_directory()
print(userhomedir)
availablenode = hdfs.get_active_namenode()
print(availablenode)
print(hdfs.listdir("/"))

hdfs.mkdirs('/test')
print(hdfs.list_status('/test'))


if not hdfs.exists("/test/work.csv"):
    hdfs.create("/test/work.csv",data=b'')


# hdfs.append('/test/ok.csv', overwrite=False, data=b'\ntest\n')

# def write_to_hdfs(data):

#     file_path = '/data/test.csv'
    
#     if hdfs.exists(file_path):
#         with hdfs.open(file_path, 'a') as f:
#             writer = csv.DictWriter(f, fieldnames=data.keys())
#             writer.writerow(data)
#     else:
#         with hdfs.create(file_path, 'w') as f:
#             writer = csv.DictWriter(f, fieldnames=data.keys())
#             writer.writeheader()
#             writer.writerow(data)


# wtf received: {'number': 4, 'message': {'App Name': 'GROW.me', 'App Id': 'com.horodyski.grower', 'Category': 'Tools', 'Rating': 0.0, 'Rating Count': 0.0, 'Installs': '100+', 'Minimum Installs': 100.0, 'Maximum Installs': 478, 'Free': True, 'Price': 0.0, 'Currency': 'USD', 'Size': '6.2M', 'Minimum Android': '4.1 and up', 'Developer Id': 'Rafal Milek-Horodyski', 'Developer Website': 'http://www.horodyski.com.pl', 'Developer Email': 'rmilekhorodyski@gmail.com', 'Released': 'Feb 21, 2020', 'Last Updated': 'Nov 12, 2018', 'Content Rating': 'Everyone', 'Privacy Policy': 'http://www.horodyski.com.pl', 'Ad Supported': False, 'In App Purchases': False, 'Editors Choice': False, 'Scraped Time': '2021-06-15 20:19:35'}}
consumer = KafkaConsumer(
    'testtest',

    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

data_fkn_block=""
for message in consumer:
    print(f"Received: {message.value}")
    data=message.value.get('message')
    data_fkn_block+=str(data)

    if message.value['number'] % 30000 == 0:
        # hdfs.append('/test/work.csv', overwrite=False, data=b''+str(data_fkn_block).encode('utf-8'))
        data_fkn_block=""

hdfs.append('/test/work.csv', overwrite=False, data=b''+str(data_fkn_block).encode('utf-8'))

    
    # hdfs.append('/test/work.csv', overwrite=False, data=b''+str(data).encode('utf-8'))
    



