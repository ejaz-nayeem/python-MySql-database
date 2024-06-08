import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="world"
)

mycursor = mydb.cursor()
q= """
    SELECT city.CountryCode, country.Code, city.Population

    FROM city
    INNER JOIN country ON city.CountryCode = country.Code AND city.Population
   """ 

mycursor.execute(q)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
     
