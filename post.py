import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)

mycursor = mydb.cursor()

def insertDepartment(title, description, parent):
    sql = "INSERT INTO departments (title, description, parentDepartment) VALUES (%s, %s, %s)"
    val = (title, description, parent)
    mycursor.execute(sql,val)
    mydb.commit()

def insertProduct(title, description, price, stock, department):
  sql = "INSERT INTO products (title, description, price, stock, department) VALUES (%s, %s, %s, %s, %s)"
  val = (title, description, price, stock, department)
  mycursor.execute(sql,val)
  mydb.commit()

def initTables():
  insertDepartment("electronics", "Electronic stuff", None)
  insertDepartment("computers", "Computer stuff", "electronics")
  insertDepartment("phones", "phones", "electronics")
  insertDepartment("tablets", "phones", "electronics")
  insertDepartment("furniture", "Furniture", None)
  insertDepartment("tables", "Tables", "furniture")
  insertDepartment("chairs", "Chairs", "furniture")
  insertDepartment("beds", "Beds", "furniture")

def initProducts():
  insertProduct("Macbook", "Macbook from apple", 900, 100, "computers")


#initTables()
#initProducts()

