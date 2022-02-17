#!C:\Python39\python.exe
print("Content-Type: text/html\n\n")

import mysql.connector
import cgi

# Get all form data
form = cgi.FieldStorage()

#extract required data
name = form.getvalue('name')
email = form.getvalue('email')



# Mysql Credentials
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = mydb.cursor()

# Query
sql = "INSERT INTO formdata (name, email) VALUES (%s, %s)"
val = (name, email)

# Run Query
mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record inserted.")
