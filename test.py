import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="QBfSyKRd82",
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)