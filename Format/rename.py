# imports
import os
import re
import os.path
from os import path


def mangaformat():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
    # all pages that didn't append to a pdf
    # files that have been removed
    removedFiles = []
    # iterate through every volume
    print('renaming ' + manga)
    for volume in os.listdir(mangaPath):
        # the volume folder is renamed to itself but with only numbers
        newVolume = re.sub('[^0-9^.]', '', volume)
        # skips renaming if the volume is already formatted properly
        if volume != newVolume:
            # the path of the volume
            source = mangaPath + '/' + volume
            # the path of the volume with the new name
            destination = mangaPath + '/' + newVolume
            try:
                # renaming the volume
                os.rename(source, destination)
            except:
                # printing error message, "cant rename old volume to new volume"
                print('├── can\'t rename ' + volume + ' to ' + newVolume)
                # move onto the next volume
                continue
        # log the renaming of the volume
        print('├── ' + volume + '         ' + newVolume)
        # iterate through every chapter in current volume
        for chapter in os.listdir(mangaPath + '/' + newVolume):
            # the chapter folder is renamed to itself but with only numbers and decimals
            # example: "Chapter 14.5" --> "14.5"
            newChapter = re.sub('[^0-9,.]', '', chapter)
            # skips renaming if the chapter is already formatted properly
            if chapter != newChapter:
                # path of the chapter
                source = mangaPath + '/' + newVolume + '/' + chapter
                # path of the chapter with the new name
                destination = mangaPath + '/' + newVolume + '/' + newChapter
                try:
                    # renaming the chapter
                    os.rename(source, destination)
                except:
                    # printing error message, "cant rename old chapter to new chapter"
                    print('│   ├── can\'t rename ' + chapter + ' to ' + newChapter)
                    # move onto the next chapter
                    continue
            # log the renaming of the chapter
            print('│   ├── ' + chapter + '  to ' + newChapter)
            # iterate through every file in current chapter
            for file in os.listdir(mangaPath + '/' + newVolume + '/' + newChapter):
                # check if current file is a folder
                if path.isdir(mangaPath + '/' + newVolume + '/' + newChapter + '/' + file):
                    # remove current file
                    os.rmdir(mangaPath + '/' + newVolume + '/' + newChapter + '/' + file)
            # iterate through every file in current chapter
            for file in os.listdir(mangaPath + '/' + newVolume + '/' + newChapter):
                # check if the current file is a .bin
                if file[-3:] == 'bin':
                    # Remove current file
                    os.remove(mangaPath + '/' + newVolume + '/' + newChapter + '/' + file)
                    # add the file path to removedFiles
                    removedFiles.append(manga + '/' + newVolume + '/' + newChapter + '/' + file)
                    # move onto next fil
                    continue
                # takes the 7 characters of the file's name
                # which in most files includes the file number, the ".",
                # and the file extension (jpg or png)
                # checks if there are any numbers in those 7 characters
                # there should be a number for each file
                # which corresponds to the
                elif re.sub('[^0-9]', '', file[-7:]) != '':
                    # the file is renamed to itself but with only numbers
                    newFile = str(int(re.sub('[^0-9]', '', file))) + file[-4:]
                else:
                    # remove the file
                    os.remove(mangaPath + '/' + newVolume + '/' + newChapter + '/' + file)
                    # add the file path to removedFiles
                    removedFiles.append(manga + '/' + newVolume + '/' + newChapter + '/' + file)
                    # move onto next file
                    continue
                # path of the file
                source = mangaPath + '/' + newVolume + '/' + newChapter + '/' + file
                # path of the file with the new name
                destination = mangaPath + '/' + newVolume + '/' + newChapter + '/' + newFile
                # attempt to compress / convert file into .jpg format
                try:
                    # renaming the image
                    os.rename(source, destination)
                    print('│   │   ├── ' + file + '  to ' + newFile)
                except:
                    # printing error message, "cant rename or convert old file to new file"
                    print('│   │   ├── can\'t rename or convert' + file + ' to ' + newFile)
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('finished renaming ' + manga)


mangaformat()
