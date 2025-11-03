class Veiculos:
    def __init__(self, cor, modelo, altura):
        self.cor = cor
        self.modelo = modelo
        self.altura = altura
    
    def acelerar(self):
        print("O carro acelerou!")
    def frear(self):
        print("O carro freou!")
    def buzinar(self):
        print("O carro buzinou!")
    
carro1 = Veiculos ("azul", "Toyota", "12m")
carro2 = Veiculos ("amarelo", "Fiat", "10m")

print(f"O carro é {carro1.cor}, seu modelo é {carro1.modelo} e de {carro1.altura}")
print(f"O carro é {carro2.cor}, seu modelo é {carro2.modelo} e de {carro2.altura}")