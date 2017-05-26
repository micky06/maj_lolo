# ************************************************************************
# ****************RECUPERATION PIECE TGV DE LOGAPLI ET DANS NSRTGV********
# ************************************************************************
import xlrd


class Logapli:

    def __init__(self):
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

    def readRowsLog(self, name):
        ws = self.sheetName(name)
        for ligne in range(ws.nrows):
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
        print("... RECUPERATION TERMINEE.......")
        return ws

    def readRowsTgv(self, name):
        ws = self.sheetName(name)
        tab = []
        for ligne in range(ws.nrows):
            self.symbole.append(format(ws.cell_value(ligne, 1)[0:8]))
            self.nom.append(format(ws.cell_value(ligne, 2)))
            self.emplacement.append(format(ws.cell_value(ligne, 3)))
            self.zone.append(self.zonage.get(format(ws.cell_value(ligne, 0))))
            tab.append({'symbole': ws.cell_value(ligne, 1)[0:8],
                        'nom': ws.cell_value(ligne, 2),
                        'emplacement': ws.cell_value(ligne, 3),
                        'zone': ws.cell_value(ligne, 0)})

        return tab

    def nbr(self):
        return len(self.zone)

    # def compare(self):

    #     x = 0
    #     self.long = len(self.symbole)
    #     self.deplace = []
    #     self.nouveau = []
    #     self.supprime = []

    #     for x in range(self.logapli.nbr()):

    #         lign = 0
    #         if self.logapli.symbole[x] in self.nsrtgv.symbole:

    #             a = self.logapli.symbole[x]
    #             lign = self.nsrtgv.symbole.index(a)

    #             if a != self.nsrtgv.emplacement[lign]:
    #                 if a != self.nsrtgv.emplacement[lign+1]:
    #                     if a != self.nsrtgv.emplacement[lign+2]:
    #                         self.deplace.append("\n",[self.logapli.zone[x],self.logapli.symbole[x],self.logapli.emplacement[x],self.logapli.nom[x]])
    #         else:
    #             self.nouveau.append("\n",[self.logapli.zone[x],self.logapli.symbole[x],self.logapli.emplacement[x],self.logapli.nom[x]])

    # print(self.long, self.deplace)

    @staticmethod
    def test(list_log, list_nsrtgv):
        long = len(list_nsrtgv)
        deplace = 0
        nouveau = 0
        supprime = 0
        for i, l in enumerate(list_log):
            if l in list_nsrtgv:
                print(l)
                count = list_nsrtgv.count(l.keys())
                lign = list_nsrtgv.index(l['symbole'])
                if count > 1:
                    print(count)
                    for c in range(count):
                        if l['emplacement'] != list_nsrtgv['emplacement']:
                            deplace += 1
                else:
                    if l['emplacement'] != list_nsrtgv['emplacement']:
                        deplace += 1

            # Si il n'existe pas
            else:
                nouveau += 1

        for tgv in list_nsrtgv:
            if not tgv in list_log:
                supprime += 1
        
        return {'deplace': deplace, 'nouveau': nouveau, 'supprime': supprime}

nsrtgv = Logapli()
# logapli = Logapli()

# log.lien_logapli = "moldu.mic"
nsrtgv.lien_logapli = "References.mic"

# logapli.readRowsLog('SYMBOLE')
tgv = nsrtgv.readRowsTgv('NSRTGV')

# print(list_tgv)

Logapli.test(tgv, tgv)
