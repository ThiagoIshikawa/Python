faturamento = 1200 # tipo: int -> numero inteiro
custo = 700.0 # tipo: float -> numero com casa decimal

imposto = faturamento * 0.1

lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("O faturamento foi de R$",faturamento)
print("O custo foi de R$", custo)
print("O lucro foi de R$", lucro)
print("A margem de lucro foi de R$",round (margem_lucro, 3))
mensagem = "faturamento da loja foi de tanto"
email = "emaildequalquer@gmail.com" # tipo: string -> texto
teve_lucro = True # tipo: boolean

# mod -> percentual% - resto da divisao

tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12
print("tempo em meses", tempo_meses)