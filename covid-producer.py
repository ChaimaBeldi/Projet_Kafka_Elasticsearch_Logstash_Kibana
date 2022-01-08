import json
import time
import urllib.request
from kafka import KafkaProducer
import http.client

###### API_Key ####

API_KEY = "0aa543c94df64f70a7ada991bf2a74bb" # FIXME Set your own API key here
url = "https://api.covidactnow.org/v2/states.json?apiKey={}".format(API_KEY)
#create kafka producer

producer = KafkaProducer(bootstrap_servers="localhost:9092")
while True:
    response = urllib.request.urlopen(url)
    states = json.loads(response.read().decode())
    for state in states:
        #print(state)
        producer.send("corona-19", json.dumps(state).encode())
    print("{} Produced {} state records".format(time.time(), len(states)))
    time.sleep(1)
