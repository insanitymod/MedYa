CREATE TABLE Patient (
   id INT PRIMARY KEY,
   nom VARCHAR(255),
   prenom VARCHAR(255),
   date_naissance DATE,
   adresse VARCHAR(255),
   num_telephone VARCHAR(20)
);

CREATE TABLE Medecin (
   id INT PRIMARY KEY,
   nom VARCHAR(255),
   prenom VARCHAR(255),
   specialite VARCHAR(255),
   adresse VARCHAR(255),
   num_telephone VARCHAR(20)
);

CREATE TABLE RendezVous (
   id INT PRIMARY KEY,
   date_heure DATETIME,
   patient_id INT,
   medecin_id INT,
   FOREIGN KEY (patient_id) REFERENCES Patient(id),
   FOREIGN KEY (medecin_id) REFERENCES Medecin(id)
);

CREATE TABLE Prescription (
   id INT PRIMARY KEY,
   date DATE,
   patient_id INT,
   medecin_id INT,
   medicament VARCHAR(255),
   dosage VARCHAR(20),
   FOREIGN KEY (patient_id) REFERENCES Patient(id),
   FOREIGN KEY (medecin_id) REFERENCES Medecin(id)
);
