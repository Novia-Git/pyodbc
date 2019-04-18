import pyodbc

#define sql connection
conn_str = "DRIVER={ODBC Driver 13 for SQL Server};SERVER=your server ip;DATABASE=your database name;UID=username;PWD=password"
conn = pyodbc.connect(conn_str)
cur = ariconn.cursor()

#execute sql
table_name = 'test'
sql = '''SELECT * FROM '''+ table_name 
cur.execute(sql)
row = cur.fetchall()

#print data
for i in row:
    print(i)

cur.commit()     

#close connection
cur.close()
conn.close()
