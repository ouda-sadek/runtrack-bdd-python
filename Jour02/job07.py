"""import mysql.connector

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

conn.close()"""
import mysql.connector

class Employe:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    # CREATE: Ajouter un employé
    def add_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.connection.commit()

    # READ: Récupérer tous les employés dont le salaire est supérieur à 3000 €
    def get_employes_salaire_superieur(self, salaire_min):
        query = "SELECT * FROM employe WHERE salaire > %s"
        self.cursor.execute(query, (salaire_min,))
        result = self.cursor.fetchall()
        return result

    # UPDATE: Mettre à jour le salaire d'un employé
    def update_salaire(self, employe_id, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (nouveau_salaire, employe_id))
        self.connection.commit()

    # DELETE: Supprimer un employé
    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (employe_id,))
        self.connection.commit()

    # Récupérer tous les employés et leur service respectif
    def get_employes_services(self):
        query = """
            SELECT e.nom, e.prenom, e.salaire, s.nom AS service
            FROM employe e
            JOIN service s ON e.id_service = s.id
        """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    # Fermer la connexion
    def close(self):
        self.cursor.close()
        self.connection.close()


# Exemple d'utilisation de la classe
if __name__ == "__main__":
    # Connexion à la base de données
    db = Employe(host="localhost", user="root", password="", database="entreprise")

    # Ajouter un employé
    db.add_employe("Cohen", "Marc", 3200, 1)

    # Récupérer les employés dont le salaire est supérieur à 3000 €
    employes = db.get_employes_salaire_superieur(3000)
    print("Employés avec un salaire > 3000€ :")
    for employe in employes:
        print(employe)

    # Mettre à jour le salaire d'un employé
    db.update_salaire(1, 3600)

    # Récupérer tous les employés et leurs services
    employes_services = db.get_employes_services()
    print("\nTous les employés avec leurs services :")
    for employe in employes_services:
        print(f"{employe[0]} {employe[1]} - {employe[3]} (Salaire: {employe[2]}€)")

    # Supprimer un employé
    db.delete_employe(5)

    # Fermer la connexion
    db.close()

    # result
    """Employés avec un salaire > 3000€ :
    (1, 'Dupont', 'Pierre', Decimal('3500.00'), 1)
    (3, 'Lemoine', 'Claire', Decimal('4000.00'), 3)
    (5, 'Lemoine', 'Jean', Decimal('5000.00'), 3)
    (6, 'Cohen', 'Marc', Decimal('3200.00'), 1)

    Tous les employés avec leurs services :
    Dupont Pierre - Informatique (Salaire: 3600.00€)
    Martin Paul - Ressources humaines (Salaire: 2500.00€)
    Lemoine Claire - Marketing (Salaire: 4000.00€)
    Durand Sophie - Informatique (Salaire: 2800.00€)
    Lemoine Jean - Marketing (Salaire: 5000.00€)
    Cohen Marc - Informatique (Salaire: 3200.00€)"""
