import mysql.connector

# recupere les donner 
nom=input("nom")
prenom=input("prenom")
email=input("email")

# se connecter a la BD


connection=mysql.connector.connect(host="fdb28.awardspace.net",
                                       user="4310852_medya",
                                       password="Momo-007",
                                       database="4310852_medya")

# inseretion
try:

    cursor=connection.cursor()
    insert="insert into Medya (nom.prenom.email) values (%s,%s,%s)"
    valeur=(nom,prenom,email)
    cursor.execute(insert,valeur)
    connection.commit()
finally:

    if  connection.is_connected():
        cursor.close()
        connection.close()

    




