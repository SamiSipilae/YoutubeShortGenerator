import moviepy.editor as mpy
import settings

output = settings.outputPath


def generateVideo(storySegments):
    clips = []
    for segment in storySegments:

        clip = mpy.ImageClip(segment['art'])
        audio = mpy.AudioFileClip(segment['audio']) 
        clip = clip.set_duration(audio.duration)
        clip = clip.set_audio(audio)
        clips.append(clip)

    final = mpy.concatenate_videoclips(clips)
    fileName = output+"video.mp4"
    final.write_videofile(fileName,fps=30,codec='libx264')
    return fileName
