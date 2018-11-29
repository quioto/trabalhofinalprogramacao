class Concessionaria:
    def __init__(self):
        self.carros = []

    def get_carros(self):
        return self.carros

    def adc_carro(self, carro):
        self.carros.append(carro)
    def salv_cars(self):
        file = open('Concessionária.txt', 'w')
        for i in self.carros:
            file.write(str(i.get_dados()))
            file.write('\n')
        file.close()