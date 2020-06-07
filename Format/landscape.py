# imports
import os
import re
import os.path
from os import path
from PIL import Image


def convert():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
    # all pages that didn't append to a pdf
    # files that have been removed
    landscapes = []
    count=[0,0]
    print('renaming ' + manga)
    # iterate through every volume
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        # iterate through every chapter in current volume
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                img = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                msize = [int(Image.open(img).size[0]),
                         int(Image.open(img).size[1])]
                if msize[0] > msize[1]:
                    landscapes.append(volume + '/' + chapter + '/' + file)
                    print('│   │   ├── ' + str(file) + ' is a landscape')
                    dup = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file).crop(
                        (0, 0, int(msize[0] / 2), msize[1]))
                    dup.save(mangaPath + '/' + volume + '/' + chapter + '/' + str(int(re.sub('[^0-9]', '', file[-6:]))) + '.5.jpg')
                    dup = Image.open(mangaPath + '/' + volume + '/' + chapter + '/' + file).crop(
                        (int(msize[0] / 2), 0, msize[0], msize[1]))
                    dup.save(mangaPath + '/' + volume + '/' + chapter + '/' + str(int(re.sub('[^0-9]', '', file[-6:]))) + '.jpg')
                    print('│   │   ├── original size: ' + str(msize[0]) + ', ' + str(msize[1]) + '  new size: ' + str(
                        msize[0] / 2) + ', ' + str(msize[1]))
                    count[0] += 2
                else:
                    count[0] += 1
    print('# of landscape files: ' + str(len(landscapes)) if str(len(landscapes)) != '' else '0')
    print('removed files: ' + ', '.join(landscapes) if str(len(landscapes)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('finished landscaping ' + manga)


convert()
