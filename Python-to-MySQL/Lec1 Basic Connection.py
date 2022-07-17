import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',password='mousepad',port=3306)

print(mydb.connection_id)