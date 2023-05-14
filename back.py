import mysql.connector

# se connecter à la base de données
conn = mysql.connector.connect(user='nom_utilisateur', password='mot_de_passe', host='hôte', database='nom_de_la_base_de_donnees')

# créer un curseur pour exécuter les requêtes SQL
cur = conn.cursor()

# insérer un nouveau patient
cur.execute("INSERT INTO Patient (id, nom, prenom, date_naissance, adresse, num_telephone) VALUES (%s, %s, %s, %s, %s, %s)",
            (1, 'Dupont', 'Jean', '1990-01-01', '1 rue des Lilas', '0601020304'))

# valider la transaction
conn.commit()

# fermer le curseur et la connexion
cur.close()
conn.close()
