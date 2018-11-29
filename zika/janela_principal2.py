from tkinter import *
from tkinter import messagebox
from janela_comprador import Janela_comprador
from janela_vendedor import Janela_vendedor
from janela_carros import Janela_carros
from janela_venda import Janela_venda
from notafiscal import Janela_Nota_Venda



class Janela_principal(Tk):
    def __init__(self, control):
        self.control = control
        super().__init__()
        self.title('Concessionária')
        self.geometry('350x200+200+200')
        Label(self, text='Concessionária do JP').grid(row=0, column=0, pady=5, columnspan=20, stick=N)

        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy).\
            grid(row=500, column=5, padx=10, columnspan=10, pady=90, stick=S)

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        self.menu = Menu(self)
        self.menucascata = Menu(self.menu, tearoff=0)
        self.menucascata.add_command(label='Vendedor', command=self.janela_vendedor)
        self.menucascata.add_command(label='Comprador', command=self.janela_comprador)
        self.menucascata.add_command(label='Carro', command=self.janela_carros)
        self.menucascata.add_separator()
        self.menucascata.add_command(label='Sair', command=self.destroy)
        self.menu.add_cascade(label='Menu', menu=self.menucascata)
        self.config(menu=self.menu)

        self.carregar_carros()

    def carregar_carros(self):
        r = 2
        c = 0
        for asd in self.control.bd.show_carros():
            Button(self, width=10, text=f'{asd.get_placa()}', command=lambda carro=asd: self.
                   janela_venda(carro)).grid(row=r, column=c, pady=5)
            c += 1
            if c == 4:
                c = 0
                r += 1
    def atualizar(self):
        for c in self.grid_slaves():
            if type(c) is Button:
                if c['text'] != 'Sair':
                    c.destroy()
        self.carregar_carros()


    def janela_comprador(self):
        Janela_comprador(self, self.control)

    def janela_vendedor(self):
        Janela_vendedor(self, self.control)

    def janela_carros(self):
        Janela_carros(self, self.control)

    def janela_venda(self, carro):
        Janela_venda(self, self.control, carro)
    def janela_nota(self):
        Janela_Nota_Venda(self, self.control)

    def destroy(self):
        if messagebox.askyesno('Sair', 'Tem certeza de que deseja sair?'):
            self.control.jn.atualizar()
            super().destroy()
