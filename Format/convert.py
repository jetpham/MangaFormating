# imports
import os
import re
import os.path
from os import path
from PIL import Image


def mangaformat():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
    # all pages that didn't append to a pdf
    # files that have been removed
    removedFiles = []
    count=[0,0]
    print('renaming ' + manga)
    # iterate through every volume
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        # iterate through every chapter in current volume
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            # # iterate through every file in current chapter
            # for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
            #     # check if current file is a folder
            #     if path.isdir(mangaPath + '/' + volume + '/' + chapter + '/' + file):
            #         # remove current file
            #         os.rmdir(mangaPath + '/' + volume + '/' + chapter + '/' + file)
            # iterate through every file in current chapter
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                # # check if the current file is a .bin
                # if file[-3:] == 'bin':
                #     # Remove current file
                #     os.remove(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                #     # add the file path to removedFiles
                #     removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                #     # move onto next fil
                #     continue
                # takes the 7 characters of the file's name
                # which in most files includes the file number, the ".",
                # and the file extension (jpg or png)
                # checks if there are any numbers in those 7 characters
                # there should be a number for each file
                # which corresponds to the
                if file[-3:] != 'jpg':
                    # path of the file
                    source = mangaPath + '/' + volume + '/' + chapter + '/' + file
                    # attempt to compress / convert file into .jpg format
                    try:
                        # set im to the current file
                        image = Image.open(source)
                        # im to rgbImage which makes it compatible to be saved as .jpg
                        rgbImage = image.convert('RGB')
                        # save rgbImage as .jpg but with the new name
                        rgbImage.save(source + '.jpg')
                        # remove original file
                        os.remove(source)
                        print('│   │   ├── converted: ' + file[:-4])
                        count[0] += 1
                        count[1] += 1
                    except:
                        # printing error message, "can't convert file to .jpg"
                        print('│   │   ├── can\'t convert ' + file)
                elif file[-3:] == 'jpg':
                    print('│   │   ├── ' + file[:-4] + ' is .jpg')
                    count[0] += 1
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('non jpg images: ' + str(count[1]))
    print('finished renaming ' + manga)


mangaformat()
