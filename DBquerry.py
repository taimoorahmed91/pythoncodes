import mysql.connector

mydb = mysql.connector.connect(
    host="130.211.216.63",
    user="root",
    password="taimoor1991",
    database="firepower"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM access")


#myresult = mycursor.fetchone()

records = mycursor.fetchall()
for row in records:
    name = row["name"]

    print(id)
