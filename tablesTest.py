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
    mycursor.execute("DROP TABLE IF EXISTS reviews")
    mycursor.execute("DROP TABLE IF EXISTS order_items")
    mycursor.execute("DROP TABLE IF EXISTS orders")
    mycursor.execute("DROP TABLE IF EXISTS users")
    mycursor.execute("DROP TABLE IF EXISTS products")
    mycursor.execute("DROP TABLE IF EXISTS departments")
    mycursor.execute("DROP TABLE IF EXISTS city_zip_code")

    
dropTables()

def tablesInit():
    mycursor.execute("CREATE TABLE IF NOT EXISTS departments (department_title varchar(255), description text(500), short_description text(50), breadcrumb varchar(255), parentDepartment varchar(255), PRIMARY KEY (department_title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS products (product_title varchar(255), breadcrumb varchar(255), short_description text(100), featured tinyint(1), hidden tinyint(1),  description text(500), price_without_tax int(11), tax_to_add int(11), discount int(11), stock int(11), department varchar(255), PRIMARY KEY (product_title), FOREIGN KEY (department) REFERENCES departments(department_title))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS city_zip_code (city varchar(255), zip_code varchar(255), PRIMARY KEY (city))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS users (email varchar(255), id_no int(11), password varchar(255), name varchar(255), street varchar(255), phone varchar(255), newsletter tinyint(1), city varchar(255), PRIMARY KEY (email), FOREIGN KEY (city) REFERENCES city_zip_code(city))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS orders (order_id int(11), tracking_id varchar(255), order_date datetime, order_status varchar(255), last_change_date datetime, payment_ref varchar(255), user_email varchar(255), PRIMARY KEY (order_id), FOREIGN KEY (user_email) REFERENCES users(email))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS order_items (related_product varchar(255), related_order int(11), quantity int(11), current_product_price int(11), current_product_discount int(11), current_product_tax int(11), CONSTRAINT PK_ORDERITEMS PRIMARY KEY (related_product, related_order), FOREIGN KEY (related_product) REFERENCES products(product_title), FOREIGN KEY (related_order) REFERENCES orders(order_id))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS reviews (review_product varchar(255), author_email varchar(255), score int(11), review_text text(100), CONSTRAINT PK_REVIEWS PRIMARY KEY (review_product, author_email), FOREIGN KEY (review_product) REFERENCES products(product_title), FOREIGN KEY (author_email) REFERENCES users(email))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS homepage (logo varchar(255), welcome_text text(500))")
    mycursor.execute("CREATE TABLE IF NOT EXISTS product_keywords (related_product varchar(255), keyword varchar(255), CONSTRAINT KW_REVIEWS PRIMARY KEY (related_product, keyword))")



tablesInit()