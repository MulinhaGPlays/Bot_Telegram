import pandas as pd

tabela = pd.read_excel("Planilhas/P1.xlsx")

tabela.loc[tabela["Alocação"] == "CAIXA", "Quantid."] = tabela["Quantid."] * 3
tabela.loc[tabela["Alocação"] == "Unidade", "Tipo"] = "Uso Único"
tabela.loc[tabela["Alocação"] == "Unidade", "Quantid."] = 1

tabela.to_excel("Planilhas/P1_Alter.xlsx")