import openAI
import settings
import googleTTS
import create_video
import image
import json
import os
import youtube


def generate():
    genre = settings.getGenre()
    topic = settings.getTopic()
    voice = googleTTS.getRandomVoice()


    story = []
    storyText = openAI.getJoke(topic)


    print(f"Fetching art for story {storyText}")
    art = openAI.getArt(storyText)
    resizedArt = image.resizeImage(art)
    audio = googleTTS.TTS(storyText, voice)
    storySegment = {
        'text': storyText,
        'art':  art,
        'resizedArt' :resizedArt,
        'audio': audio
    }
    story.append(storySegment)


    video = create_video.generateVideo(story)

    title= f"Ai generated 2 joke: {topic}",
    description=  storyText + f"\n\n a 2 sentence joke about: {topic}\n This story is automatically AI generated using openAI and other similar tools.",
    tags=["AI", "artificialintelligence", "joke", "short", f"humor","funny","openai", "aigenerated","story"]

    youtube.upload(video, description,tags,title)
