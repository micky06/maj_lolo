from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

#----------------------------------------------------------------------

def geoliste(self, g):
        r = [i for i in range(0, len(g)) if not g[i].isdigit()]
        return (int(g[0:r[0]])), int(
            g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])


def verif():

        
        fen1 = Tk()
        fen1.attributes("-toolwindow", 1)
        fen1.title('Vérifications')
        fen1.update_idletasks()
        photo = PhotoImage(file="OK.png")
        igm = Text.image_create(0,0,image= photo)
        
        fen1.resizable(False, False)

        # création de widgets Label(), Entry() :

        Label(fen1, igm).grid(row=0, column=0, sticky=E)
        Label(fen1, text='').grid(row=0, column=1, sticky=E)
        Label(fen1, text='Test connection Base de Données...').grid(row=1, column=1, sticky=E)
        Label(fen1, text='').grid(row=2, column=1, sticky=E)
        Label(fen1, text='').grid(row=3, column=1, sticky=E)
        Label(fen1, text='Test').grid(row=4, column=1, sticky=E)
        Label(fen1, text='').grid(row=5, column=1, sticky=E)
        Label(fen1, text='').grid(row=6, column=1, sticky=E)
        Label(fen1, text='Test').grid(row=7, column=1, sticky=E)
        Label(fen1, text='').grid(row=8, column=1, sticky=E)
        Label(fen1, text='').grid(row=9, column=1, sticky=E)
        Label(fen1, text='Test').grid(row=10, column=1, sticky=E)
        Label(fen1, text='').grid(row=11, column=1, sticky=E)
        Label(fen1, text='').grid(row=12, column=1, sticky=E)
        Label(fen1, text='         Test').grid(row=13, column=1, sticky=E)

verif()
