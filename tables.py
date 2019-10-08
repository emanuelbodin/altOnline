import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8889,
  database="altOnline"
)

mycursor = mydb.cursor()

def tablesInit():
    mycursor.execute("CREATE TABLE IF NOT EXISTS departments (title varchar(255), description text(500), short_description text(50), breadcrumb varchar(255), parentDepartment varchar(255), PRIMARY KEY (title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS products (title varchar(255), breadcrumb varchar(255),  description text(500), price_without_tax int(11), tax_to_add int(11), discount int(11), stock int(11), department varchar(255), FOREIGN KEY (department) REFERENCES departments(title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS city_zip_code (city varchar(255), zip_code varchar(255), PRIMARY KEY (city))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS users (email varchar(255), id_no int(11), password varchar(255), name varchar(255), street varchar(255), phone varchar(255), newsletter bit, city varchar(255), PRIMARY KEY (email), FOREIGN KEY (city) REFERENCES city_zip_code(city))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id int(11), tracking_id varchar(255), order_date datetime, order_status varchar(255), last_change_date datetime, payment_ref varchar(255),  user_email varchar(255))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS order_items (product_title varchar(255), orderID int(11), quantity int(11), current_prodyct_price int(11), current_product_discount int(11), current_product_tax int(11), CONSTRAINT PK_ORDERITEMS PRIMARY KEY (product_title, orderID), FOREIGN KEY (product_title) REFERENCES products(title), FOREIGN KEY (orderID) REFERENCES orders(order_id))")
    #mycursor.execute("CREATE TABLE IF NOT EXISTS reviews (product_title varchar(255), email varchar(255), score int(11), review_text text(100), CONSTRAINT PK_REVIEWS PRIMARY KEY (product_title, email), FOREIGN KEY (product_title) REFERENCES products(title))")

tablesInit()