import os
from os import path
from fpdf import FPDF
import ast
from PIL import Image
import statistics

def chaptersToPDF(manga, mangaPath, mapPath):
    Paths = ast.literal_eval(open(mapPath, 'r').read())
    errorPages = []
    map = []
    # the manga's folder on the desktop
    if False if os.path.isdir(mangaPath + 'ch/') else True:
        os.mkdir(mangaPath + 'ch/')
    for chapter in Paths:
        chapterwidth = []
        chapterheight = []
        for image in chapter[1:]:
            chapterwidth.append(Image.open(image).size[0])
            chapterheight.append(Image.open(image).size[1])
        pdf = FPDF('P', 'mm', (statistics.median(chapterwidth), statistics.median(chapterheight)))
        pdf.set_auto_page_break(0)
        for image in chapter[1:]:
            if path.exists(image):
                pdf.add_page()
                try:
                    pdf.image(image, 0, 0, statistics.median(chapterwidth), statistics.median(chapterheight))
                except:
                    print(image)
            else:
                errorPages.append(image)
        pdf.output(mangaPath + 'ch/' + chapter[0][0] + '.pdf', 'F')
        map.append(mangaPath + 'ch/' + chapter[0][0] + '.pdf')
        print(str(int(chapter[0][1] / Paths[-1][0][1] * 100)) + '% ' + chapter[0][0] + '.pdf')
    open(mapPath, 'w').write(str(map))
