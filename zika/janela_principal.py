from tkinter import *
from tkinter import messagebox
from janela_comprador import Janela_comprador
from janela_vendedor import Janela_vendedor
from janela_carros import Janela_carros
from janela_3 import Janela_nome
class Janela_principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        Janela_nome(self)
        self.title(f'{Janela_nome.nome}')
        self.geometry('400x400+150+150')
        Label(self, text='Menu').grid(row=0, column=0, pady=10, columnspan=3)
        self.btn_carros = Button(self, width=10, text='Carros',
                                 command=self.janela_carros).grid(row=1, column=2, padx=5)
        self.btn_comprador = Button(self, width=10, text='Comprador',
                                    command=self.janela_comprador).grid(row=1, column=0, padx=5)
        self.btn_vendedor = Button(self, width=10, text='Vendedor',
                                   command=self.janela_vendedor).grid(row=1, column=1, padx=5)
        self.btn_close = Button(self, width=10, text='Sair',
                         command=self.destroy).grid(row=2, column=0, padx=5, columnspan=3, pady=5)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        r = 0
        c = 0
        for a in self.control.carros:
            self.a_carro = Button(self, width=10, text=f'{a[4]}').grid(row=r, column=c)
            c += 1
            if c == 2:
                c = 0
                r += 1



    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza de que deseja sair?'):
            super().destroy()

    def janela_comprador(self):
        Janela_Comprador(self)

    def janela_vendedor(self):
        Janela_Vendedor(self)

    def janela_carros(self):
        Janela_Carros(self)
    def atualizar_patio(self):
        for c in self.grid_slaves():
            if type(c) is Button:
                if c['text'] != 'Sair':
                    c.destroy()
        self.carregar_carros()