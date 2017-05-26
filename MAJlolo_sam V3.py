

import os
import mysql.connector
from GUI import *
from Reference import *
from Bdd import *
from Verif import *
from Logapli import *
import socket

def main():
    # ************************************************************************
    # *********************** INITIALISATION *********************************
    # ************************************************************************


    logapli = Logapli()
    nsrtgv = Logapli()
    nsrtgv.lien_logapli = "References.mic"

    # ************************************************************************
    # ********************** Interface Graphique  ****************************
    # ************************************************************************



    v = Verification()
    v.verif_param()
    v.verif_reseau()
    v.verif_logapli()
    v.verif_reference()
    print(v.Controle)

    ihm = IHM(None)
    if v.Controle == 3:
        etat = "normal"
    else:
        etat = "disabled"
    ihm.initialize(v.log, v.ips, v.ids, v.mdp, v.dat, etat)
    ihm.mainloop()


    if v.Controle == 3:
        print('0 = QUITTER\n1 = Lire LOGAPLI\n2 = Lire XLS\n3 = Effacer\n4 = MAJ de la Table\n5 = Creation XLS\n6 = compare ', end=' ')
        a = int(input())     # conversion de la chaîne entrée en entier
        while a:     # équivalent à : < while a != 0: >
            if a == 1:
                print("Lecture du fichier LOGAPLI ...")
                logapli.readRowsLog("SYMBOLES")
            elif a == 2:
                print("Lecture du fichier Excel ...")
                nsrtgv.readRowsTgv("NSRTGV")
            elif a == 3:
                print("Effacement de la Table BDD ...")
                with DB(logapli) as db:
                    db.query = "TRUNCATE TABLE logappli"
                    db.effacer()
            elif a == 4:
                print("MAJ de la Table BDD ...")
                with DB(logapli) as db:
                    db.maj()
            elif a == 5:
                print("Creation du fichier Excel ...")
                createxls = CreateXls(logapli)
                createxls.creation()

            elif a == 6:
                print("Verification ...")
                logapli.compare()
                
            else:
                print("Choix incorrect....")
            print('0 = QUITTER\n1 = Lire LOGAPLI\n2 = Lire XLS\n3 = Effacer\n4 = MAJ de la Table\n5 = Creation XLS', end=' ')
            a = int(input())
        print("Vous avez entré zéro :")
    else:
        # ouvrir fenetre parametres
        print(" IL FAUT OUVRIR LA FENETRES DES PARAMETRES !!!!!!!!!!!!!!!")





if __name__ == "__main__":
    main()
    
