import json
from kafka import KafkaConsumer

###
from elasticsearch import Elasticsearch
es = Elasticsearch()
####
from datetime import datetime


consumer = KafkaConsumer("corona-19", bootstrap_servers='localhost:9092')

for message in consumer:
    print(message)
    #stat = message.value.decode() 
    country= stat["country"]  
    lastUpdatedDate= stat["lastUpdatedDate"]
    
    population= stat["population"]
    metrics= stat["metrics"]
    actuals= stat["actuals"]
    cases = actuals["cases"]
    deaths = actuals["deaths"]
    positiveTests = actuals["positiveTests"]
    negativeTests = actuals["negativeTests"]
    hospitalBeds = actuals["hospitalBeds"] 
    newCases= actuals["newCases"]
    newDeaths = actuals["newDeaths"]
    vaccinesDistributed= actuals["vaccinesDistributed"]
    vaccinesInitiated= actuals["vaccinationsCompleted"]
    vaccinesCompleted= actuals["vaccinationsCompleted"]
  
