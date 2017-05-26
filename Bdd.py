# ************************************************************************
# **************** MAJ DE LA BASE DE DONNEES MYSQL ***********************
#*************************************************************************

class DB():

    def __init__(self, logapli):
        self.logapli = logapli
        self.config = {'user': 'root', 'password': 'r00t',
                       'host': '10.6.13.18', 'database': 'pieces'}
        self.query = ""
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        self.nouveau = ""

    def __enter__(self):
        # Si ça ne fonctionne pas, alors mettre : 
        # return DB(logapli)
        return DB(self.logapli)

    # def getAll(self):
    #     self.cursor.execute(self.query)
    #     return self.cursor.fetchall()

    # def getOne(self):
    #     self.cursor.execute(self.query)
    #     return self.cursor.fetchone()

    # def boucleGetAll(self, args):
    #     for (id, symbole, nom) in args:
    #         print('{0} : {1} : {2}'.format(id, symbole, nom))

    def effacer(self):
        self.cursor.execute(self.query)
        self.conn.commit()
        print(".... TABLE EFFACEE.....")

    def maj(self):
        x = 0
        for x in range(self.logapli.nbr()):
            Zone, Symbole, Nom, Emplacement, Bdl = self.logapli.zone[x], self.logapli.symbole[
                x], self.logapli.nom[x], self.logapli.emplacement[x], self.logapli.bdl[x]

            valeurs = (Zone, Symbole, Nom, Emplacement, Bdl)

            self.cursor.execute(
                """INSERT INTO logappli (zone,symbole,nom,emplacement,bdl) VALUES(%s,%s,%s,%s,%s)""", valeurs)
            self.conn.commit()
        print(".... TABLE MISE A JOUR.....")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
            print("Close DB")
