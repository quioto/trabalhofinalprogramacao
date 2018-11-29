from tkinter import *
from carro import Carro
from tkinter import messagebox


class Janela_carros(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Carrins')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()
        Label(self, text='').grid(row=0, column=2, padx=20, pady=2)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=2)
        Label(self, text='').grid(row=50, column=0, padx=20, pady=20)

        self.btn_add = Button(self, text='Adicionar carro', command=self.adc_car).\
            grid(row=8, column=1, columnspan=3, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover carro', command=self.remove_car).\
            grid(row=49, column=1, columnspan=3, pady=10, stick=S)

        self.btn_close = Button(self, text='Fechar janela', command=self.destroy, width=10)
        self.btn_close.grid(row=50, column=1, columnspan=3, stick=S, pady=20)

        self.entry_mod_var = StringVar()
        self.entry_mod = Entry(self, textvariable=self.entry_mod_var).\
            grid(row=1, column=3)
        self.lbl_mod = Label(self, text='Modelo').\
            grid(row=1, column=1, stick=E)

        self.entry_marca_var = StringVar()
        self.entry_marca = Entry(self, textvariable=self.entry_marca_var).\
            grid(row=2, column=3)
        self.lbl_mod = Label(self, text='Marca').\
            grid(row=2, column=1, stick=E)

        self.entry_ano_var = StringVar()
        self.entry_ano = Entry(self, textvariable=self.entry_ano_var).\
            grid(row=3, column=3)
        self.lbl_ano = Label(self, text='Ano').\
            grid(row=3, column=1, stick=E)

        self.entry_preco_var = StringVar()
        self.entry_preco = Entry(self, textvariable=self.entry_preco_var).\
            grid(row=4, column=3)
        self.lbl_preco = Label(self, text='Preço de Compra').\
            grid(row=4, column=1, stick=E)
        self.entry_estado_var = StringVar()
        self.entry_estado = Entry(self, textvariable=self.entry_estado_var).\
            grid(row=5, column=3)
        self.lbl_estado = Label(self, text='Estado').\
            grid(row=5, column=1, stick=E)
        self.entry_placa_var = StringVar()
        self.entry_placa = Entry(self, textvariable=self.entry_placa_var).\
            grid(row=6, column=3)
        self.lbl_placa = Label(self, text='Placa').\
            grid(row=6, column=1, stick=E)
        # self.data_compra_var = StringVar()
        # self.entry_data_compra = Entry(self, textvariable=self.entry_data_compra).\
        #     grid(row=7, column=3)
        # self.lbl_data_compra = Label(self, text="Data da compra").\
        #     grid(row=7, column=1, stick=E)

        self.entry_placa_var2 = StringVar()
        self.entry_placa2 = Entry(self, textvariable=self.entry_placa_var2). \
            grid(row=48, column=3)
        self.lbl_placa2 = Label(self, text='Placa'). \
            grid(row=48, column=1, stick=E)

    def adc_car(self):
        modelo = self.entry_mod_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = float(self.entry_preco_var.get())
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        # data_compra = self.entry_data_compra_var.get()
        c = Carro(modelo, marca, ano, estado, preco, placa)
        self.control.bd.adc_carro(c)
        messagebox.showinfo('Carro', f'{placa} foi adicionado.')

    def remove_car(self):
        placa = self.entry_placa_var2.get()
        rmvd = None
        if messagebox.askyesno('Excluir', f'Tem ceteza que deseja excluir o carro: {placa}?') is False:
            return None
        for c in self.control.bd.show_carros():
            if c.get_placa() == placa:
                rmvd = self.control.bd.remove_car(c)
                messagebox.showinfo('Carro', f'{placa} foi removido.')
        if rmvd is None:
            messagebox.showerror('Carro', 'Não há carro cadastrado com estes dados.')

    def destroy(self):
        self.control.bd.salv_carro()
        self.control.jn.atualizar()
        super().destroy()


