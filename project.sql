DROP TABLE IF EXISTS product_keywords;
DROP TABLE IF EXISTS homepage;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS departments;
DROP TABLE IF EXISTS city_zip_code;

CREATE TABLE IF NOT EXISTS departments (department_title varchar(255), description text(500), short_description text(50), breadcrumb varchar(255), parentDepartment varchar(255), PRIMARY KEY (department_title));
CREATE TABLE IF NOT EXISTS products (product_title varchar(255), short_description text(500), breadcrumb varchar(255), featured tinyint(1) default 0, hidden tinyint(1) default 0, description text(500), price_without_tax int(11), tax_to_add int(11), discount int(11) default 0, stock int(11), department varchar(255), PRIMARY KEY (product_title), FOREIGN KEY (department) REFERENCES departments(department_title));
CREATE TABLE IF NOT EXISTS city_zip_code (city varchar(255), zip_code varchar(255), PRIMARY KEY (city));
CREATE TABLE IF NOT EXISTS users (email varchar(255), id_no int(11), password varchar(255), name varchar(255), street varchar(255), phone varchar(255), newsletter tinyint(1) default 0, city varchar(255), PRIMARY KEY (email), FOREIGN KEY (city) REFERENCES city_zip_code(city));
CREATE TABLE IF NOT EXISTS orders (order_id int(11), tracking_id varchar(255), order_date datetime, order_status varchar(255), last_change_date datetime, payment_ref varchar(255), user_email varchar(255), PRIMARY KEY (order_id), FOREIGN KEY (user_email) REFERENCES users(email));
CREATE TABLE IF NOT EXISTS order_items (related_product varchar(255), related_order int(11), quantity int(11), current_product_price int(11), current_product_discount int(11), current_product_tax int(11), CONSTRAINT PK_ORDERITEMS PRIMARY KEY (related_product, related_order), FOREIGN KEY (related_product) REFERENCES products(product_title), FOREIGN KEY (related_order) REFERENCES orders(order_id));
CREATE TABLE IF NOT EXISTS reviews (review_product varchar(255), author_email varchar(255), score int(11), review_text text(100), CONSTRAINT PK_REVIEWS PRIMARY KEY (review_product, author_email), FOREIGN KEY (review_product) REFERENCES products(product_title), FOREIGN KEY(author_email) REFERENCES users(email));
CREATE TABLE IF NOT EXISTS homepage (logo varchar(255), welcome_text text(500));
CREATE TABLE IF NOT EXISTS product_keywords (related_product varchar(255), keyword varchar(255), CONSTRAINT KW_REVIEWS PRIMARY KEY (related_product, keyword), FOREIGN KEY (related_product) REFERENCES products(product_title));

INSERT INTO departments(department_title, description, short_description, breadcrumb, parentDepartment) VALUES('IT Department', 'IT support', 'Fixes all the sweet IT problems', '/IT/', NULL);
INSERT INTO departments(department_title, description, parentDepartment) VALUES('IPads', 'Sells IPads', 'IT Department');
INSERT INTO departments(department_title, description, parentDepartment) VALUES('Gaming Computers', 'Sells Gaming Computers', 'IT Department');
INSERT INTO departments(department_title, description, parentDepartment) VALUES('Laptops', 'Sells laptops', 'IT Department');
INSERT INTO departments(department_title, description, short_description, breadcrumb, parentDepartment) VALUES('PR Department', 'Media and graphics', 'Does all the hard marketing for your products', '/PR/',  NULL);
INSERT INTO departments(department_title, description, parentDepartment) VALUES('Movies', 'Sells Movies', 'PR Department');
INSERT INTO departments(department_title, description, parentDepartment) VALUES('Pictures', 'Sells Pictures', 'PR Department');
INSERT INTO departments(department_title, description, parentDepartment) VALUES('Flyers', 'Sells Flyers', 'PR Department');


INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('IPad 7', 'Super awesome IPad', 1000, 38, 10,  3, 'IPads');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('IPad 8', 'Super awesome IPad', 2000, 38, 11, 50, 'IPads');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('IPad 9', 'Super awesome IPad', 3000, 38, 12, 6, 'IPads');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('IPad 10', 'Super awesome IPad', 4000, 38, 0, 564, 'IPads');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('TOSHIBA', 'Super awesome TOSHIBA', 6000, 39, 99, 34, 'Laptops');
INSERT INTO products(product_title, featured, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('Mona Lisa', 1,  'The real painting of Mona Lisa', 9999999, 10, 0,  1, 'Pictures');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('Rocketman', 'Movie about Elton John', 100, 25, 30, 14, 'Movies');
INSERT INTO products(product_title, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('DELL HYPER GAMING COMPUTER', 'Best gaming computer on the market right now', 10000, 10, 80, 4, 'Gaming Computers');
INSERT INTO products(product_title, featured, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('Random flyer', 1,  'Superfly', 106, 50, 0, 10000, 'Flyers');
INSERT INTO products(product_title, featured, description, price_without_tax, tax_to_add, discount, stock, department) VALUES('IPad XXX', 1, 'Super awesome IPadXXX', 100088, 38, 0, 90, 'IPads');

INSERT INTO city_zip_code(city, zip_code) VALUES ('UPPSALA', 75431);
INSERT INTO users (email, id_no, password, name, street, phone, city) VALUES ('hampan@hampmail.com', 123456789, 'pwdpwd', 'hampan', 'regngatan 21', 0701234567, 'UPPSALA');
INSERT INTO users (email, id_no, password, name, street, phone, city) VALUES ('manne@mannmail.com', 987654321, 'pwdpwd', 'manne', 'solgatan 21', 0703457812, 'UPPSALA');

INSERT INTO reviews(review_product, author_email, score, review_text) VALUES ('IPad 7', 'hampan@hampmail.com', 5, 'Very good product, much happiness');
INSERT INTO reviews(review_product, author_email, score, review_text) VALUES ('IPad 7', 'manne@mannmail.com', 1, 'Very bad product, much sadness');

INSERT INTO orders (order_id, tracking_id, order_date, order_status, last_change_date, payment_ref, user_email) VALUES (12, 131535, '2019-10-09', 'Delivered', '2019-09-10', 124145, 'hampan@hampmail.com');
INSERT INTO order_items (related_product, related_order, quantity, current_product_price, current_product_discount, current_product_tax) VALUES ('IPad 8', 12, 2, 2000, 0, 38);

INSERT INTO homepage (logo, welcome_text) VALUES (NULL, 'Welcome to altOnline!');

INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad 7', 'Apple');
INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad 7', 'IPad');
INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad 8', 'Apple');
INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad 9', 'Apple');
INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad 10', 'Apple');
INSERT INTO product_keywords (related_product, keyword) VALUES ('IPad XXX', 'IPad');
INSERT INTO product_keywords (related_product, keyword) VALUES ('Rocketman', 'Elton John');

SELECT * FROM departments;
SELECT * FROM products;
SELECT * FROM users;
SELECT * FROM city_zip_code;
SELECT * FROM reviews;
SELECT * FROM orders;
SELECT * FROM order_items;
SELECT * FROM homepage;
SELECT * FROM product_keywords;

SELECT welcome_text FROM homepage LIMIT 1;
SELECT department_title, short_description, breadcrumb FROM departments WHERE parentDepartment IS NULL;
SELECT product_title, description, price_without_tax, tax_to_add, discount, breadcrumb FROM products WHERE featured = 1;
SELECT * FROM product_keywords WHERE related_product = 'IPad 7';

SELECT DISTINCT product_title FROM products, product_keywords WHERE product_title = related_product AND keyword IN (SELECT keyword FROM product_keywords WHERE related_product = 'IPad 7');
SELECT * FROM (SELECT * FROM products WHERE department = 'IPads') a LEFT JOIN (SELECT review_product, AVG(score) FROM reviews) b ON product_title = review_product;
EXPLAIN SELECT * FROM products WHERE discount > 0 ORDER BY discount DESC;

CREATE INDEX department_name ON products(department);