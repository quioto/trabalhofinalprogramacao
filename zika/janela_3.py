from tkinter import *

class Janela_nome(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.transient(parent)
        self.grab_set()
        self.nome = None
        self.entry = Entry(self)
        self.entry.grid(row=1, column=0)
        Label(self, text='Digite o nome da Concessionária:').grid(row=0, column=0)
        self.btn_ok = Button(self, text='OK', width=10,
                             command=self.ok_click).grid(row=2, column=0, columnspan=1)

    def ok_click(self):
        if self.entry.get():
            self.nome = self.entry.get()
            super().destroy()

    def get_nome(self):
        return self.nome
