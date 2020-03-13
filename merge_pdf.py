import PyPDF2
import sys

filelist = sys.argv[1]

pdf_list = []
with open(filelist) as f:
    for l in f:
        pdf_list.append(l.strip())

output = PyPDF2.PdfFileWriter()
for pdf_dir in pdf_list:
    pdf = PyPDF2.PdfFileReader(pdf_dir)
    pages = pdf.pages
    for page in pages:
        output.addPage(page)
from StringIO import StringIO
o = StringIO()
output.write(o)
with open('merged.pdf', mode='w') as f:
    f.write(o.getvalue())
