from PyPDF2 import PdfFileReader, PdfFileWriter
import re
import ast

Paths = ast.literal_eval(open('../map.txt', 'r').read())

Paths = sorted_nicely(Paths)


def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    print(type(paths))
    for path in paths:
        print('added: ' + str(path))
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)


merge_pdfs(Paths, output='../Fire.pdf')
print(Paths)

# # imports
# import os
# import re
# import os.path
# from os import path
# from PIL import Image
# from fpdf import FPDF
# import img2pdf
# import ast
#
# Paths = ast.literal_eval(open('../map.txt', 'r').read())
#
#
# def masterPDF(x, y, w, h):
#     simplePaths = []
#     # the manga's folder on the desktop
#     manga = 'Food'
#     user = 'Jet Pham'
#     mangaPath = 'C:/Users/' + user + '/Desktop/' + manga
#     errorPages = []
#     pdf = FPDF()
#     pdf.set_auto_page_break(0)
#     for chapter in Paths:
#         for image in chapter[1:]:
#             if path.exists(image):
#                 simplePaths.append(image)
#     for image in simplePaths:
#         pdf.add_page()
#         pdf.image(image, x, y, w, h)
#     print(str(int(chapter[0][1] / Paths[-1][0][1] * 100)) + '%')
#     print('exporting...')
#     print('# of pages: ' + pdf.page_no())
#     pdf.output(mangaPath + '.pdf', 'F')
#     print('done exporting')
#
#
# masterPDF(0, 0, 1066, 1600)
