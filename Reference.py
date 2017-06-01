


# ************************************************************************
# *************** SAUVEGARDE PIECES TGV DANS FICHIER *********************
#*************************************************************************
from xlwt import Workbook
import xlwt

# creation d'un classeur et d'une feuille
class CreateXls():

    """ Creation d'un fichier xls sous l'extention .mic qui servira
         de base de reference pour le comparer au fichier Logapli """

    def __init__(self, tab):
        self.tab = tab
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
 
        for ligne,v in enumerate(self.tab[1:]):
            if v['bdl'] == "yes":
                STYLE = self.style3
            else:
                STYLE = self.style2
            self.feuille.write(ligne + 1, 0, v['zone'], STYLE)
            self.feuille.write(
                ligne + 1, 1, v['symbole'], STYLE)
            self.feuille.write(ligne + 1, 2, v['nom'], STYLE)
            self.feuille.write(
                ligne + 1, 3, v['emplacement'], STYLE)
            self.feuille.write(ligne + 1, 4, v['bdl'], STYLE)
        try:
            self.classeur.save("References3.mic")
        except PermissionError:

            print(""" Veuillez fermer le fichier "References.mic"....""")

        print("creation du fichier EXCEL terminé....")
