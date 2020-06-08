from os import path
from fpdf import FPDF
import ast

Paths = ast.literal_eval(open('../map.txt', 'r').read())


def chaptersToPDF(manga, mangaPath):
    # the manga's folder on the desktop

    errorPages = []
    map = []
    for chapter in Paths:
        pdf = FPDF('P', 'mm', (728, 1048))
        pdf.set_auto_page_break(0)
        for image in chapter[1:]:
            if path.exists(image):
                pdf.add_page()
                pdf.image(image, None, None, 728, 1048)
            else:
                errorPages.append(image)
        pdf.output(mangaPath + 'ch/' + chapter[0][0] + '.pdf', 'F')
        map.append(mangaPath + 'ch/' + chapter[0][0] + '.pdf')
        print(str(int(chapter[0][1] / Paths[-1][0][1] * 100)) + '%')
    open('map.txt', 'w').write(str(map))



