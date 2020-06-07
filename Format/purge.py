# imports
import os
import re
import os.path
from os import path
from PIL import Image


def purge():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
    # all pages that didn't append to a pdf
    # files that have been removed
    removedFiles = []
    count = [0, 0]
    otherFormats = []

    def removeDuplicates(duplicateArray):
        final_list = []
        for item in duplicateArray:
            if item not in final_list:
                final_list.append(item)
        return final_list

    print('purging ' + manga)
    # iterate through every volume
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        # iterate through every chapter in current volume
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            # iterate through every file in current chapter
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                # check if current file is a folder
                if path.isdir(mangaPath + '/' + volume + '/' + chapter + '/' + file):
                    # remove current file
                    os.rmdir(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    removedFiles.append(file)
                # check if the current file is a .bin
                elif file[-3:] == 'bin':
                    # Remove current file
                    os.remove(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    # add the file path to removedFiles
                    removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                    # move onto next fil
                    continue
                elif file[-3:] == 'jpg':
                    print('│   │   ├── ' + file[:-4] + ' is .jpg')
                    count[0] += 1
                else:
                    otherFormats.append(file.split('.')[-1])
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('other found formats: ' + ', '.join(removeDuplicates(otherFormats)))
    print('finished purging ' + manga)


purge()
