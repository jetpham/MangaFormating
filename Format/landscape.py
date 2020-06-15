import os
import os.path
from PIL import Image


def landscape(manga, mangaPath):
    landscapes = []
    count = [0, 0]
    print('renaming ' + manga)
    for volume in os.listdir(mangaPath):
        print('├── ' + volume)
        for chapter in os.listdir(mangaPath + '/' + volume):
            print('│   ├── ' + chapter)
            for file in os.listdir(mangaPath + '/' + volume + '/' + chapter):
                image = mangaPath + '/' + volume + '/' + chapter + '/' + file
                if round(Image.open(image).size[0] / Image.open(image).size[1], 2) > 0.8:
                    landscapes.append(image)
                    count[0] += 2
                    dup = Image.open(image).crop(
                        (0, 0, int(Image.open(image).size[0] / 2), Image.open(image).size[1]))
                    dup.save(image[:-4] + '.5.jpg')
                    dup = Image.open(image).crop(
                        (int(Image.open(image).size[0] / 2), 0, Image.open(image).size[0],
                         Image.open(image).size[1]))
                    dup.save(image)
                    print('│   │   │  ' + str(
                        round(Image.open(image).size[0] / Image.open(image).size[1], 2)) + ' - ' + str(
                        Image.open(image).size[0]) + ', ' + str(
                        Image.open(image).size[1]) + ' - ' + str(
                        Image.open(image).size[0] / 2) + ', ' + str(Image.open(image).size[1]) + ' - ' + image)
                else:
                    count[0] += 1
    print('# of landscape files: ' + str(len(landscapes)) if str(len(landscapes)) != '' else '0')
    print('Landscapes: ' + ', '.join(landscapes) if str(len(landscapes)) != '' else 'None')
    print('total images: ' + str(count[0]))
    print('finished landscaping ' + manga)
