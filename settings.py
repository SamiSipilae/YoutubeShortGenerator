import keyring
import random

OpenAiAPIKey = keyring.get_password("openai", "apikey")

genre = 'horror'

text_file = open("wordlist.10000.txt", "r")
topics = text_file.read().split('\n')
text_file.close()

def getGenre():
    return genre

def getTopic():
    return  random.choice(topics)