import mysql.connector
from mysql.connector import Error

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
