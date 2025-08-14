import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',database='db')
cursor = conn.cursor()

b=input()
s=input()
x=f'update products set prices = {s} where {b}'
cursor.execute(x)