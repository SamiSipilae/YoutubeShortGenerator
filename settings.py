import keyring
import random
import os

cleanUp = True

OpenAiAPIKey = keyring.get_password("openai", "apikey")


youtubeClientID = keyring.get_password("youtube", "client")
youtubeClientSecret = keyring.get_password("youtube", "secret")


googleApiJSONPath = f"google.json"
outputPath = "output/"
genre = 'horror' 

text_file = open("wordlist.10000.txt", "r")
topics = text_file.read().split('\n')
text_file.close()

def getGenre():
    return genre

def getTopic():
    return  random.choice(topics)