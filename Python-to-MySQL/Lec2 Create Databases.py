import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='mousepad',port=3306)

cur = mydb.cursor()

cur.execute("CREATE DATABASE my_database1")