<<<<<<< HEAD
import sqlite3

# se connecter à la base de données
conn = sqlite3.connect('nom_de_la_base_de_donnees.db')

# créer un curseur pour exécuter les requêtes SQL
cur = conn.cursor()

# insérer un nouveau patient dans la table Patient
cur.execute("INSERT INTO Patient (id, nom, prenom, date_naissance, adresse, num_telephone) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 'Dupont', 'Jean', '1990-01-01', '1 rue des Lilas', '0601020304'))

# valider la transaction
conn.commit()

# fermer le curseur et la connexion
cur.close()
conn.close()
=======
import sqlite3

# se connecter à la base de données
conn = sqlite3.connect('nom_de_la_base_de_donnees.db')

# créer un curseur pour exécuter les requêtes SQL
cur = conn.cursor()

# insérer un nouveau patient dans la table Patient
cur.execute("INSERT INTO Patient (id, nom, prenom, date_naissance, adresse, num_telephone) VALUES (?, ?, ?, ?, ?, ?)",
            (1, 'Dupont', 'Jean', '1990-01-01', '1 rue des Lilas', '0601020304'))

# valider la transaction
conn.commit()

# fermer le curseur et la connexion
cur.close()
conn.close()
>>>>>>> 258e66c6cb5117d089998cb0a1c07a82d5a67c0e
