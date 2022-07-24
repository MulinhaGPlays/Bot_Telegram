from unicodedata import name
from colorama import Cursor
from numpy import insert
import pyodbc


BancoDados = 'BD1_PyODBC'
ServerName = '.\FILAUPE'
driver = 'SQL Server'

Driver = '{' + f"{driver}" + '}'

conexao = pyodbc.connect(f'DRIVER={Driver};'
                         f'SERVER={ServerName};'
                         f'DATABASE={BancoDados};'
                         f'Trusted_Connection=yes')
cursor = conexao.cursor()
print("""Conexão com o banco de dados realizada com sucesso!
                  Bem vindo ao PyODBC!""")

def CreateTable(name):
      print("""Os tipos de dados disponíveis são: 
             1 - INT
             2 - VARCHAR(100)
             3 - DATETIME
             4 - DECIMAL(5, 2)
             5 - BIT
             6 - FLOAT
             7 - DOUBLE
             8 - SMALLINT
             9 - TINYINT
             10 - BIGINT
             11 - REAL
             12 - NUMERIC(10, 5)
             13 - MONEY(10,2)
             14 - DATE
             15 - TIME
             16 - DATETIME2
             17 - DATETIMEOFFSET
             18 - NTEXT
             19 - TEXT
             20 - VARBINARY
             21 - IMAGE
             22 - UNIQUEIDENTIFIER
             23 - SQL_VARIANT
             24 - XML""")
      fieldsBase = input('Insira os campos da tabela separados por "," e o número do tipo ao lado Ex:Batata2 : ')
      TypesC = ['INT', 'VARCHAR', 'DATETIME', 'DECIMAL', 'BIT', 'FLOAT', 'DOUBLE', 'SMALLINT', 'TINYINT', 'BIGINT', 'REAL', 'NUMERIC', 'MONEY',
                'DATE', 'TIME', 'DATETIME2', 'DATETIMEOFFSET', 'NTEXT', 'TEXT', 'VARBINARY', 'IMAGE', 'UNIQUEIDENTIFIER', 'SQL_VARIANT', 'XML']
      fieldsTemp = fieldsBase.split(',')
      fieldsName = fieldsBase.split(',')
      fieldsType = []
      n = 0
      for word in fieldsTemp:
            for letter in fieldsTemp[n]:
                  if letter.isnumeric():
                        fieldsType.append(TypesC[int(letter) - 1])
                        fieldsName[n] = fieldsName[n].split(f'{fieldsTemp[n]}')[0]
                        break
                  else:
                        fieldsTemp[n] = fieldsTemp[n].replace(letter, "")
            n += 1
      fields = ''
      for i in range(len(fieldsName)):
            fields += f"{fieldsName[i]} {fieldsType[i]}, "
      fields = fields[:-2]
      cursor.execute(f'CREATE TABLE {name} ({fields})')
      conexao.commit()
      print(f'Tabela {name} criada com sucesso!')
      return name

CreateTable(input('Insira o nome da tabela: '))

# cursor.execute(f"SELECT * FROM {CreateTable(input('Insira o nome da tabela: '))}")
# MostrarTabela = cursor.fetchone()
# print(MostrarTabela)
