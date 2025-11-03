#janela para selecionar a pasta no computador

import os
from tkinter.filedialog import askdirectory
import shutil

pasta_selecionada = askdirectory()
print(pasta_selecionada)

lista_arquivos = os.listdir(pasta_selecionada)
print(lista_arquivos)

#Fazer backup dos arquivos e pastas
nome_pasta = "backup"
nome_backup = f"{pasta_selecionada}/{nome_pasta}"

if not os.path.exists(nome_backup):
    os.mkdir(nome_backup)

for arquivo in lista_arquivos:
    print(arquivo)
    nome_arquivo = f"{nome_pasta}/{arquivo}"
    nome_final_arquivo = f"{nome_backup}/{arquivo}"

    if "." in arquivo:
         shutil.copy2(nome_arquivo, nome_final_arquivo)
    elif "backup" != arquivo:
        shutil.copytree(nome_arquivo, nome_final_arquivo)
        

