from fpdf import FPDF
import os.path
from os import path
chap =
imagelist = []
temp = []
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
        wr.append(image)
print(pdf.page_no())
pdf.output(chap + '/' + cn + '.pdf', 'F')
pdf.output('../Stonech/' + cn + '.pdf', 'F')
paths.append('../Stonech/' + cn + '.pdf')