import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server Native Client 10.0};SERVER=localhost;DATABASE=ED;UID=kth;PWD=pass')

cursor = cnxn.cursor()

cursor.execute("select Job_Title from dbo.Contact")

row = cursor.fetchone()
if row:
    print(row)


