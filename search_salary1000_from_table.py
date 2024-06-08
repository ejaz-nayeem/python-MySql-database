import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="ejaz_db"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user_information where salary<1000")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
     
