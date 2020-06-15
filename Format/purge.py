import os
import os.path
from os import path


def purge(manga, mangaPath):
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
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                if not any(char.isdigit() for char in file):
                    os.remove(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                    print('has no numbers ' + manga + '/' + volume + '/' + chapter + '/' + file)
                    continue
                elif path.isdir(mangaPath + '/' + volume + '/' + chapter + '/' + file):
                    os.rmdir(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                    print('is folder ' + manga + '/' + volume + '/' + chapter + '/' + file)
                    continue
                elif file[-3:] == 'bin':
                    os.remove(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                    print('│   │   ├── ' + file[:-4] + ' is .bin')
                    continue
                elif file[-3:] == 'jpg':
                    print('│   │   ├── ' + file[:-4] + ' is .jpg')
                    count[0] += 1
                elif file[-3:] == 'png':
                    print('│   │   ├── ' + file[:-4] + ' is .png')
                    count[0] += 1
                else:
                    otherFormats.append(file.split('.')[-1])
                    os.remove(mangaPath + '/' + volume + '/' + chapter + '/' + file)
                    removedFiles.append(manga + '/' + volume + '/' + chapter + '/' + file)
                    print('other format ' + manga + '/' + volume + '/' + chapter + '/' + file)
                    continue
    print('# of removed files: ' + str(len(removedFiles)) if str(len(removedFiles)) != '' else '0')
    print('removed files: ' + ', '.join(removedFiles) if str(len(removedFiles)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('other found formats: ' + ', '.join(removeDuplicates(otherFormats)))
    print('finished purging ' + manga)
