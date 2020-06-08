import os
import os.path
from PIL import Image


def landscape(manga, mangaPath):
    landscapes = []
    count = [0, 0]
    print('renaming ' + manga)
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                image = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                fileDimentions = [image.size[0],
                                  image.size[1]]
                if fileDimentions[0] > fileDimentions[1]:
                    landscapes.append(volume + '/' + chapter + '/' + file)
                    print('│   │   ├── ' + str(file) + ' is a landscape')
                    dup = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file).crop(
                        (0, 0, int(fileDimentions[0] / 2), fileDimentions[1]))
                    dup.save(mangaPath + '/' + volume + '/' + chapter + '/' +
                             file[:-4] + '.5.jpg')
                    dup = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file).crop(
                        (int(fileDimentions[0] / 2), 0, fileDimentions[0], fileDimentions[1]))
                    dup.save(mangaPath + '/' + volume + '/' + chapter + '/' +
                             file)
                    print('│   │   │   original size: ' + str(fileDimentions[0]) + ', ' + str(
                        fileDimentions[1]) + '  new size: ' + str(
                        fileDimentions[0] / 2) + ', ' + str(fileDimentions[1]))
                    count[0] += 2
                else:
                    count[0] += 1
    print('# of landscape files: ' + str(len(landscapes)) if str(len(landscapes)) != '' else '0')
    print('Landscapes: ' + ', '.join(landscapes) if str(len(landscapes)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('finished landscaping ' + manga)
