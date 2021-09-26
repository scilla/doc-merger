from docx import Document
import os, time

files = []
source_folder = 'DOC_source'
l = os.listdir(source_folder)
for x in l:
    filename, file_extension = os.path.splitext(x)
    if file_extension != '.docx':
        continue
    files.append(os.path.join(source_folder, x))
    print(x)

merged_document = Document()

for index, file in enumerate(files):
    sub_doc = Document(file)

    # Don't add a page break if you've reached the last file.
    if index < len(files)-1:
       sub_doc.add_page_break()

    for element in sub_doc.element.body:
        merged_document.element.body.append(element)

merged_document.save('merged_' + str(time.time()) + '.docx')
