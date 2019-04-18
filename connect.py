import pyodbc

#define sql connection
ariconn_str = "DRIVER={ODBC Driver 13 for SQL Server};SERVER=your server ip;DATABASE=your database name;UID=username;PWD=password"
ariconn = pyodbc.connect(ariconn_str)
aricur = ariconn.cursor()

#execute sql
table_name = 'test'
sql = '''SELECT * FROM '''+ table_name 
aricur.execute(sql)
row = aricur.fetchall()

#print data
for i in row:
    print(i)

aricur.commit()     

#close connection
aricur.close()
ariconn.close()