import mysql.connector
from mysql.connector import Error


# Paramètres de connexion à la base de données
host = "localhost"  # ou l'adresse IP du serveur MySQL si ce n'est pas local
user = "root"  # remplace par ton nom d'utilisateur
password = ""  # remplace par ton mot de passe
database = "LaPlateforme"  # nom de la base de données

try:
    # database connection
    connection = mysql.connector.connect(
        host = "localhost",        
        database = "LaPlateforme",  
        user = "root", 
        password = "" 
    )

    if connection.is_connected():
        print("Connexion réussie!")
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        # Run the query to retrieve all students
        cursor.execute("SELECT * FROM etudiant")
        # Retrieve all results
        resultats = cursor.fetchall()

        # Show results
        print("Liste des étudiants :")
        for etudiant in resultats:
            print(etudiant)

except Error as e:
    print(f"Erreur: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("La connexion MySQL est fermée")

# result
"""Connexion réussie!
Liste des étudiants :
(1, 'Spaghetti', 'Betty', 20, 'betty.Spaghetti@laplateforme.io')
(2, 'Steak', 'Chuck', 45, 'chuck.steak@laplateforme.io')
(4, 'Barnes', 'Binkie', 16, 'binkie.barnes@laplateforme.io')
(5, 'Dupuis', 'Gertrude', 20, 'gertrude.dupuis@laplateforme.io')
(11, 'Dupuis', 'Martin', 18, 'martin.dupuis@laplateforme.io')
La connexion MySQL est fermée"""
