import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="world"
)

mycursor = mydb.cursor()
x=input()

#mycursor.execute("SELECT * FROM city where CountryCode= ",'x')
#mycursor.execute(f"SELECT * FROM city where CountryCode='{x}'")

    
#myresult = mycursor.fetchall()
mycursor.execute(f"SELECT * FROM city WHERE CountryCode = '{x}'")
myresult = mycursor.fetchall()

if mycursor.rowcount == 0:
    print("Invalid country code")
else:
    for row in myresult:
        print(row)

     
