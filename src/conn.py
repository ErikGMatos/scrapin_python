import pyodbc 
server = '172.16.10.50' 
database = 'CaptacaoConversaoGraduacao' 
username = 'sa' 
password = 'homologacao' 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('''
            select distinct  isnull(cctb.ativo,0)ativo, tb.*, isnull(cctb.percentualdesconto,0)percentualdesconto from pse.tipobolsa tb 
            left join pse.cursocaptacaotipobolsa cctb
            on tb.codtipobolsa = cctb.codtipobolsa and cctb.codcursocaptacaoperiodocaptacao = 5710
            left join pse.cursocaptacaoperiodocaptacao ccpc
            on cctb.codcursocaptacaoperiodocaptacao = ccpc.codcursocaptacaoperiodocaptacao
            ''')
             
row = cursor.fetchone() 
while row: 
    print(row) 
    row = cursor.fetchone()

cursor.close()
cnxn.close() 