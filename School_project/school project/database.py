import mysql.connector

db = mysql.connector.connect(user='root', password='1234')
cursor = db.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS school")
cursor.execute("USE school")
cursor.execute("""CREATE TABLE IF NOT EXISTS studentdata(
        studentId int primary key,
        firstname text,
        lastname text,
        rollno int,
        std text,
        section text,
        gender text,
        address text,
        dob date
        )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS parentinfo(
        studentId int primary key,
        fatherName text,
        fatherNo int,
        fatherProfession text,
        motherName text,
        motherNo int,
        motherProfession text
        )""")


db.commit()