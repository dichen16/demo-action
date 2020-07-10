import psycopg2

try:
    conn = psycopg2.connect(host="localhost",database="mydb", user="test", password="test", port='5432')
    print("connected!!!")
except:
    print("I am unable to connect to the database")
