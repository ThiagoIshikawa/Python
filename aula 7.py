lista_preco = [100, 200, 300, 400, 500]

#Impostos

#Aliquota 1 - ir = 0.2
#Aliquota 2 - iss = 0.15

for preco in lista_preco:

    imposto_ir = 0.2 * preco
    imposto_iss = 0.15 * preco

    imposto_total = imposto_ir + imposto_iss
    print(f"Imposto total sobre o produto de R${preco}: R${imposto_total}")