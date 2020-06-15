import os
import os.path
import re


def sorted_nicely(list):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(list, key=alphanum_key)


def sort_files(list):
    return sorted(list, key=lambda x: float(x[:-4]))


def map(manga, mangaPath, mapPath):
    complex = []
    count = [0, 0]
    print('mapping ' + manga)
    chapterindex = 0
    for volume in sorted_nicely(os.listdir(mangaPath)):
        print('├── ' + volume)
        for chapter in sorted_nicely(os.listdir(mangaPath + '/' + volume)):
            print('│   ├── ' + chapter)
            complex.append([[chapter, chapterindex]])
            for file in sort_files(os.listdir(mangaPath + '/' + volume + '/' + chapter)):
                complex[chapterindex].append(mangaPath + '/' + volume + '/' + chapter + '/' + file)
            print(sorted_nicely(os.listdir(mangaPath + '/' + volume + '/' + chapter)))
            chapterindex += 1
    print('total files mapped: ' + str(count[0]))
    print('non jpg images: ' + str(count[1]))
    print('finished renaming ' + manga)
    for chapter1 in complex:
        print(chapter1)
    open(mapPath, 'w').write(str(complex))