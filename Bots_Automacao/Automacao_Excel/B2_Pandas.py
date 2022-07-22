import os # Importa o módulo os para acesso aos sistema operacional
from pathlib import Path # importando o módulo pathlib para trabalhar com caminhos
import pandas as pd # Importando o Pandas para manipulação de arquivos Excel

caminho= Path.cwd()/"Bots_Automacao/Automacao_Excel/Dados/Vendas" # Caminho do arquivo Excel

vendas = pd.DataFrame(columns=['Loja','Vendedor','Valor da Venda']) # Criação de uma tabela vazia

for pasta in caminho.iterdir(): # Percorre todas as pastas do caminho
    if pasta.is_dir(): # Verifica se a pasta é um diretório
        os.chdir(pasta) # Abre caso for um diretório
        caminho= Path.cwd() # Caminho do arquivo Excel
        for pasta in caminho.iterdir(): # Percorre todas as pastas do caminho
            if pasta.is_dir(): # Verifica se a pasta é um diretório
                os.chdir(pasta) # Abre caso for um diretório
                caminho= Path.cwd() # Caminho do arquivo Excel
                for pasta in caminho.iterdir(): # Percorre todas as pastas do caminho
                    if pasta.is_dir(): # Verifica se a pasta é um diretório
                        os.chdir(pasta) # Abre caso for um diretório
                        caminho= Path.cwd() # Caminho do arquivo Excel
                        for arquivo in caminho.iterdir(): # Percorre todos os arquivos da pasta
                            venda = pd.read_excel(arquivo) # Leitura do arquivo Excel
                            vendas = vendas.append(venda,ignore_index=True) # Adiciona a tabela ao DataFrame

os.chdir(caminho/"../../../../../") # Volta ao diretório anterior
vendas.to_excel("Planilhas/1_Dados_Vendas_AlterPandas.xlsx") # Salva o arquivo Excel