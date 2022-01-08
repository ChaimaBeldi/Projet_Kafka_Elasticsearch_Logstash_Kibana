import json
import time
import urllib.request
from kafka import KafkaProducer
import http.client

conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "69f49cf31fmshe575bfd771cbc5bp132c3bjsne3a3c4895a6b"
    }
conn.request("GET", "/statistics", headers=headers)
res = conn.getresponse()
#create kafka producer
producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    stat = res.read().decode()
    print(stat)
    producer.send("covid-19", stat.encode())
    print("{} Produced {} stat records".format(time.time(), len(stat)))		
    time.sleep(2)	
