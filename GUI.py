
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from Verif import Verification
from Logapli import *
from Compare import *
import time
import asyncio

class IHM(Tk,Verification,Logapli):

    def __init__(self, parent):
        
        self.entrees = []
        Tk.__init__(self, parent)
        Verification.__init__(self)
        Logapli.__init__(self)
        self.parent = parent
        self.f1 = True
        self.fin = True
        self.etat = "disabled"
        self.vpb = 1
        self.list_log = []
        self.v = Verification()
        self.nsrtgv = Logapli()
        self.logapli = Logapli()
        self.variable()
        self.initialize()
        
        

    def variable(self):
        liimd = Verification.verif_param(self)
        print("########################## ==>  ", liimd)
        self.log = liimd[0]
        self.ips = liimd[1]
        self.ids = liimd[2]
        self.mdp = liimd[3]
        self.dat = liimd[4]
        

    def initialize(self):
        
        self.grid()
        self.attributes("-toolwindow", 1)
        self.title('Mise à Jour de la Borne')  # Ajout d'un titre
        self.update_idletasks()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.l, self.h = width // 1.3, height // 1.3
        self.geometry("%dx%d%+d%+d" % (self.l, self.h, (width - self.l) // 2,(height - self.h) // 2))
        self.resizable(False, False)  # n'autoriser pas le redimensionnement.
        self.lpb = int(self.l // 1.4)

        self.marge(0)
        self.bmaj = Button(self, text=" Verifier la Maj", width=int(self.l // 70),
                      height=2, relief=RAISED,state=self.etat, command=self.Verif_Maj)
        self.bmaj.grid(row=16, column=1, sticky='WE',padx=3, pady=5)
        self.marge(2)
        bparam = Button(self, text=" Parametre", width=int(self.l // 70),
                        height=2, relief=RAISED, command=self.param)
        bparam.grid(row=16, column=3, sticky='WE',padx=3, pady=5)
        self.marge(4)
        bquit = Button(self, text=" Quitter", width=int(self.l // 70),
                        height=2, relief=RAISED, command=self.destroy)
        bquit.grid(row=16, column=5, sticky='WE',padx=3, pady=5)
        self.marge(6)
        
        self.ligne(1)
        self.ligne(2)
        self.ligne(3)
        self.titre(4,"Vérification des paramètres : ")
        self.progress_bar(4, "verif")
        self.ligne(5)
        self.titre(6,"Lecture des Données LOGAPLI : ")
        self.progress_bar(6, "logapli")
        self.ligne(7)
        self.titre(8,"Lecture des Données de Référence : ")
        self.progress_bar(8, "reference")
        self.ligne(9)
        self.titre(10,"Recherche d'une Mise à Jour : ")
        self.progress_bar(10, "maj")
        self.ligne(11)
        self.titre(12,"Mise à Jour de la Base de Données : ")
        self.progress_bar(12, "bdd")
        self.ligne(13)
        self.ligne(14)
         
        # Wait for 5 seconds
        # time.sleep(15)

        
        
        print( self.state())
        
    def marge(self, column):
        Label(self, text=' ', width=int(self.l // 100)).grid(row=0, column=column, sticky='EW')

    def ligne(self, row):
        Label(self, text=' ', height=int(self.h // 200)).grid(row=row, column=1, sticky='EW')

    def titre(self, line, titre):
        Label(self, text = titre , font = ("Arial",int(self.l // 100), "bold italic")).grid(row = line, column = 0, columnspan=3, sticky =EW)
        
    def progress_bar(self, line, name):

        style = ttk.Style()
        style.theme_use('alt')
        style.configure("green.Horizontal.TProgressbar",
                        foreground='white', background='green')

        if name == "verif":
            self.count_verif = DoubleVar()
            self.ProgressBarTtk(line, self.count_verif)
        elif name == "logapli":
            self.count_logapli = DoubleVar()
            self.ProgressBarTtk(line, self.count_logapli)
        elif name == "reference":
            self.count_reference = DoubleVar()
            self.ProgressBarTtk(line, self.count_reference)
        elif name == "maj":
            self.count_maj = DoubleVar()
            self.ProgressBarTtk(line, self.count_maj)
        elif name == "bdd":
            self.count_bdd = DoubleVar()
            self.ProgressBarTtk(line, self.count_bdd)
        
    def ProgressBarTtk(self, line, var):
        pb = ttk.Progressbar(
            self, variable=var, style="green.Horizontal.TProgressbar",
            maximum=100, length=int(self.l // 1.4))
        pb.grid(row=line, column=3, columnspan=3)
        
        return pb


    def geoliste(self, g):
        r = [i for i in range(0, len(g)) if not g[i].isdigit()]
        print(g, r)
        return (int(g[0:r[0]])), int(
            g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])

    def param(self):

        if self.f1:

            self.f1 = False
            self.fen1 = Toplevel(self)
            self.fen1.protocol("WM_DELETE_WINDOW", self.Fermer)
            self.fen1.attributes("-toolwindow", 1)
            
            self.fen1.title('Paramètres')
            self.fen1.update_idletasks()
            l, h, x, y = self.geoliste(self.fen1.geometry())
            self.fen1.geometry("%dx%d%+d%+d" % ((l * 3), (h * 2),
                                           (self.fen1.winfo_screenwidth() - l) // 4, (self.fen1.winfo_screenheight() - h) // 4))
            self.fen1.resizable(False, False)

            # création de widgets Label(), Entry() :

            Label(self.fen1, text='').grid(row=0, column=0, sticky=E)
            Label(self.fen1, text='Lien LOGAPLI :').grid(row=1, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=2, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=3, column=0, sticky=E)
            Label(self.fen1, text='IP Serveur :').grid(row=4, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=5, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=6, column=0, sticky=E)
            Label(self.fen1, text='Identifiant :').grid(row=7, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=8, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=9, column=0, sticky=E)
            Label(self.fen1, text='Mot de passe :').grid(row=10, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=11, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=12, column=0, sticky=E)
            Label(self.fen1, text='         Nom de la Base DATA :').grid(
                row=13, column=0, sticky=E)

            self.lienlogapli = Entry(self.fen1, width=65)  # LIEN LOGAPLI
            self.lienlogapli.insert(0, self.log)
            self.ipserveur = Entry(self.fen1, width=45)  # IP SERVEUR MYSQL
            self.ipserveur.insert(0, self.ips)
            self.idserveur = Entry(self.fen1, width=45)  # IDENTIFIANT MYSQL
            self.idserveur.insert(0, self.ids)
            self.mdpserveur = Entry(self.fen1, width=45)  # MDP MYSQL
            self.mdpserveur.insert(0, self.mdp)
            self.nomtable = Entry(self.fen1, width=45)  # TABLE MYSQL
            self.nomtable.insert(0, self.dat)

            Label(self.fen1, text='').grid(row=0, column=1, sticky=E)
            self.lienlogapli.grid(row=1, column=1)
            Label(self.fen1, text='').grid(row=2, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=3, column=1, sticky=E)
            self.ipserveur.grid(row=4, column=1, sticky=W)
            Label(self.fen1, text='').grid(row=5, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=6, column=1, sticky=E)
            self.idserveur.grid(row=7, column=1, sticky=W)
            Label(self.fen1, text='').grid(row=8, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=9, column=1, sticky=E)
            self.mdpserveur.grid(row=10, column=1, sticky=W)
            Label(self.fen1, text='').grid(row=11, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=12, column=1, sticky=E)
            self.nomtable.grid(row=13, column=1, sticky=W)
            Label(self.fen1, text='').grid(row=14, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=15, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=16, column=1, sticky=E)
            Label(self.fen1, text='').grid(row=17, column=1, sticky=E)
            
            valid = Button(self.fen1, text="Vailder", relief=RAISED,
                           command=self.validation)
            anull = Button(self.fen1, text="QUITTER",
                           relief=RAISED, command=self.Fermer)

            valid.grid(row=16, column=0, sticky=E)
            anull.grid(row=16, column=1, sticky=E)
        else:
            pass

    def validation(self):
        fichier = open("param", "w")
        fichier.write(self.lienlogapli.get() + "\n" + self.ipserveur.get() + "\n" +
                        self.idserveur.get() + "\n" + self.mdpserveur.get() + "\n" + self.nomtable.get() + "\n")
        fichier.flush()
        fichier.close
        print(self.lienlogapli.get(), "\n", self.ipserveur.get(), "\n",
        self.idserveur.get(), "\n", self.mdpserveur.get(), "\n", self.nomtable.get())

        #self.update_idletasks()

        v = Verification()
        v.verif_param()
        v.verif_reseau()
        v.verif_logapli()
        if v.Controle == 3:
            self.bmaj.config(state = "normal")
        self.Fermer()
    
    def Verif_Maj(self):
        # list_log =[]
        # logapli = Logapli()
        # nsrtgv = Logapli()
        # logapli.lien_logapli = self.log
        # nsrtgv.lien_logapli = "References.mic"
        # i = ihm.verifReference(self.log, "SYMBOLES")
        
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.verifReference("References.mic", "NSRTGV"))
        #comp = Compare_log_nsrtgv()
        #print(comp.compare(list_log, tgv))



    def Fermer(self):
        self.f1 = True
        self.fen1.destroy()
        return self.f1


    def verif(self):
        print(self.count_verif.get())
        if self.count_verif.get() == 1:
            self.v.verif_param()
            self.count_verif.set(25)
        elif self.count_verif.get() == 25:
            # self.v.verif_reseau()
            self.count_verif.set(50)
        elif self.count_verif.get() == 50:
            self.v.verif_logapli()
            self.count_verif.set(75)
        elif self.count_verif.get() == 75:
            self.v.verif_reference()
            self.count_verif.set(100)

            if self.v.Controle == 3:
                self.bmaj.config(state = "normal")
            else:
                self.bmaj.config(state = "disabled")
            return
        elif self.count_verif.get() == 0:
            self.count_verif.set(1)
        
        if self.count_verif.get() < 100:
            self.after(1000, self.verif)
    
    @asyncio.coroutine
    def verifReference(self, lien, name):
        if name == "NSRTGV":
            self.counter = self.count_reference
        else:
            self.counter = self.count_logapli

        self.logapli.lien_logapli = lien
        self.ws = self.logapli.sheetName(name)
        self.tab = []    
        self.ligne = 1
        print(name, self.ws.nrows)
        res = yield from self.g()
        print(res)

    @asyncio.coroutine
    def g(self):
        
        if self.ligne < self.ws.nrows:
            self.tab = self.logapli.readRowsTgv(self.ws, self.ligne, self.tab)
            self.counter.set((self.ligne / self.ws.nrows) * 100)
            self.ligne += 1
            print("Ligne : ", self.ligne)
            self.after(2, self.g)
        else:
            return self.tab

    # import asyncio

    # @asyncio.coroutine
    # def slow_square(x):
    #     yield from asyncio.sleep(1)
    #     return x * x

    # @asyncio.coroutine
    # def test():
    #     res = yield from slow_square(3)
    #     print(res)

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test())

    def verifref(self, lien1, name1):
        
        self.lien, self.name = lien1, name1
        print(self.lien, self.name)
        self.verifReference(self.lien, self.name)
        
        #return self.tab

ihm = IHM(None)
ihm.verif()

#ihm.verifLogapli()

ihm.Verif_Maj()


ihm.mainloop()