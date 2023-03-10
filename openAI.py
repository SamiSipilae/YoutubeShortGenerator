import openai
import urllib.request
import settings

openai.api_key = settings.OpenAiAPIKey
output = settings.outputPath

def getStory(genre, topic):
    prompt = f"Write a 2 sentence {genre} story about {topic}\n"
    print(f"Fetching story with prompt: {prompt}")
    story = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=50,
    temperature=0.9
    )

    storyText = story['choices'][0]['text'].replace('\n','')
    print(f"Story generated: {storyText}")
    return storyText


def getJoke(topic):
    prompt = f"Write a funny joke about {topic}\n"
    print(f"Fetching joke with prompt: {prompt}")
    joke = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=250,
    temperature=0.9
    )

    jokeText = joke['choices'][0]['text'].replace('\n','')
    print(f"Joke generated: {jokeText}")
    return jokeText


def getArt(subject):
    fileNameLong = "".join([c for c in f"{subject}" if c.isalpha() or c.isdigit() or c==' ']).rstrip()  
    fileName = fileNameLong[:32]+ ".png" #cap filename length
    print(f"Fetcing image {fileName}")
    response = openai.Image.create(
    prompt= subject,
    n=1,
    size="512x512"
    )
    imageUrl = response['data'][0]['url']
    urllib.request.urlretrieve(imageUrl, output+fileName)


    return output+fileName