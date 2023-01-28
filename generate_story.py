import openAI
import settings


genre = settings.getGenre()
topic = settings.getTopic()
story = openAI.getStory(genre,topic)

if '.' in story:
    sentences = story.strip().split('.')
else:
    sentences = story.strip().split(',')
print(sentences)
for sentence in sentences:
    print(f"Fetching art for sentence {sentence}")
    openAI.getArt(sentence)



