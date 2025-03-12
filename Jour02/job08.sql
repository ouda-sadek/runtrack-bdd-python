mysql> CREATE DATABASE zoo;
Query OK, 1 row affected (0.08 sec)

mysql> USE zoo;
Database changed
mysql> CREATE TABLE cage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     superficie INT,
    ->     capacite_max INT
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> CREATE TABLE animal (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     race VARCHAR(255),
    ->     id_cage INT,
    ->     date_naissance DATE,
    ->     pays_origine VARCHAR(255),
    ->     FOREIGN KEY (id_cage) REFERENCES cage(id)
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> INSERT INTO cage (superficie, capacite_max) VALUES (50, 10);
INSERT INTO cage (superficie, capacite_max) VALUES (100, 20);
INSERT INTO cage (superficie, capacite_max) VALUES (75, 15);
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO cage (superficie, capacite_max) VALUES (100, 20);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO cage (superficie, capacite_max) VALUES (75, 15);
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Lion', 'Panthera leo', 1, '2015-06-01', 'Kenya');
INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VQuery OK, 1 row affected (0.00 sec)

mysql> INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Elephant', 'Loxodonta', 2, '2010-03-15', 'Tanzania');
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES ('Giraffe', 'Giraffa camelopardalis', 3, '2018-09-12', 'South Africa');
Query OK, 1 row affected (0.00 sec)

mysql> 