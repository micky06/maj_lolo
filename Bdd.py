
import mysql.connector
# ************************************************************************
# **************** MAJ DE LA BASE DE DONNEES MYSQL ***********************
#*************************************************************************

class BDD():

    def __init__(self, tab,config = None):
        self.tab = tab
        self.query = ""
        self.conn = mysql.connector.connect(**config)
        self.cursor = self.conn.cursor()
        self.nouveau = ""

    def __enter__(self):
        # Si ça ne fonctionne pas, alors mettre : 
        # return DB(logapli)
        return BDD(tab)

 
    def effacer(self):
        self.cursor.execute("""TRUNCATE TABLE logappli""")
        self.conn.commit()
        #self.cursor.execute("""CREATE TABLE logappli(id INTEGER PRIMARY KEY, zone TEXT, symbole TEXT, nom TEXT, emplacement TEXT, bdl TEXT);""")
        #self.conn.commit()

        print(".... TABLE EFFACEE.....")

    def maj(self):
        for x,v in enumerate(self.tab[1:]):
            Zone, Symbole, Nom, Emplacement, Bdl =  v['zone'],  v['symbole'], v['nom'],  v['emplacement'],  v['bdl']

            valeurs = (Zone, Symbole, Nom, Emplacement, Bdl)

            self.cursor.execute(
                """INSERT INTO logappli (zone,symbole,nom,emplacement,bdl) VALUES(%s,%s,%s,%s,%s)""", valeurs)
            self.conn.commit()
        print(".... TABLE MISE A JOUR.....")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("Close DB")
