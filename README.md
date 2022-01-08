# Projet_Kafka_Elasticsearch_Logstash_Kibana

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)

_Une solution pour suivre les statistques de covid-19 dans US._
#
![This is an image ](/images/crée-par.svg)
- Chaima Beldi
- Mariem Mnasser 
##
 Les nouvelles vagues de la pandémie de COVID-19 font toujours rage dans le monde, provoquant des perturbations sanitaires et économiques majeures.
 Il devient évident alors qu’un suivi précis des données émergentes est toujours crucial pour les gouvernements et les décideurs.
 ## Pour commencer

- _Architecture_ : Notre pipeline commence par la récupération de la clé de l'API COVID-19 du site "covidactnow", L'API Covid Act Now donne accès à toutes nos données COVID qui suivent les États, les comtés et les métros américains.
Il comprend des données et des mesures pour les cas , les vaccinations , les tests , les hospitalisations et les décès . Voir les définitions de données pour toutes les données incluses.
Puis, on a crée le script covid-producer.py qui contient un producer Kafka où on va stocker les données renvoyés par l'appel à l'API.
On a également développé un consumer Kafka (covid-consumer.py) pour le topic 'corona-19'. A prés, On lance les deux scripts pour la récupération des donnés.
Passant à l'étape d'indexation pour visualiser ces données sur le dashboard du kibana en temps réel.
Pour la réalisation de cette étape, on a ajouté le 'fichier pipeline.conf' dans le dossier de configurtion du logstash qui prend comme paramètre :
    - Input: qui est notre serveur kafka lancé sur localhost:9092 où on spécifie aussi le topic qui va envoyé les données.
    - Output: qui est elasticsearch lancé sur localhost:9200.
Finalement, on visualise sur le dashboard de Kibana les données envoyés en temps réel.
#
![This is an image ](/images/cap5.JPG)
#
## Technologies
On a utilsé ces technologies

- Kafka
- Elasticsearch
- Logstash
- Kibana
 ## Démo:
 - Voir la vidéo "Démo.mp4"0
