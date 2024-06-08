import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="ejaz_db"
)

mycursor = mydb.cursor()

sql = "INSERT user_information (user_name, salary) VALUES (%s, %s)"
val = ("John7", "1000")
#sql2 = "INSERT user_information (user_name, salary) VALUES (%s, %s)"
#val2 = ("John4", "1000")
mycursor.execute(sql, val)
#mycursor.execute(sql2, val2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
