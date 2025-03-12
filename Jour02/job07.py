import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"

)

if conn.is_connected():
    print("Connexion réussie!")
   
cursor = conn.cursor()

query = "SELECT * FROM service"
cursor.execute(query)

result = cursor.fetchone()
service = result[0]

print(f"Le service est : {service}")

conn.close()
