mysql> INSERT INTO etage(nom, numero, superficie) VALUES ("ROC", 0, 500)
    -> 
    -> ;
Query OK, 1 row affected (0.05 sec)

mysql> INSERT INTO etage(nom, numero, superficie) VALUES ("R+1", 1, 500);
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM etage;
+----+------+--------+------------+
| id | nom  | numero | superficie |
+----+------+--------+------------+
|  1 | ROC  |      0 |        500 |
|  2 | R+1  |      1 |        500 |
+----+------+--------+------------+
2 rows in set (0.02 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("lounge", 1, 100)
    -> ;
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("Studio Son", 1, 5); 
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("Broadcsting", 2, 50);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("Bocal Peda", 2, 4); 
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("Coworking", 2, 80); 
Query OK, 1 row affected (0.00 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite) VALUES ("Studio Video", 2, 5);
Query OK, 1 row affected (0.01 sec)

mysql> SELECT * FROM salle;
+----+--------------+----------+----------+
| id | nom          | id_etage | capacite |
+----+--------------+----------+----------+
|  1 | lounge       |        1 |      100 |
|  2 | Studio Son   |        1 |        5 |
|  3 | Broadcsting  |        2 |       50 |
|  4 | Bocal Peda   |        2 |        4 |
|  5 | Coworking    |        2 |       80 |
|  6 | Studio Video |        2 |        5 |
+----+--------------+----------+----------+
6 rows in set (0.00 sec)

mysql> 
