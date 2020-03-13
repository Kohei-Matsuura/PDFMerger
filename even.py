import PyPDF2
import sys

filelist = sys.argv[1]

PDF_LIST = []
with open(filelist) as f:
    for l in f:
        l = l.strip()
        if '.pdf' in l:
            PDF_LIST.append(l.split(' ')[-1])

NEW_PDF_LIST = []
for pdf in PDF_LIST:
    reader = PyPDF2.PdfFileReader(pdf)
    num_pages = reader.getNumPages()
    print('{} has {} pages.'.format(pdf, num_pages))
    if num_pages % 2 == 0:
        pass
    else:
        output = PyPDF2.PdfFileWriter()
        pages = reader.pages
        for page in pages:
            output.addPage(page)
        output.addBlankPage()
        from StringIO import StringIO
        o = StringIO()
        output.write(o)
        with open('even_{}'.format(pdf), mode='w') as f:
            f.write(o.getvalue())
        
