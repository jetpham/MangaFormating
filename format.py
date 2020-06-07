# imports
import os
import re
from fpdf import FPDF
from PIL import Image
import os.path
from os import path


def mangaformat():
    # the manga's folder on the deskto
    f = 'Food'
    # all pages that didn't append to a pdf
    errorPages = []
    # files that have been removed
    removedFiles = []
    # the paths of every chapter
    # .pdf in the {manga}ch desktop folder
    paths = []
    # iterate through every volume
    print('formatting ' + str(f))
    for v in os.listdir('../' + f):
        # the volume folder is renamed to itself but with only numbers
        vn = re.sub('[^0-9^.]', '', v)
        # skips renaming if the volume is already formatted properally
        if v != vn:
            # the path of the volume
            src = '../' + f + '/' + v
            # the path of the volume with the new name
            dest = '../' + f + '/' + vn
            try:
                # renaming the volume
                os.rename(src, dest)
            except:
                # printing error message, "cant rename old volume to new volume"
                print('├── can\'t rename ' + v + ' to ' + vn)
                # move onto the next volume
                continue
        # log the renaming of the volume
        print('├── ' + v + '         ' + vn)
        # iterate through every chapter in current volume
        for c in os.listdir('../' + f + '/' + vn):
            # the chapter folder is renamed to itself but with only numbers and decimals
            # example: "Chapter 14.5" --> "14.5"
            cn = re.sub('[^0-9,.]', '', c)
            # skips renaming if the chapter is already formatted properally
            if c != cn:
                # path of the chapter
                src = '../' + f + '/' + vn + '/' + c
                # path of the chapter with the new name
                dest = '../' + f + '/' + vn + '/' + cn
                try:
                    # renaming the chapter
                    os.rename(src, dest)
                except:
                    # printing error message, "cant rename old chapter to new chapter"
                    print('│   ├── can\'t rename ' + c + ' to ' + cn)
                    # move onto the next chapter
                    continue
            # log the renaming of the chapter
            print('│   ├── ' + c + '  to ' + cn)
            # iterate through every file in current chapter
            for m in os.listdir('../' + f + '/' + vn + '/' + cn):
                # check if current file is a folder
                if path.isdir('../' + f + '/' + vn + '/' + cn + '/' + m):
                    # remove current file
                    os.rmdir('../' + f + '/' + vn + '/' + cn + '/' + m)
            # iterate through every file in current chapter
            for m in os.listdir('../' + f + '/' + vn + '/' + cn):
                # check if the current file is a .bin
                if m[-3:] == 'bin':
                    # Remove current file
                    os.remove('../' + f + '/' + vn + '/' + cn + '/' + m)
                    # add the file path to removedFiles
                    removedFiles.append(f + '/' + vn + '/' + cn + '/' + m)
                    # move onto next fil
                    continue
                # takes the 7 characters of the file's name
                # which in most files includes the file number, the ".",
                # and the file extension (jpg or png)
                # checks if there are any numbers in those 7 characters
                # there should be a number for each file
                # which corresponds to the
                elif re.sub('[^0-9]', '', m[-7:]) != '':
                    # the file is renamed to itself but with only numbers
                    mn = str(int(re.sub('[^0-9]', '', m)))
                else:
                    # remove the file
                    os.remove('../' + f + '/' + vn + '/' + cn + '/' + m)
                    # add the file path to removedFiles
                    removedFiles.append(f + '/' + vn + '/' + cn + '/' + m)
                    # move onto next file
                    continue
                # path of the file
                src = '../' + f + '/' + vn + '/' + cn + '/' + m
                # path of the file with the new name
                dest = '../' + f + '/' + vn + '/' + cn + '/' + mn
                # attempt to compress / convert file into .jpg format
                try:
                    # set im to the current file
                    im = Image.open(src)
                    # im to rgb_im which makes it compatible to be saved as .jpg
                    rgb_im = im.convert('RGB')
                    # save rgb_im as .jpg but with the new name
                    rgb_im.save(dest + '.jpg')
                    # remove original file
                    os.remove(src)
                    print('│   │   ├── ' + m + '  to ' + mn)
                except:
                    # printing error message, "cant rename or convert old file to new file"
                    print('│   │   ├── can\'t rename or convert' + m + ' to ' + mn)
            for m in os.listdir('../' + f + '/' + vn + '/' + cn):
                img = Image.open('../' + f + '/' + vn + '/' + cn + '/' + m)
                msize = [int(Image.open(img).size[0]),
                         int(Image.open(img).size[1])]
                if msize[0] > msize[1]:
                    print('│   │   ├── ' + str(mn) + ' is a landscape')
                    dup = Image.open('../' + f + '/' + vn + '/' + cn + '/' + m).crop(
                        (0, 0, int(msize[0] / 2), msize[1]))
                    dup.save('../' + f + '/' + vn + '/' + cn + '/' + str(int(re.sub('[^0-9]', '', m[-6:]))) + '.5.jpg')
                    dup = Image.open('../' + f + '/' + vn + '/' + cn + '/' + m).crop(
                        (int(msize[0] / 2), 0, msize[0], msize[1]))
                    dup.save('../' + f + '/' + vn + '/' + cn + '/' + str(int(re.sub('[^0-9]', '', m[-6:]))) + '.jpg')
                    print('│   │   ├── original size: ' + str(msize[0]) + ', ' + str(msize[1]) + '  new size: ' + str(
                        msize[0] / 2) + ', ' + str(msize[1]))
            chap = '../' + f + '/' + vn + '/' + cn
            imagelist = []
            for n in range(len(os.listdir(chap))):
                imagelist.append(chap + '/' + str(n + 1) + '.jpg')
                try:
                    if path.exists(chap + '/' + str(n + 1.5) + '.jpg'):
                        imagelist.append(chap + '/' + str(n + 1.5) + '.jpg')
                except:
                    continue
            pdf = FPDF('P', 'mm', (728, 1048))
            pdf.set_auto_page_break(0)
            for image in imagelist:
                if path.exists(image):
                    pdf.add_page()
                    pdf.image(image, None, None, 728, 1048)
                else:
                    errorPages.append(image)

            # pdf.output(chap + '/' + cn + '.pdf', 'F')
            pdf.output('../' + f + 'ch/' + cn + '.pdf', 'F')
            paths.append('../' + f + 'ch/' + cn + '.pdf')
            print('│   ├── Page Length: ' + str(pdf.page_no()))

    print('Pages that didn\'t append to a pdf: ' + ', '.join(errorPages))
    print('# of removed files: ' + str(len(removedFiles)))
    print('removed files: ' + ', '.join(removedFiles))
    try:
        open('../' + f + 'Paths.txt', 'x').write(str(paths))
    except:
        open('../' + f + 'Paths.txt', 'w').write(str(paths))
    print('paths: ' + ', '.join(paths))
    print('finished formatting ' + f)


mangaformat()
