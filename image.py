import PIL
import settings
output = settings.outputPath

def resizeImage(fileName):
    image = PIL.Image.open(fileName)
    image2 = PIL.ImageOps.fit(image, (1080, 1920), bleed = 0.0, centering =(0.5, 0.5))
    newFileName =  fileName.replace(output,output+'resized_')
    image2.save(newFileName)
    return newFileName
