import PyPDF2
import os

def listar_arquivos(diretorio):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        print(arquivo)


'''
pdf_file = open('lorem-ipsum.pdf', 'rb')
dados_pdf = PyPDF2.PdfFileReader(pdf_file)
arq1 = ("")
arq2 =
arq3 = 
'''

