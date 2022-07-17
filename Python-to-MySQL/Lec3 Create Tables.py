import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mousepad',
    port=3306,
    database='my_database1')

cur = mydb.cursor()

str1 = "CREATE TABLE SCHOOL(Stu_id int(10), Stu_fname varchar(10), Stu_lname varchar(10))"

cur.execute(str1)

