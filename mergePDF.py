import PyPDF2
import os

def listar_arquivos(diretorio, lista_arquivos):
    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        if '.pdf' in arquivo:
            lista_arquivos.append(arquivo)

def merge_pdf(lista_arquivo_pdf, nome_arquivo_mergeado):
    merge = PyPDF2.PdfMerger()
    
    for arquivo in lista_arquivo_pdf:
        merge.append(arquivo)

    merge.write(nome_arquivo_mergeado)

# colocar diretório de onde estão os arquivos pdf - depois devo incorporar algo que já pega o diretório automaticamente
diretorio = "c://Users//willi//OneDrive//Documentos//Projetos Computação//mergepdf"

lista_pdfs = []

listar_arquivos(diretorio, lista_pdfs)

print(lista_pdfs)

lista_arq_lido = []

for pdf in lista_pdfs:
    arquivo = open(pdf, 'rb')
    lista_arq_lido.append(PyPDF2.PdfReader(arquivo))

merge_pdf(lista_arq_lido, "teste_merge.pdf")


