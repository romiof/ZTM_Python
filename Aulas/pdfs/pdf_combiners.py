# Script para fazer Merge dos arquivos de PDF, usando a lib PyPDF2
# Entrada de arquivos são os argumentos passados na linha de comando, após ter chamado o scritp em Python
import PyPDF2
import sys

# Faz a leitura de N parametros na chamada do script e salva eles em uma lista.
inputs = sys.argv[1:]

def pdf_combine(pdf_list):
    objMerger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        objMerger.append(pdf)
    objMerger.write(f"C:/Users/fromio/Desktop/Udemy/ZTM_Python/Aulas/pdfs/super.pdf")

pdf_combine(inputs)

