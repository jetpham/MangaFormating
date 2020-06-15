import os
import re
import os.path
from os import path


def rename(manga, mangaPath):
    removedFiles = []
    print('renaming ' + manga)
    for volume in os.listdir(mangaPath):
        newVolume = re.sub('[^0-9]', '', volume)
        if volume != newVolume:
            source = mangaPath + '/' + volume
            destination = mangaPath + '/' + newVolume
            try:
                os.rename(source, destination)
            except:
                print('├── can\'t rename ' + volume + ' to ' + newVolume)
                continue
        print('├── ' + volume + '         ' + newVolume)
        for chapter in os.listdir(mangaPath + '/' + newVolume):
            newChapter = re.sub('[^0-9^.]', '', chapter).strip('.')
            print('asdfasdf     ' + newChapter)
            if chapter != newChapter:
                source = mangaPath + '/' + newVolume + '/' + chapter
                destination = mangaPath + '/' + newVolume + '/' + newChapter
                try:
                    os.rename(source, destination)
                except:
                    print('│   ├── can\'t rename ' + chapter + ' to ' + newChapter)
                    continue
            print('│   ├── ' + chapter + '  to ' + newChapter)
            for file in os.listdir(mangaPath + '/' + newVolume + '/' + newChapter):
                if re.sub('[^0-9]', '', file) != '':
                    newFile = re.sub('[^0-9]', '', file[:-4]).lstrip('0') + file[-4:]
                else:
                    os.remove(mangaPath + '/' + newVolume + '/' + newChapter + '/' + file)
                    removedFiles.append(manga + '/' + newVolume + '/' + newChapter + '/' + file)
                    continue
                source = mangaPath + '/' + newVolume + '/' + newChapter + '/' + file
                destination = mangaPath + '/' + newVolume + '/' + newChapter + '/' + newFile
                try:
                    os.rename(source, destination)
                    print('│   │   ├── ' + file + '  to ' + newFile)
                except:
                    print('│   │   ├── can\'t rename or convert' + file + ' to ' + newFile)
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('finished renaming ' + manga)
