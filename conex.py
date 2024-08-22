import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="escola"
)

def view_data(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()

def send_data(query):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    mydb.commit()