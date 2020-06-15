import os
import os.path
from PIL import Image


def convert(manga, mangaPath):
    removedFiles = []
    count = [0, 0]
    print('converting ' + manga)
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                if file[-3:] != 'jpg':
                    source = mangaPath + '/' + volume + '/' + chapter + '/' + file
                    try:
                        image = Image.open(source)
                        rgbImage = image.convert('RGB')
                        rgbImage.save(source[:-3] + 'jpg')
                        os.remove(source)
                        print('│   │   ├── converted: ' + file[:-4])
                        count[0] += 1
                        count[1] += 1
                    except:
                        print('│   │   ├── can\'t convert ' + file)
                elif file[-3:] == 'jpg':
                    print('│   │   ├── ' + file[:-4] + ' is .jpg')
                    count[0] += 1
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('non jpg images: ' + str(count[1]))
    print('finished renaming ' + manga)
