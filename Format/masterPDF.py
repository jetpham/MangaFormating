from PyPDF2 import PdfFileReader, PdfFileWriter
import ast




def merge_pdfs(mangaPath, mapPath):
    Paths = ast.literal_eval(open(mapPath, 'r').read())
    pdf_writer = PdfFileWriter()
    print(type(Paths))
    for path in Paths:
        print('added: ' + str(path))
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # Add each page to the writer object
            pdf_writer.addPage(pdf_reader.getPage(page))
    # Write out the merged PDF
    with open(mangaPath + '.pdf', 'wb') as out:
        pdf_writer.write(out)
