# imports
import os
import os.path

def map():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
    map = []
    count = [0, 0]
    print('mapping ' + manga)
    # iterate through every volume
    chapterindex = 0
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        # iterate through every chapter in current volume
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            map.append([[chapter, chapterindex]])
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                map[chapterindex].append(mangaPath + '/' + volume + '/' + chapter + '/' + file)
            chapterindex += 1
    print('total files mapped: ' + str(count[0]))
    print('non jpg images: ' + str(count[1]))
    print('finished renaming ' + manga)
    for chapter1 in map:
        print(chapter1)
    open('../map.txt', 'w').write(str(map))


map()
# map = [[[chapter, chapterindex], [filepath1], [filepath2]...], [[chapter, chapterindex], [filepath1], [filepath2]...]...]
