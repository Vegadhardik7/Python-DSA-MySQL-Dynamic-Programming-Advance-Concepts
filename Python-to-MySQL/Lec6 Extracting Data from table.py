import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mousepad',
    port=3306,
    database='my_database1')

cur = mydb.cursor()

str1 = "select * from school"

cur.execute(str1)
result = cur.fetchall()

for i in result:
    print(i)