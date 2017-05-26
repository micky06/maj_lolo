

import mysql.connector
import os
import time
#from GUI import *

class Verification():

    def __init__(self):
        self.Controle = 0

    def verif_param(self):
        try:
            f = open("param", "r")
            lignes = f.readlines()
            print("Ouverture param", lignes)
            f.close
        except FileNotFoundError:
            self.log = r"\\S58nelct120\mr_nel_technicentre_zones_blanches\LOGAPLI\LOGAPLI.xls"
            self.ips = "10.6.13.18"
            self.ids = "root"
            self.mdp = "r00t"
            self.dat = "pieces"
            print("param INEXISTANT")

            f = open("param", "w")
            f.write(self.log + "\n" + self.ips + "\n" +
                    self.ids + "\n" + self.mdp + "\n" +
                    self.dat + "\n")
            print("Fichier créé...")
            f.close
        else:
            params = []
            for ligne in lignes:
                params.append(ligne[:-1])
            print(params)
            self.log = r'%s' % params[0]
            self.ips = params[1]
            self.ids = params[2]
            self.mdp = params[3]
            self.dat = params[4]
            self.Controle += 1
            
            print("Récupération des parametres")
        liimd = [self.log, self.ips, self.ids, self.mdp, self.dat, self.Controle]
        return liimd


# ************************************************************************
# ********************* TEST RESEAU MYSQL ********************************
# ************************************************************************

    def verif_reseau(self):
        self.config = {'user': self.ids, 'password': self.mdp, 'host': self.ips, 'database': self.dat}
        print(self.config)
        try:
            cnx = mysql.connector.connect(**self.config)
            cur = cnx.cursor(buffered=True)
            cur.close()
            cnx.close()
            print("Serveur : OK")
            self.Controle += 1
            return True
        except:
            print("PAS DE RESEAU OU KIOSQUE HS")
        return False

# ************************************************************************
# ********************* TEST LIEN LOGAPLI ********************************
# ************************************************************************

    def verif_logapli(self):

        if os.path.isfile(self.log):
            print("Logapli : OK")
            self.Controle += 1
            return True
        else:
            print(" Lien LOGAPLI incorrecte...")

# ************************************************************************
# ********************* TEST FICHIER REFERENCE ***************************
# ************************************************************************

    def verif_reference(self):
        if os.path.isfile("References.mic"):
            print("reference : OK")
            return True
        else:
            # prevoir la creation du fichier
            print(" Fichier référence MANQUANT..")

