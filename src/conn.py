import pyodbc 
server = '000.00.00.00' 
database = 'db' 
username = 'sa' 
password = '123' 
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT * from pse.cursocaptacao") 
row = cursor.fetchone() 
while row: 
    print(row) 
    row = cursor.fetchone()

cursor.close()
cnxn.close() 