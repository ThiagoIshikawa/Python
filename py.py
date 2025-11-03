class Carros:
    def __init__(self, cor, altura, modelo):
        self.cor = cor 
        self.altura = altura
        self.modelo = modelo 
    def acelerar(self):
        print("O carro acelerou!")
    def parar(self):
        print("O carro parou!")
    def estacionar(self):
        print("O carro estacionou!")

carro1 = Carros ("azul", "1,2", "Toyota")
carro2 = Carros ("vermelho", "1,4", "Honda")

print(f"O carro é {carro1.cor}, de altura {carro1.altura} e de modelo {carro1.modelo}")
print(f"O carro é {carro2.cor}, de altura {carro2.altura} e de modelo {carro2.modelo}")

