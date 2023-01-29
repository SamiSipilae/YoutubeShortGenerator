import openAI
import settings
import googleTTS
import create_video
import image
import json
import os
import youtube


def cleanUp():
    files = os.glob(settings.outputPath + '.mp4')
    for file in files:
        os.remove(file)
    files = os.glob(settings.outputPath + '.png')
    for file in files:
        os.remove(file)   

genre = settings.getGenre()
topic = settings.getTopic()
voice = googleTTS.getRandomVoice()



storyText = openAI.getStory(genre,topic)


sentences = list(filter(None, storyText.strip().split('.')))
if len(sentences) < 2:
    sentences = list(filter(None, storyText.strip().split(',')))


story = []
for sentence in sentences:
    print(f"Fetching art for sentence {sentence}")
    art = openAI.getArt(sentence)
    resizedArt = image.resizeImage(art)
    audio = googleTTS.TTS(sentence, voice)
    storySegment = {
        'text': sentence,
        'art':  art,
        'resizedArt' :resizedArt,
        'audio': audio
    }
    story.append(storySegment)


video = create_video.generateVideo(story)

title= f"Ai generated 2 story horror: {topic}",
description=  storyText + f"\n\n a 2 sentence {genre} story about: {topic}\n This story is automatically AI generated using openAI and other similar tools.",
tags=["AI", "artificialintelligence", "horror", "short", "2sentencehorror","openai", "aigenerated","story"]

youtube.upload(video, description,tags,title)
