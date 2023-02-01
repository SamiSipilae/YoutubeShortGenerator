
from google.cloud import texttospeech
from google.oauth2 import service_account
import settings
import random

output = settings.outputPath

def buildVoiceList():
    wantedVoices = []
    for voice in client.list_voices(language_code='en-*').voices:
        if 'wave' in voice.name.lower() or 'neural' in voice.name.lower():
            voiceDict = {
                'name': voice.name,
                'code': voice.language_codes[0]
            }
            wantedVoices.append(voiceDict)
    return wantedVoices

def getRandomVoice():
    return random.choice(voiceList)

json = settings.googleApiJSONPath
client = texttospeech.TextToSpeechClient(credentials=service_account.Credentials.from_service_account_file(json))
voiceList = buildVoiceList()


def TTS(sentence, voice):
    fileNameLong =  "".join([c for c in f"{sentence}" if c.isalpha() or c.isdigit() or c==' ']).rstrip()  
    fileName = fileNameLong[:32]+ ".mp3" #cap filename length
    # Instantiates a client
    print(f"Fetching voice: {fileNameLong}")
    synthesis_input = texttospeech.SynthesisInput(text=sentence)
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")

    print(f"Voice chosen: {voice['name']} language: {voice['code']}")
    voiceSelection = texttospeech.VoiceSelectionParams(
        name=voice['name'], language_code=voice['code']
    )
  
    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voiceSelection, audio_config=audio_config
    )
    # The response's audio_content is binary.
    with open(output+fileName, "wb") as out:
        # Write the response to the output file.
        out.write(response.audio_content)
    return output+fileName

