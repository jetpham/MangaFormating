from os import path
from fpdf import FPDF
import ast

Paths = ast.literal_eval(open('../map.txt', 'r').read())


def chaptersToPDF():
    # the manga's folder on the desktop
    manga = 'Food'
    user = 'Jet Pham'
    mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
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
    open('../map.txt', 'w').write(str(map))


chaptersToPDF()
