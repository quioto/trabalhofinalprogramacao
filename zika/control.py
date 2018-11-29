from janela_principal2 import Janela_principal
from bd_simulado import Simulado



class Controle:
    def __init__(self):
        self.bd = Simulado()
        self.bd.text_carros()
        self.bd.text_compradores()
        self.bd.text_vendedores()
        self.bd.text_vendas()
        self.jn = Janela_principal(self)
        self.jn.mainloop()
