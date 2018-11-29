from tkinter import *
from comprador import Comprador
from tkinter import messagebox


class Janela_comprador(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Comprador')
        self.geometry('370x200+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=10)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=10)

        self.btn_adc = Button(self, text='Adicionar Comprador', command=self.adc_comp). \
            grid(row=4, column=1, pady=10, stick=S)
        self.bt_remove = Button(self, text='Remover Comprador', command=self.remove_vend). \
            grid(row=4, column=3, columnspan=2, pady=10, stick=S)
        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=5, column=1, columnspan=3, stick=S, pady=20)

        self.entry_nome_var = StringVar()
        self.entry_nome = Entry(self, textvariable=self.entry_nome_var). \
            grid(row=1, column=3, padx=1, pady=1)
        self.lbl_nome = Label(self, text='Nome'). \
            grid(row=1, column=1, padx=1, pady=1)

        self.entry_cpf_var = StringVar()
        self.entry_cpf = Entry(self, textvariable=self.entry_cpf_var). \
            grid(row=2, column=3, padx=1, pady=1)
        self.lbl_cpf = Label(self, text='CPF'). \
            grid(row=2, column=1, padx=1, pady=1)

    def adc_comp(self):
        nome = self.entry_nome_var.get()
        cpf = self.entry_cpf_var.get()
        c = Comprador(nome, cpf)
        self.control.bd.adc_comprador(c)
        messagebox.showinfo('O comprador', f'{nome} foi adicionado.')

    def remove_vend(self):
        cpf = self.entry_cpf_var.get()
        rmvd = None
        for comp in self.control.bd.show_comp():
            if cpf == comp.get_cpf():
                if messagebox.askyesno\
                            ('Excluir', f'Tem ceteza que deseja excluir o comprador {comp.get_nome()}?') is False:
                    return None
                rmvd = self.control.bd.remove_comp(comp)
                messagebox.showinfo('Comprador', f'{comp.get_nome()} foi removido.')
        if rmvd is None:
            messagebox.showerror('Comprador', 'Não há comprador cadastrado neste CPF')

    def destroy(self):
        self.control.bd.salv_comprador()
        super().destroy()

