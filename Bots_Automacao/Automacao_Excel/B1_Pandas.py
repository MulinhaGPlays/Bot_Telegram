import pandas as pd # Importando o Pandas para manipulação de arquivos Excel

tabela = pd.read_excel("Planilhas/P1.xlsx") # Leitura do arquivo Excel

tabela.loc[tabela["Alocação"] == "CAIXA", "Quantid."] = tabela["Quantid."] * 3 # Alteração de valores na tabela com base em uma condição
tabela.loc[tabela["Alocação"] == "Unidade", "Tipo"] = "Uso Único" # Alteração de valores 
tabela.loc[tabela["Alocação"] == "Unidade", "Quantid."] = 1 # Alteração de valores

tabela.to_excel("Planilhas/P1_AlterPandas.xlsx") # Salvar alteraçõe no arquivo Excel ou criar um novo arquivo