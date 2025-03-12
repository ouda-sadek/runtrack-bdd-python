import mysql.connector
from datetime import datetime

class Zoo:
    def __init__(self, host, user, password, database):
        # Connexion à la base de données
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    # Ajouter une cage
    def add_cage(self, superficie, capacite_max):
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        values = (superficie, capacite_max)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Supprimer une cage
    def delete_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (id_cage,))
        self.connection.commit()

    # Ajouter un animal
    def add_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Supprimer un animal
    def delete_animal(self, id_animal):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (id_animal,))
        self.connection.commit()

    # Modifier un animal
    def update_animal(self, id_animal, nom=None, race=None, id_cage=None, date_naissance=None, pays_origine=None):
        query = "UPDATE animal SET nom = COALESCE(%s, nom), race = COALESCE(%s, race), id_cage = COALESCE(%s, id_cage), date_naissance = COALESCE(%s, date_naissance), pays_origine = COALESCE(%s, pays_origine) WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id_animal)
        self.cursor.execute(query, values)
        self.connection.commit()

    # Afficher tous les animaux
    def show_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animals = self.cursor.fetchall()
        for animal in animals:
            print(f"ID: {animal[0]}, Nom: {animal[1]}, Race: {animal[2]}, Cage ID: {animal[3]}, Date Naissance: {animal[4]}, Pays Origine: {animal[5]}")

    # Afficher les animaux par cage
    def show_animals_in_cages(self):
        query = """
        SELECT c.id, c.superficie, a.nom, a.race
        FROM cage c
        LEFT JOIN animal a ON c.id = a.id_cage
        """
        self.cursor.execute(query)
        cages = self.cursor.fetchall()
        for cage in cages:
            print(f"Cage ID: {cage[0]}, Superficie: {cage[1]} m2")
            if cage[2]:
                print(f"  - Animal: {cage[2]}, Race: {cage[3]}")
            else:
                print("  - No animals in this cage")

    # Calculer la superficie totale des cages
    def calculate_total_area(self):
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0]

    # Fermer la connexion
    def close(self):
        self.cursor.close()
        self.connection.close()

# Exemple d'utilisation de la classe
if __name__ == "__main__":
    # Connexion à la base de données
    zoo = Zoo(host="localhost", user="root", password="", database="zoo")

    # Ajouter une cage
    zoo.add_cage(120, 25)

    # Ajouter un animal
    zoo.add_animal('Zebra', 'Equus zebra', 1, '2017-03-10', 'Kenya')

    # Afficher tous les animaux
    print("Liste des animaux dans le zoo:")
    zoo.show_animals()

    # Afficher les animaux dans chaque cage
    print("\nListe des animaux par cage:")
    zoo.show_animals_in_cages()

    # Calculer la superficie totale des cages
    total_area = zoo.calculate_total_area()
    print(f"\nLa superficie totale des cages est de {total_area} m2")

    # Modifier un animal
    zoo.update_animal(1, nom="Lion Modifié", race="Panthera leo modifié")

    # Supprimer un animal
    zoo.delete_animal(2)

    # Supprimer une cage
    zoo.delete_cage(2)

    # Fermer la connexion à la base de données
    zoo.close()

    # result 
    """Liste des animaux dans le zoo:
    ID: 1, Nom: Lion, Race: Panthera leo, Cage ID: 1, Date Naissance: 2015-06-01, Pays Origine: Kenya
    ID: 2, Nom: Elephant, Race: Loxodonta, Cage ID: 2, Date Naissance: 2010-03-15, Pays Origine: Tanzania
    ID: 3, Nom: Giraffe, Race: Giraffa camelopardalis, Cage ID: 3, Date Naissance: 2018-09-12, Pays Origine: South Africa
    ID: 4, Nom: Zebra, Race: Equus zebra, Cage ID: 1, Date Naissance: 2017-03-10, Pays Origine: Kenya

    Liste des animaux par cage:
    Cage ID: 1, Superficie: 50 m2
    - Animal: Zebra, Race: Equus zebra
    Cage ID: 1, Superficie: 50 m2
    - Animal: Lion, Race: Panthera leo
    Cage ID: 2, Superficie: 100 m2
    - Animal: Elephant, Race: Loxodonta
    Cage ID: 3, Superficie: 75 m2
    - Animal: Giraffe, Race: Giraffa camelopardalis
    Cage ID: 4, Superficie: 120 m2
    - No animals in this cage

    La superficie totale des cages est de 345 m2"""
