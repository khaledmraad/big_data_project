from kafka import KafkaAdminClient


admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
admin_client.delete_topics(topics=['testtest'])