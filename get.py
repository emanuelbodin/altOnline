import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)

mycursor = mydb.cursor()

def getDepartments():
    mycursor.execute("Select * from departments")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)


getDepartments()
