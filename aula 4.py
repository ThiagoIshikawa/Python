faturamento = 1000
custo = 120
lucro = faturamento - custo



if lucro >= 0:
    print("Lucro de", lucro)
    print("Deu lucro")
else:
    # print("prejuizo de", prejuizo)
    print("Deu prejuizo")

print("Acabou")

# Máquina_mágica_de_idade 

idade = int(input("Escreva sua idade: "))
print(idade)

if idade <= 12:
    print("Voce é uma criança!")
    print("Que legal!")
elif idade <= 17:
    print("Voce é um adolescente!")
    print("Que massa!")
else:
    print("Voce é um adulto!")
    print("Wow, boa sorte com os boletos ksks!")

