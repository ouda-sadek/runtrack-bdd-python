import mysql.connector
conn = mysql.connector.connect(
    host= "localhost",
    user = "root",
    password = "",
    database = "LaPlateforme"
)

if conn.is_connected():
    print("Connexion réussie!")
cursor = conn.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)
salles = cursor.fetchall()
print("Noms et capacité des salles : ")
for salle in salles:
    print(f"Nom : {salle[0]}, Capacité : {salle[1]}")

conn.close()
print("Connexion fermée!")

