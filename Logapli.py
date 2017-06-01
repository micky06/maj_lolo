# ************************************************************************
# ****************RECUPERATION PIECE TGV DE LOGAPLI ET DANS NSRTGV********
# ************************************************************************
import xlrd
import collections
from Compare import *
import time


class Logapli(object):

    def __init__(self):
        self.nb_lignes_en_cours = 0
        self.nb_total_lignes_log = 0
        self.lien_logapli = ""
        self.zone, self.symbole, self.nom, self.emplacement, self.bdl = [], [], [], [], []
        self.zonage = {"00000041059_001": "AUTRE", "00000041059_002": "VISSERIE",
                       "00000041059_003": "CONFORT", "00000041059_004": "MECA",
                       "00000041059_005": "VISSERIE", "BTGV1": "CONFORT", "BTGV2": "MECA",
                       "BTGV4": "MECA", "00000041059_006": "FILTRE"}

    def openWorkbook(self):
        return xlrd.open_workbook(self.lien_logapli)

    def sheetName(self, name):
        return self.openWorkbook().sheet_by_name(name)

    def readRowsLog(self, ws, ligne, tab):

        #ws = self.sheetName(name)
        #tab = []
        #for ligne in range(ws.nrows):
        d = collections.OrderedDict()
        x = format(ws.cell_value(ligne, 3))
        if "00000041059" in x or "BTGV" in x:

            self.symbole.append(format(ws.cell_value(ligne, 0)[0:8]))
            self.nom.append(format(ws.cell_value(ligne, 1)))
            self.emplacement.append(format(ws.cell_value(ligne, 4)))
            self.zone.append(self.zonage.get(
                format(ws.cell_value(ligne, 3))))
            if "BTGV" in x:
                self.bdl.append("yes")
            else:
                self.bdl.append("no")

            d['symbole'] = ws.cell_value(ligne, 0)[0:8]
            d['nom'] = ws.cell_value(ligne, 1)
            d['emplacement'] = ws.cell_value(ligne, 4)
            d['zone'] = ws.cell_value(ligne, 3)
            d['bdl'] = self.bdl[0]
            tab.append(d)

        #print("... RECUPERATION TERMINEE logapli.......")
        return tab

    def nbr(self):
        return len(self.zone)

    def readRowsTgv(self, ws, ligne, tab):
        d = collections.OrderedDict()
        self.symbole.append(format(ws.cell_value(ligne, 1)[0:8]))
        self.nom.append(format(ws.cell_value(ligne, 2)))
        self.emplacement.append(format(ws.cell_value(ligne, 3)))
        self.zone.append(self.zonage.get(format(ws.cell_value(ligne, 0))))
        d['symbole'] = ws.cell_value(ligne, 1)[0:8]
        d['nom'] = ws.cell_value(ligne, 2)
        d['emplacement'] = ws.cell_value(ligne, 3)
        d['zone'] = ws.cell_value(ligne, 0)
        d['bdl'] = ws.cell_value(ligne, 4)
        tab.append(d)
        return tab
