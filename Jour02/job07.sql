mysql> CREATE DATABASE entreprise;
Query OK, 1 row affected (0.10 sec)

mysql> USE entreprise;
Database changed
mysql> CREATE TABLE employe (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     prenom VARCHAR(255),
    ->     salaire DECIMAL(10, 2),
    ->     id_service INT
    -> );
Query OK, 0 rows affected (0.08 sec)

mysql> INSERT INTO employe (nom, prenom, salaire, id_service)
    -> VALUES
    ->     ('Dupont', 'Pierre', 3500, 1),
    ->     ('Martin', 'Paul', 2500, 2),
    ->     ('Lemoine', 'Claire', 4000, 3),
    ->     ('Durand', 'Sophie', 2800, 1),
    ->     ('Lemoine', 'Jean', 5000, 3);
Query OK, 5 rows affected (0.01 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> CREATE TABLE service (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255)
    -> );
Query OK, 0 rows affected (0.02 sec)

mysql> INSERT INTO service (nom)
    -> VALUES
    ->     ('Informatique'),
    ->     ('Ressources humaines'),
    ->     ('Marketing');
Query OK, 3 rows affected (0.03 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM employe WHERE salaire > 3000;
+----+---------+--------+---------+------------+
| id | nom     | prenom | salaire | id_service |
+----+---------+--------+---------+------------+
|  1 | Dupont  | Pierre | 3500.00 |          1 |
|  3 | Lemoine | Claire | 4000.00 |          3 |
|  5 | Lemoine | Jean   | 5000.00 |          3 |
+----+---------+--------+---------+------------+
3 rows in set (0.01 sec)

mysql> SELECT e.nom, e.prenom, e.salaire, s.nom AS service
    -> FROM employe e
    -> JOIN service s ON e.id_service = s.id;
+---------+--------+---------+---------------------+
| nom     | prenom | salaire | service             |
+---------+--------+---------+---------------------+
| Dupont  | Pierre | 3500.00 | Informatique        |
| Martin  | Paul   | 2500.00 | Ressources humaines |
| Lemoine | Claire | 4000.00 | Marketing           |
| Durand  | Sophie | 2800.00 | Informatique        |
| Lemoine | Jean   | 5000.00 | Marketing           |
+---------+--------+---------+---------------------+
5 rows in set (0.02 sec)

mysql> 