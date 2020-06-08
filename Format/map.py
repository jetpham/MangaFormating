# imports
import os
import os.path
import re

def sorted_nicely(list):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)


def map(manga, mangaPath):
    # the manga's folder on the desktop

    map = []
    count = [0, 0]
    print('mapping ' + manga)
    # iterate through every volume
    chapterindex = 0
    for volume in sorted_nicely(os.listdir(mangaPath)):
        print('├── ' + volume)
        # iterate through every chapter in current volume
        for chapter in sorted_nicely(os.listdir(mangaPath + '/' + volume)):
            print('│   ├── ' + chapter)
            map.append([[chapter, chapterindex]])
            for file in sorted_nicely(os.listdir(mangaPath + '/' + volume + '/' + chapter)):
                map[chapterindex].append(mangaPath + '/' + volume + '/' + chapter + '/' + file)
            chapterindex += 1
    print('total files mapped: ' + str(count[0]))
    print('non jpg images: ' + str(count[1]))
    print('finished renaming ' + manga)
    for chapter1 in map:
        print(chapter1)
    open('map.txt', 'w').write(str(map))


