import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)

mycursor = mydb.cursor()

def dropTables():
    mycursor.execute("DROP TABLE reviews")
    mycursor.execute("DROP TABLE users")
    mycursor.execute("DROP TABLE order_items")
    mycursor.execute("DROP TABLE orders")
    mycursor.execute("DROP TABLE products")
    mycursor.execute("DROP TABLE departments")
    mycursor.execute("DROP TABLE city_zip_code")

    
dropTables()