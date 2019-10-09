import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  port=8888,
  database="altOnline"
)

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO homepage(logo, welcome_text) values(null, 'Välkommen')")

