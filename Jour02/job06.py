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

query = "SELECT SUM(capacite) AS capacite_total FROM salle"
cursor.execute(query)

result = cursor.fetchone()
capacite_total = result[0]

print(f"La capacité de toute les salles est de {capacite_total} personnes")


cursor.close()
conn.close()
print("Connexion fermée!")