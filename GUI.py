
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
from Verif import Verification
from Logapli import *
from Compare import *
from Reference import *
from Bdd import *
import time
import asyncio
import image_base_64
from ctypes import windll


class IHM(Tk, Verification, Logapli):

    def __init__(self, parent):

        self.entrees = []
        Tk.__init__(self, parent)

        """ Icon Windows app"""
        img = PhotoImage(file=r'img/icon.png')
        self.tk.call('wm', 'iconphoto', self._w, img)
        
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
        # self.variable()
        self.initialize()

    def variable(self):
        liimd = Verification.verif_param(self)
        self.log = liimd[0]
        self.ips = liimd[1]
        self.ids = liimd[2]
        self.mdp = liimd[3]
        self.dat = liimd[4]

    def initialize(self):

        self.grid()

        self.title('Mise à Jour de la Borne')  # Ajout d'un titre
        self.update_idletasks()
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.l, self.h = width // 1.3, height // 1.3
        self.geometry("%dx%d%+d%+d" % (self.l, self.h,
                                       (width - self.l) // 2, (height - self.h) // 2))
        self.resizable(False, False)  # n'autoriser pas le redimensionnement.
        self.lpb = int(self.l // 1.4)

        self.marge(0)
        self.bmaj = Button(self, text=" Verifier la Maj", width=int(self.l // 70),
                           height=2, relief=RAISED, state=self.etat, command= self.bouton)
        self.bmaj.grid(row=16, column=1, sticky='WE', padx=3, pady=5)
        self.marge(2)
        bparam = Button(self, text=" Parametre", width=int(self.l // 70),
                        height=2, relief=RAISED, command=self.param)
        bparam.grid(row=16, column=3, sticky='E', padx=3, pady=5)
        self.marge(4)
        bquit = Button(self, text=" Quitter", width=int(self.l // 70),
                       height=2, relief=RAISED, command=self.destroy)
        bquit.grid(row=16, column=5, sticky='WE', padx=3, pady=5)
        self.marge(6)

        self.ligne(1)
        self.ligne(2)
        self.ligne(3)
        self.logo()
        self.logo_tgv()
        self.titre(4, "Vérification des paramètres : ")
        self.progress_bar(4, "verif")
        self.ligne(5)
        self.titre(6, "Lecture des Données LOGAPLI : ")
        self.progress_bar(6, "logapli")
        self.ligne(7)
        self.titre(8, "Lecture des Données de Référence : ")
        self.progress_bar(8, "reference")
        self.ligne(9)
        self.titre(10, "Recherche d'une Mise à Jour : ")
        self.progress_bar(10, "maj")
        self.ligne(11)
        self.titre(12, "Mise à Jour de la Base de Données : ")
        self.progress_bar(12, "bdd")
        self.ligne(13)
        self.ligne(14)


    def bouton(self):
        v = self.Verif_Maj()
        v() 
    def marge(self, column):
        Label(self, text=' ', width=int(self.l // 100)
              ).grid(row=0, column=column, sticky='EW')

    def ligne(self, row, bg=None):
        Label(self, text=' ', height=int(self.h // 200)
              ).grid(row=row, column=1, sticky='EW')

    def titre(self, line, titre):
        Label(self, text=titre, font=("Arial", int(self.l // 100),
                                      "bold italic")).grid(row=line, column=0, columnspan=3, sticky=EW)
    
    def logo(self):
        logo_png = PhotoImage(file ="deployment.gif")
        photo = Label(self, image=logo_png)
        photo.image = logo_png
        photo.grid(row=1, column=1, rowspan=2)
    
    def logo_tgv(self):
        logo_png = PhotoImage(file ="tgv_duplex.gif")
        photo = Label(self, image=logo_png)
        photo.image = logo_png
        photo.grid(row=2, column=3, columnspan=2)



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
        return (int(g[0:r[0]])), int(
            g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])

    def param(self):

        if self.f1:

            self.f1 = False
            self.fen1 = Toplevel(self)
            self.fen1.protocol("WM_DELETE_WINDOW", self.Fermer)
            # self.fen1.attributes("-toolwindow", 1)

            self.fen1.title('Paramètres')
            self.fen1.update_idletasks()
            l, h, x, y = self.geoliste(self.fen1.geometry())
            self.fen1.geometry("%dx%d%+d%+d" % ((l * 3), (h * 2),
                                                (self.fen1.winfo_screenwidth() - l) // 4, (self.fen1.winfo_screenheight() - h) // 4))
            self.fen1.resizable(False, False)

            # création de widgets Label(), Entry() :

            Label(self.fen1, text='').grid(row=0, column=0, sticky=E)
            Label(self.fen1, text='Lien LOGAPLI :').grid(
                row=1, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=2, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=3, column=0, sticky=E)
            Label(self.fen1, text='IP Serveur :').grid(
                row=4, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=5, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=6, column=0, sticky=E)
            Label(self.fen1, text='Identifiant :').grid(
                row=7, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=8, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=9, column=0, sticky=E)
            Label(self.fen1, text='Mot de passe :').grid(
                row=10, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=11, column=0, sticky=E)
            Label(self.fen1, text='').grid(row=12, column=0, sticky=E)
            Label(self.fen1, text='         Nom de la Base DATA :').grid(
                row=13, column=0, sticky=E)

            self.variable()
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
        fichier.close()
        v = Verification()
        v.verif_param()
        v.verif_reseau()
        v.verif_logapli()
        if v.Controle == 3:
            self.bmaj.config(state="normal")
            self.Fermer()
        else:
            messagebox.showerror("PROBLEME de paramètre", "Au moins 1 de vos paramètres n'est pas VALABLE...\n Merci de les vérifier.", parent=self.fen1)
            self.Fermer()
            self.param()
        return

    def Verif_Maj(self):
        self.bmaj.config(state="disabled")
        self.val_maj = 0

        i = self.verifReference("References2.mic", "SYMBOLES") # essai MAISON
#        i = self.verifReference(self.log, "SYMBOLES") # essai TRAVAIL
        j = self.verifReference("References3.mic", "NSRTGV")
        i()
        j()


        def wait():
            
            nonlocal i, j
            fini, tab = i(True)
            fini1, tab1 = j(True)
            if fini and fini1:
                c = Compare_log_nsrtgv()
                index = 0
                def refresh():
                    nonlocal self, index
                    long ,comp = c.compare(tab, tab1, index)
                    index += 1
                    count = (index / long) * 100
                    self.count_maj.set(count)
                    #print(self.count_maj.get())
                    if long > index:
                        self.after(1, refresh)
                    else:
                        print(long, comp)
                        nv = comp.get("nouveau")
                        sup = comp.get("supprime")
                        dep = comp.get("deplace")
                        for valeur in comp.values():
                            self.val_maj = self.val_maj + valeur

                        if self.val_maj !=0:
                            creat = CreateXls(tab)
                            if messagebox.askyesno("Résultat : ","Les changements suivants ont été trouvés :\n\n" +
                                                "Nouvelle(s) pièce(s) : %s\n" %nv +
                                                "Pièce(s) supprimée(s) : %s\n" %sup +
                                                "Pièce(s) déplacée(s) : %s\n" %dep +
                                                "\n \n Voulez-vous mettre à jour \n la Base De Données ? "):
                                self.bmaj.config(state="normal")
                                fin1 = creat.creation()
                                self.count_bdd.set(50)
                                if fin1:                                                
                                    self.db(tab)
                                    self.count_bdd.set(100)
                                messagebox.showinfo("TERMINE...", " Base de Donnéés et Fichier Référence Maj")
                                self.count_bdd.set(0)
                                self.count_logapli.set(0)
                                self.count_reference.set(0)
                                self.count_maj.set(0)
                                self.bmaj.config(state="normal")
                            else:
                                self.bmaj.config(state="normal")
                            
                        else:
                            messagebox.showinfo("Résultat : ", "Aucun changement n'a été trouvé\n \n Il est INUTILE de mettre à jour la Base De Donéées...")
                            self.bmaj.config(state="normal")
                            print("Pas de MAJ a faire")

                refresh()

            else:
                self.after(1000, wait)

        return wait

    def db(self, tab):
        self.variable()
        config = {'user': self.ids, 'password': self.mdp,
                       'host': self.ips, 'database': self.dat}
        bdd = BDD(tab, config)
        bdd.effacer()
        bdd.maj()



    def Fermer(self):
        self.f1 = True
        self.fen1.destroy()
        return self.f1

    def verif(self):
        if self.count_verif.get() == 1:
            self.v.verif_param()
            self.count_verif.set(25)
        elif self.count_verif.get() == 25:
            self.v.verif_reseau() 
            self.count_verif.set(50)
        elif self.count_verif.get() == 50:
#            self.v.verif_logapli() # A retirer pour essai MAISON
            self.count_verif.set(75)
        elif self.count_verif.get() == 75:
            self.v.verif_reference()
            self.count_verif.set(100)

            if self.v.Controle == 3:
                self.bmaj.config(state="normal")
            else:
                self.bmaj.config(state="normal") # essai MAISON
#                self.bmaj.config(state="disabled") # essai TRAVAIL
                messagebox.showwarning("PROBLEME de paramètre", "Au moins 1 de vos paramètres n'est pas VALABLE...\n Merci de les vérifier.")
            return
        elif self.count_verif.get() == 0:
            self.count_verif.set(1)

        if self.count_verif.get() < 100:
            self.after(1000, self.verif)

    def verifReference(self, lien, name):
        self.count_maj.set(0)
        if name == "NSRTGV":
            readRows = self.readRowsTgv
            counter = self.count_reference
        else:
            readRows = self.readRowsTgv # essai MAISON
 #           readRows = self.readRowsLog # essai TRAVAIL
            counter = self.count_logapli

        self.logapli.lien_logapli = lien
        ws = self.logapli.sheetName(name)
        tab = []
        ligne = 1

        fini = False

        def g(info=False):
            nonlocal ws, ligne, tab, fini
            if not info:
                if ligne < ws.nrows:
                    tab = readRows(ws, ligne, tab)
                    counter.set((ligne / ws.nrows) * 100)
                    ligne += 1
                    self.after(1, g)
                else:
                    fini = True
                    print(" jai fini reference....", fini)
            else:
                if fini:
                    return (fini, tab)
                    
                else:
                    return (fini, None)

        return g
    
    def overrideredirect(self, boolean=None):

        Tk.overrideredirect(self, boolean)
        GWL_EXSTYLE = -20
        WS_EX_APPWINDOW = 0x00040000
        WS_EX_TOOLWINDOW = 0x00000080
        if boolean:
            hwnd = windll.user32.GetParent(self.winfo_id())
            style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
            style = style & ~WS_EX_TOOLWINDOW
            style = style | WS_EX_APPWINDOW
            res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)

        self.wm_withdraw()
        self.wm_deiconify()



ihm = IHM(None)

ihm.overrideredirect(True)
# self.attributes("-toolwindow", 1)

ihm.overrideredirect()

ihm.verif()


ihm.mainloop()
