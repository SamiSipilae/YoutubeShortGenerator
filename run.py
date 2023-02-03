import joke
import os
import glob
import a2_sentence_story
import random
import settings
import time
import logging

def cleanUp():
    fileTypes = ['*.mp4','*.png', '*.mp3']
    if settings.cleanUp:
        print("Cleaning up files.")
        filesToDelete = []
        for files in fileTypes:
            filesToDelete.extend(glob.glob(settings.outputPath +files))

        for file in filesToDelete:
            os.remove(file)   
        



while True:

    try:
        type = random.choice(['joke', '2sentenceStory'])

        if type == 'joke':
            joke.generate()
        elif type == '2sentenceStory':
            a2_sentence_story.generate()

        cleanUp()
        
    except Exception:
        logging.exception("Error:")
    time.sleep(60*30)