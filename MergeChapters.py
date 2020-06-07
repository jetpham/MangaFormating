from PyPDF2 import PdfFileReader, PdfFileWriter
import re

Paths = ['../Firech/192.pdf', '../Firech/193.pdf', '../Firech/194.pdf', '../Firech/195.pdf', '../Firech/0.pdf',
         '../Firech/1.pdf', '../Firech/10.pdf', '../Firech/100.pdf', '../Firech/101.pdf', '../Firech/102.pdf',
         '../Firech/103.pdf', '../Firech/104.pdf', '../Firech/105.pdf', '../Firech/106.pdf', '../Firech/107.pdf',
         '../Firech/108.pdf', '../Firech/109.pdf', '../Firech/11.pdf', '../Firech/110.pdf', '../Firech/111.pdf',
         '../Firech/112.pdf', '../Firech/113.pdf', '../Firech/114.pdf', '../Firech/115.pdf', '../Firech/116.pdf',
         '../Firech/117.pdf', '../Firech/118.pdf', '../Firech/119.pdf', '../Firech/12.pdf', '../Firech/120.pdf',
         '../Firech/121.pdf', '../Firech/122.pdf', '../Firech/123.pdf', '../Firech/124.pdf', '../Firech/125.pdf',
         '../Firech/126.pdf', '../Firech/127.pdf', '../Firech/128.pdf', '../Firech/129.pdf', '../Firech/13.pdf',
         '../Firech/130.pdf', '../Firech/131.pdf', '../Firech/132.pdf', '../Firech/133.pdf', '../Firech/134.pdf',
         '../Firech/135.pdf', '../Firech/136.pdf', '../Firech/137.pdf', '../Firech/138.pdf', '../Firech/139.pdf',
         '../Firech/14.pdf', '../Firech/140.pdf', '../Firech/141.pdf', '../Firech/142.pdf', '../Firech/143.pdf',
         '../Firech/144.pdf', '../Firech/145.pdf', '../Firech/146.pdf', '../Firech/147.pdf', '../Firech/148.pdf',
         '../Firech/149.pdf', '../Firech/15.pdf', '../Firech/150.pdf', '../Firech/151.pdf', '../Firech/152.pdf',
         '../Firech/153.pdf', '../Firech/154.pdf', '../Firech/155.pdf', '../Firech/156.pdf', '../Firech/157.pdf',
         '../Firech/158.pdf', '../Firech/159.pdf', '../Firech/16.pdf', '../Firech/160.pdf', '../Firech/161.pdf',
         '../Firech/162.pdf', '../Firech/163.pdf', '../Firech/164.pdf', '../Firech/165.pdf', '../Firech/166.pdf',
         '../Firech/167.pdf', '../Firech/168.pdf', '../Firech/169.pdf', '../Firech/17.pdf', '../Firech/170.pdf',
         '../Firech/171.pdf', '../Firech/172.pdf', '../Firech/173.pdf', '../Firech/174.pdf', '../Firech/175.pdf',
         '../Firech/176.pdf', '../Firech/177.pdf', '../Firech/178.pdf', '../Firech/179.pdf', '../Firech/18.pdf',
         '../Firech/180.pdf', '../Firech/181.pdf', '../Firech/182.pdf', '../Firech/183.pdf', '../Firech/184.pdf',
         '../Firech/185.pdf', '../Firech/19.pdf', '../Firech/2.pdf', '../Firech/20.pdf', '../Firech/21.pdf',
         '../Firech/22.pdf', '../Firech/23.pdf', '../Firech/24.pdf', '../Firech/25.pdf', '../Firech/26.pdf',
         '../Firech/27.pdf', '../Firech/28.pdf', '../Firech/29.pdf', '../Firech/3.pdf', '../Firech/30.pdf',
         '../Firech/31.pdf', '../Firech/32.pdf', '../Firech/33.pdf', '../Firech/34.pdf', '../Firech/35.pdf',
         '../Firech/36.pdf', '../Firech/37.pdf', '../Firech/38.pdf', '../Firech/39.pdf', '../Firech/4.pdf',
         '../Firech/40.pdf', '../Firech/41.pdf', '../Firech/42.pdf', '../Firech/43.pdf', '../Firech/44.pdf',
         '../Firech/45.pdf', '../Firech/46.pdf', '../Firech/47.pdf', '../Firech/48.pdf', '../Firech/49.pdf',
         '../Firech/5.pdf', '../Firech/50.pdf', '../Firech/51.pdf', '../Firech/52.pdf', '../Firech/53.pdf',
         '../Firech/54.pdf', '../Firech/55.pdf', '../Firech/56.pdf', '../Firech/57.pdf', '../Firech/58.pdf',
         '../Firech/59.pdf', '../Firech/6.pdf', '../Firech/60.pdf', '../Firech/61.pdf', '../Firech/62.pdf',
         '../Firech/63.pdf', '../Firech/64.pdf', '../Firech/65.pdf', '../Firech/66.pdf', '../Firech/67.pdf',
         '../Firech/68.pdf', '../Firech/69.pdf', '../Firech/7.pdf', '../Firech/70.pdf', '../Firech/71.pdf',
         '../Firech/72.pdf', '../Firech/73.pdf', '../Firech/74.pdf', '../Firech/75.pdf', '../Firech/76.pdf',
         '../Firech/77.pdf', '../Firech/78.pdf', '../Firech/79.pdf', '../Firech/8.pdf', '../Firech/80.pdf',
         '../Firech/81.pdf', '../Firech/82.pdf', '../Firech/83.pdf', '../Firech/84.pdf', '../Firech/85.pdf',
         '../Firech/86.pdf', '../Firech/87.pdf', '../Firech/88.pdf', '../Firech/89.pdf', '../Firech/9.pdf',
         '../Firech/90.pdf', '../Firech/91.pdf', '../Firech/92.pdf', '../Firech/93.pdf', '../Firech/94.pdf',
         '../Firech/95.pdf', '../Firech/96.pdf', '../Firech/97.pdf', '../Firech/98.pdf', '../Firech/99.pdf',
         '../Firech/186.pdf', '../Firech/187.pdf', '../Firech/188.pdf', '../Firech/189.pdf',
         '../Firech/190.pdf', '../Firech/191.pdf', '../Firech/196.pdf', '../Firech/197.pdf', '../Firech/198.pdf',
         '../Firech/199.pdf', '../Firech/200.pdf', '../Firech/201.pdf', '../Firech/202.pdf', '../Firech/203.pdf',
         '../Firech/204.pdf', '../Firech/205.pdf', '../Firech/206.pdf', '../Firech/207.pdf', '../Firech/208.pdf',
         '../Firech/209.pdf', '../Firech/210.pdf', '../Firech/211.pdf', '../Firech/212.pdf', '../Firech/213.pdf',
         '../Firech/214.pdf', '../Firech/215.pdf', '../Firech/216.pdf', '../Firech/217.pdf', '../Firech/218.pdf']


def sorted_nicely(l):
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


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
