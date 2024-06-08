import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0987654321",
  database="world"
)

mycursor = mydb.cursor()
x=input()

q= f"""
    SELECT city.CountryCode, city.Population, country.Name, country.Continent

    FROM city
    INNER JOIN country ON city.CountryCode = country.Code AND city.Population WHERE city.Name='{x}'
   """ 

mycursor.execute(q)

myresult = mycursor.fetchall()

if mycursor.rowcount == 0:
    print("Invalid country name")
else:
    for x in myresult:
        print(x)


     
