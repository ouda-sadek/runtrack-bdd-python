mysql> Use LaPlateforme;

mysql> CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     numero INT NOT NULL,
    ->     superficie INT NOT NULL
    -> );
Query OK, 0 rows affected (0.09 sec)

mysql> CREATE TABLE salle (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     id_etage INT,
    ->     capacite INT,
    ->     FOREIGN KEY (id_etage) REFERENCES etage(id)
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> SHOW TABLES;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etage                  |
| etudiant               |
| salle                  |
+------------------------+
3 rows in set (0.12 sec)


