import PyPDF2

template = PyPDF2.PdfFileReader(open(f"C:/Users/fromio/Desktop/Udemy/ZTM_Python/Aulas/pdfs/super.pdf", 'rb'))
watermark = PyPDF2.PdfFileReader(open(f"C:/Users/fromio/Desktop/Udemy/ZTM_Python/Aulas/pdfs/wtr.pdf", 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    pag = template.getPage(i)
    pag.mergePage(watermark.getPage(0))
    output.addPage(pag)

with open(f"C:/Users/fromio/Desktop/Udemy/ZTM_Python/Aulas/pdfs/exercicio.pdf", 'wb') as file:
    output.write(file)
