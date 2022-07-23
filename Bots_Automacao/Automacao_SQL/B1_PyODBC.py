import pyodbc

conexao = pyodbc.connect("Driver={SQL Server};" 
                         "Server=.\FILAUPE;" 
                         "Database=BD1_PyODBC;" 
                         "Trusted_Connection=yes;")

cursor = conexao.cursor()
cursor.execute("SELECT * FROM Vendas")












MostrarTabela = cursor.fetchone()
print(MostrarTabela)

