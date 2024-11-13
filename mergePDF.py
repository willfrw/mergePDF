import PyPDF2
import os
from pathlib import Path

def listar_arquivos(diretorio, lista_arquivos):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        if '.pdf' in arquivo:
            lista_arquivos.append(arquivo)

def merge_pdf(diretorio, lista_arquivo_pdf, nome_arquivo_mergeado):
    merge = PyPDF2.PdfFileMerger()
    
    for arquivo in lista_arquivo_pdf:
        merge.append(arquivo)

    merge.write(nome_arquivo_mergeado)

diretorio = "c://Users//willi//OneDrive//Documentos//Projetos Computação//mergepdf"

lista_pdfs = []

listar_arquivos(diretorio, lista_pdfs)

print(lista_pdfs)

lista_arq_lido = []

for pdf in lista_pdfs:
    arquivo = open(pdf, 'rb')
    lista_arq_lido.append(PyPDF2.PdfFileReader(arquivo))

merge_pdf(lista_arq_lido, "teste_merge.pdf")


'''
pdf_file = open('lorem-ipsum.pdf', 'rb')
dados_pdf = PyPDF2.PdfFileReader(pdf_file)
arq1 = ("")
arq2 =
arq3 = 
'''

