import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mousepad',
    port=3306,
    database='my_database1')

cur = mydb.cursor()

str2 = "INSERT INTO SCHOOL VALUES(%s,%s,%s)"

s1 = (101,'Ram','Jain')

cur.execute(str2,s1)

mydb.commit()