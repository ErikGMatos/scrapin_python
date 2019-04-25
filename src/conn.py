import pyodbc
server = '000.00.00.00'
database = 'db'
username = 'sa'
password = '123'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()

#select
cursor.execute('''
            select distinct  isnull(cctb.ativo,0)ativo, tb.*, isnull(cctb.percentualdesconto,0)percentualdesconto from pse.tipobolsa tb 
            left join pse.cursocaptacaotipobolsa cctb
            on tb.codtipobolsa = cctb.codtipobolsa and cctb.codcursocaptacaoperiodocaptacao = 5710
            left join pse.cursocaptacaoperiodocaptacao ccpc
            on cctb.codcursocaptacaoperiodocaptacao = ccpc.codcursocaptacaoperiodocaptacao
            ''')

#select
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

#insert
# cursor.execute('''
#                 INSERT INTO TabelaTeste(numero,nome)
#                 VALUES('1','Joao')
#             ''')
#cnxn.commit()

#fecha cursor e fecha conexao respectivamente
cursor.close()
cnxn.close()
