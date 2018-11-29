class Vendedor:
    def __init__(self, nome, cpf, matricula):
        self.nome = nome
        self.cpf = cpf
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_matricula(self):
        return self.matricula

    def get_dados(self):
        return self.nome, self.cpf, self.matricula
