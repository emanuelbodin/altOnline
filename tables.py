import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)


# gustavs print
print("Gustavs test")

mycursor = mydb.cursor()

def tablesInit():
    mycursor.execute("CREATE TABLE IF NOT EXISTS departments (title varchar(255), description text(500), parentDepartment varchar(255), PRIMARY KEY (title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS products (title varchar(255), description text(500), price int(11), stock int(11), department varchar(255), FOREIGN KEY (department) REFERENCES departments(title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS orders (date datetime, status varchar(255), lastChange datetime, paymentReference varchar(255), trackingNumber varchar(255), user varchar(255))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS users (email varchar(255), password varchar(255), name varchar(255), address varchar(255), identityNo int(11), phone varchar(255), newsletter bit)")

tablesInit()