


# ************************************************************************
# *************** SAUVEGARDE PIECES TGV DANS FICHIER *********************
#*************************************************************************
from xlwt import Workbook
import xlwt

# creation d'un classeur et d'une feuille
class CreateXls():

    def __init__(self, logapli):
        self.logapli = logapli
        self.classeur = Workbook()
        self.feuille = self.classeur.add_sheet("NSRTGV")

        self.style1 = xlwt.easyxf("font: bold 1, color black; pattern: pattern solid, fore-colour light_blue;"
                                  "align: horizontal center, vertical center;"
                                  "border: left thin, top thin, right thin, bottom thin")
        self.style2 = xlwt.easyxf("font: bold 1, color black; pattern: pattern solid, fore-colour white;"
                                  "align: horizontal center, vertical center;"
                                  "border: left thin, top thin, right thin, bottom thin")
        self.style3 = xlwt.easyxf("font: bold 1, color black; pattern: pattern solid, fore-colour yellow;"
                                  "align: horizontal center, vertical center;"
                                  "border: left thin, top thin, right thin, bottom thin")

# creation des ENTETEs
    def creation(self):
        self.feuille.write(0, 0, "ZONE", self.style1)
        self.feuille.write(0, 1, "SYMBOLE", self.style1)
        self.feuille.write(0, 2, "NOM", self.style1)
        self.feuille.write(0, 3, "EMPLACEMENT", self.style1)
        self.feuille.write(0, 4, "BDL", self.style1)
        self.feuille.col(0).width = 5760
        self.feuille.col(1).width = 5760
        self.feuille.col(2).width = 26120
        self.feuille.col(3).width = 5080
        self.feuille.col(4).width = 2400
        # remplissage du tableau
        ligne = 0
        for ligne in range(self.logapli.nbr()):
            if self.logapli.bdl[ligne] == "yes":
                STYLE = self.style3
            else:
                STYLE = self.style2
            self.feuille.write(ligne + 1, 0, self.logapli.zone[ligne], STYLE)
            self.feuille.write(
                ligne + 1, 1, self.logapli.symbole[ligne], STYLE)
            self.feuille.write(ligne + 1, 2, self.logapli.nom[ligne], STYLE)
            self.feuille.write(
                ligne + 1, 3, self.logapli.emplacement[ligne], STYLE)
            self.feuille.write(ligne + 1, 4, self.logapli.bdl[ligne], STYLE)
        try:
            self.classeur.save("References.mic")
        except PermissionError:

            print(""" Veuillez fermer le fichier "References.xls"....""")

        print("creation du fichier EXCEL terminé....")

# sauvegarde du classeur
