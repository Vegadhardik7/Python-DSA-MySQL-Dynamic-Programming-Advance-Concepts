import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mousepad',
    port=3306,
    database='my_database1')

cur = mydb.cursor()

s = "UPDATE SCHOOL SET Stu_id=Stu_id+1 WHERE Stu_id>102"

cur.execute(s)
mydb.commit()