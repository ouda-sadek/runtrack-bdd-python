mysql> DESCRIBE etudiant;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nom    | varchar(255) | NO   |     | NULL    |                |
| prenom | varchar(25)  | NO   |     | NULL    |                |
| age    | int          | NO   |     | NULL    |                |
| email  | varchar(255) | NO   |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)
