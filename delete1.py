import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="ejaz_db"
)

mycursor = mydb.cursor()

sql = "DELETE FROM user_information WHERE salary = '45'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
