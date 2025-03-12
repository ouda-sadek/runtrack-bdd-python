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

query = "SELECT SUM(superficie) AS total_superficie FROM etage"
cursor.execute(query)

result = cursor.fetchone()
total_superficie = result[0]

print(f"La superficie totale des étages est de {total_superficie} m².")


cursor.close()
conn.close()

