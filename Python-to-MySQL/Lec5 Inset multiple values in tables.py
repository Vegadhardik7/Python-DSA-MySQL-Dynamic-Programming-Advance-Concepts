import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mousepad',
    port=3306,
    database='my_database1')

cur = mydb.cursor()

str2 = "INSERT INTO SCHOOL VALUES(%s,%s,%s)"

vals = [(102,'Jay','Lohar'),(103,'Shruti','Panchal'),(104,'Priya','Kadam')]

cur.executemany(str2, vals)
mydb.commit()