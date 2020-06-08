# imports
import os
import re
import os.path
from os import path
from PIL import Image


def lanscape(manga, mangaPath):
    # the manga's folder on the desktop

    # all pages that didn't append to a pdf
    # files that have been removed
    landscapes = []
    count = [0, 0]
    print('renaming ' + manga)
    # iterate through every volume
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        # iterate through every chapter in current volume
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
                             file[:-4] + '.jpg')
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



