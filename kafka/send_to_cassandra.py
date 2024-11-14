from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
import os
import csv

# Setup Cassandra connection
auth_provider = PlainTextAuthProvider(username='admin', password='admin')
cluster = Cluster(['127.0.0.1'], port=9042, auth_provider=auth_provider)
session = cluster.connect()

# Create the keyspace and table if not exists
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS test_data 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")
session.set_keyspace('test_data')

session.execute("""
    CREATE TABLE  google_data (
        "App Name" varchar ,
        "App Id" varchar PRIMARY KEY,
        "Category" varchar,
        "Rating" varchar,
        "Rating Count" varchar,
        "Installs" varchar,
        "Minimum Installs" varchar,
        "Maximum Installs" varchar,
        "Free" varchar,
        "Price" varchar,
        "Currency" varchar,
        "Size" varchar,
        "Minimum Android" varchar,
        "Developer Id" varchar,
        "Released" varchar,
        "Last Updated" varchar,
        "Content Rating" varchar,
        "Ad Supported" varchar,
        "In App Purchases" varchar,
        "Editors Choice" varchar


    )
""")



# Function to insert data into Cassandra
def insert_into_cassandra(session, row):
    insert_query = """
    INSERT INTO google_data ("App Name", "App Id", Category, Rating, "Rating Count", Installs, 
                             "Minimum Installs", "Maximum Installs", Free, Price, Currency, Size, 
                             "Minimum Android", "Developer Id", Released, "Last Updated", "Content Rating", 
                             "Ad Supported", "In App Purchases", "Editors Choice")
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """


# COPY keypsace.tableName ("App Name", "App Id", Category, Rating, "Rating Count", Installs,  "Minimum Installs", "Maximum Installs", Free, Price, Currency, Size, "Minimum Android", "Developer Id", Released, "Last Updated", "Content Rating", "Ad Supported", "In App Purchases", "Editors Choice") FROM 'part-00005-458a8eae-3796-4d7f-8471-ed368b48de64-c000.csv' WITH DELIMITER=',' AND HEADER=TRUE;

    print("inserting")
    # print(row)
    # Insert the data
    session.execute(insert_query, (
    str(row["App Name"]), str(row["App Id"]), str(row["Category"]), str(row["Rating"]), str(row["Rating Count"]),
    str(row["Installs"]), str(row["Minimum Installs"]), str(row["Maximum Installs"]), str(row["Free"]),
    str(row["Price"]), str(row["Currency"]), str(row["Size"]), str(row["Minimum Android"]), str(row["Developer Id"]),
    str(row["Released"]), str(row["Last Updated"]), str(row["Content Rating"]), str(row["Ad Supported"]),
    str(row["In App Purchases"]), str(row["Editors Choice"])
))

csv_path = "./csv_result/"
files = [f for f in os.listdir(csv_path) if os.path.isfile(os.path.join(csv_path, f))]

for sub_csv in files:
    df = pd.read_csv(os.path.join(csv_path, sub_csv), on_bad_lines="skip")
    
    for i, row in df.iterrows():
        insert_into_cassandra(session, row)
        print(i)
        if i == 5:
            break

rows = session.execute('SELECT * FROM google_data')
for row in rows:
    print(row)

cluster.shutdown()
