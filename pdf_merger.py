import PyPDF2 as pdf
import os
import time

source_folder = 'PDF_source'
l = os.listdir(source_folder)
writer = pdf.PdfFileWriter()
blank_file = open('blank.pdf', 'rb')
blank_reader = pdf.PdfFileReader(blank_file)
blank_page = blank_reader.getPage(0)

for x in l:
    filename, file_extension = os.path.splitext(x)
    if file_extension != '.pdf':
        continue
    print(x)
    pdf_file = open(os.path.join(source_folder, x), 'rb')
    reader = pdf.PdfFileReader(pdf_file)
    for page_number in range(reader.numPages):
        page = reader.getPage(page_number)
        writer.addPage(page)
    if reader.numPages % 2:
        writer.addPage(blank_page)

with open('output_' + str(round(time.time())) + '.pdf', 'wb') as f:
    writer.write(f)

