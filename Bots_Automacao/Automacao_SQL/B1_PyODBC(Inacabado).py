import pyodbc
import time

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

class Table:
      def CreateTable(self, name):
            self.name = name
            TypesC = ['int', 'VARCHAR', 'DATETIME', 'DECIMAL', 'BIT', 'FLOAT', 'DOUBLE', 'SMALLINT', 'TINYINT', 'BIGINT', 'REAL', 'NUMERIC', 'MONEY',
                      'DATE', 'TIME', 'DATETIME2', 'DATETIMEOFFSET', 'NTEXT', 'TEXT', 'VARBINARY', 'IMAGE', 'UNIQUEIDENTIFIER', 'SQL_VARIANT', 'XML']
            print(f'\nCriando a tabela {name}...')
            print('Os tipos de dados disponíveis são:')
            for i in range(len(TypesC)):
                  time.sleep(0.125)
                  print(f"""{i+1} - {TypesC[i]}""")
            fieldsBase = input('Insira os campos da tabela separados por "," e o número do tipo ao lado Ex:Batata2 : ')
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
            self.fields = fields
            cursor.execute(f'CREATE TABLE {name} ({fields})')
            conexao.commit()
            print(f'Tabela {name} criada com sucesso!')

Table.CreateTable(Table, input('Insira o nome da tabela: '))

cursor.execute(f"SELECT * FROM {Table.name}")
MostrarTabela = cursor.fetchone()
print(MostrarTabela)
