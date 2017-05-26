#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from multiprocessing import Queue
import json
import os.path
import sys
from tkinter import *
from tkinter.messagebox import *
import tkinter.ttk as ttk

if sys.platform == "win32":
    from ctypes import windll


class Window(Tk):

    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
        self.url = ''
        self.homeFile = os.path.expanduser(
            '~') + self.osSlash() + '.traffic_speed'
        img = PhotoImage(file=r'img/icon.png')
        self.tk.call('wm', 'iconphoto', self._w, img)
        self.maxRx = 1

    def osSlash(self):
        if sys.platform == 'win32':
            return '\\'
        else:
            return '/'

    def initialize(self):
        self.grid()
        # **** Configuration principale!!! *******
        self.title('Traffic Speed')
        self.update_idletasks()
        width = self.winfo_screenwidth() - 430
        height = self.winfo_screenheight() - 170
        self.geometry('400x100+{}+{}'.format(width, height))
        self.configure(background='black')

        # ************** Option des input et button ****************
        self.option = {'fg': 'white', 'bg': 'black',
                       'justify': 'center'}
        self.option_font = {'font': 'none 16 italic'}
        self.option_entry = {
            **self.option, 'insertbackground': 'white', 'borderwidth': 0, **self.option_font}

        self.option_button = {**self.option}

        self.inputText()
        self.valid()
        self.label()
        self.labelImage()
        self.progressBar()

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

    # *********** On commence avec la première ligne ************
    # ********************** Input ******************************

    def inputText(self):
        self.host_variable = StringVar()
        self.host = Entry(self, **self.option_entry, width=10,
                          textvariable=self.host_variable)
        self.host.grid(column=0, row=0, sticky='EW',
                       padx=3, pady=7, columnspan='6')
        self.host_variable.set(u"ex : sokys.noip.me")
        self.host.bind("<Key>", self.key)

        self.port_variable = StringVar()
        self.port = Entry(self, **self.option_entry, width=7,
                          textvariable=self.port_variable)
        self.port.grid(column=6, row=0, sticky='EW',
                       padx=3, pady=7, columnspan='3')
        self.port_variable.set(u"ex : 1111")
        self.port.bind("<Key>", self.key)

    # ********************** Button *****************************
    def valid(self):
        button = Button(self, text=u"Ok", **self.option_button)
        button.grid(column=9, row=0, pady=7, padx=3)
        button.bind("<Key>", self.key)
        button.bind("<Button-1>", self.callback)

    # ********************** Label ******************************
    def label(self):
        self.name_variable = StringVar()
        self.name = Label(self, textvariable=self.name_variable,
                          **self.option, **self.option_font, width=7)
        self.name.grid(column=0, row=1, sticky='EW', columnspan='2', padx=3)
        self.name_variable.set(u"enp0s25")

        self.rx_variable = StringVar()
        self.rx = Label(self, textvariable=self.rx_variable, **
                        self.option, **self.option_font, width=11)
        self.rx.grid(column=2, row=1, sticky='EW', columnspan='4', padx=3)
        self.rx_variable.set(u"25.235 Ko/s")

        self.tx_variable = StringVar()
        self.tx = Label(self, textvariable=self.tx_variable, **
                        self.option, **self.option_font, width=11)
        self.tx.grid(column=6, row=1, sticky='EW', columnspan='4', padx=3)
        self.tx_variable.set(u"10.123 Mo/s")

    def labelImage(self):
        self.name_image = Label(self, **self.option, **self.option_font)
        self.name_image.grid(column=0, row=2, sticky='EW', columnspan='2')

        rxPhoto = PhotoImage(file="img/rx.png")
        self.rx_image = Label(self, image=rxPhoto, **
                              self.option, **self.option_font)
        self.rx_image.photo = rxPhoto
        self.rx_image.grid(column=2, row=2, sticky='EW', columnspan='4')

        txPhoto = PhotoImage(file="img/tx.png")
        self.tx_image = Label(self, image=txPhoto, **
                              self.option, **self.option_font)
        self.tx_image.photo = txPhoto
        self.tx_image.grid(column=6, row=2, sticky='EW', columnspan='4')

    # ********************** Label ******************************
    def progressBar(self):
        self.progress_var = DoubleVar()

        style = ttk.Style()
        style.theme_use('alt')
        style.configure("green.Horizontal.TProgressbar",
                        foreground='white', background='black')

        self.bar = ttk.Progressbar(
            self, variable=self.progress_var, style="green.Horizontal.TProgressbar",
            maximum=100)

        self.bar.grid(column=0, row=2)

    def writeFile(self, host, port):
        f = open(self.homeFile, 'w')
        f.write("http://" + host + ":" + port)
        self.url = "http://" + host + ":" + port
        f.close()

    def readFile(self):
        if os.path.exists(self.homeFile):
            f = open(self.homeFile, 'r')
            self.url = ""
            count = 0
            for l in f:
                if count == 0:
                    self.url = l
                count += 1
            f.close()
            return self.url
        else:
            return ''

    def getJson(self):
        try:
            req = requests.post(self.url)
            json_data = req.json()
            return json_data[0]
        except requests.exceptions.RequestException as e:
            showinfo(
                'Erreur', 'Attention une erreur d\'adresse est survenu.\rVérifier host et port!')
            return ''

    def refresh(self):
        d = self.getJson()

        if d:
            actual = self.debitToOctect(d["RxName"], float(d["RxFinal"]))
            if self.maxRx < actual:
                self.maxRx = actual

            self.progress_var.set(self.barPourcent(actual, self.maxRx))
            self.name_variable.set(d["Name"])
            self.rx_variable.set("{0} {1}".format(d["RxFinal"], d["RxName"]))
            self.tx_variable.set("{0} {1}".format(d["TxFinal"], d["TxName"]))
            self.after(1000, self.refresh)

    def barPourcent(self, actual, max_rx=1):
        return (actual / max_rx) * 100

    def debitToOctect(self, name, debit):
        if name == "Mo/s":
            return debit * 1000000
        elif name == "Ko/s":
            return debit * 1000
        else:
            return debit

    def exitApp(self, event):
        response = askokcancel(
            title="Quitter ?", message="Veux-tu quitter l'application?")
        if response:
            self.destroy()
        else:
            self.after(1, lambda: self.focus_force())

    def focus(self, event):
        self.after(1, lambda: self.focus_force())

    def key(self, event):
        if event.char == '\r':
            self.saveHostAndPort()

    def callback(self, event):
        self.saveHostAndPort()

    def saveHostAndPort(self):
        response = askokcancel(
            'Enregistrer', 'Veux-tu enregistrer les nouvelles informations ?')
        if response:
            self.writeFile(self.host.get(), self.port.get())
            self.refresh()

    def create_window(self):
        window = Toplevel(self)

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


def main():
    w = Window(None)

    if sys.platform == "win32":
        w.overrideredirect(True)
    else:
        w.wm_attributes('-fullscreen', 'true')

    w.bind("<Button-3>", w.exitApp)

    w.name.bind("<Button-1>", w.focus)
    w.rx.bind("<Button-1>", w.focus)
    w.tx.bind("<Button-1>", w.focus)
    w.name_image.bind("<Button-1>", w.focus)
    w.rx_image.bind("<Button-1>", w.focus)
    w.tx_image.bind("<Button-1>", w.focus)

    read = w.readFile()
    w.url = read
    if read:
        w.host_variable.set(read.split("://")[1].split(":")[0])
        w.port_variable.set(read.split("://")[1].split(":")[1])
        w.refresh()

    w.mainloop()


if __name__ == '__main__':
    main()
