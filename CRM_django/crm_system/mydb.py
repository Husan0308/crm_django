import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="root",
    password="password123"
)

cursorObject = conn.cursor()

cursorObject.execute("CREATE DATABASE husancoder")

print("All Done!")