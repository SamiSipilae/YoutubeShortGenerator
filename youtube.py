from youtube_upload.client import YoutubeUploader
import settings
import shutil

# due to apparent bug in youtube_upload the oauth file is always deleted, so we keep a copy
shutil.copyfile('_oauth.json', 'oauth.json')


uploader = YoutubeUploader(settings.youtubeClientID ,settings.youtubeClientSecret)
uploader.authenticate()



def upload(file, description):
    # Video options
    options = {
        "title" : "2 sentence horror", # The video title
        "description" : description, # The video description
        "tags" : ["AI", "story", "horror", 'short', '#aigenerated','chatgpt', 'openai', 'artificalintelligence',],
        "categoryId" : settings.youtubeCategory,
        "privacyStatus" : "public", # Video privacy. Can either be "public", "private", or "unlisted"
        "kids" : False, # Specifies if the Video if for kids or not. Defaults to False.
        #"thumbnailLink" : "https://cdn.havecamerawilltravel.com/photographer/files/2020/01/youtube-logo-new-1068x510.jpg" # Optional. Specifies video thumbnail.
    }

    # upload video
    uploader.upload(file, options) 