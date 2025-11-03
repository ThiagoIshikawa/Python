faturamento = 1200
custo = 700
lucro = faturamento - custo

print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "emailaleatorio@gmail.com"

# maiuscula
email_cliente = email_cliente.upper()
print(email_cliente)

# minuscula
email_cliente = email_cliente.lower()
print(email_cliente)

# @
print(email_cliente.find("@"))

# Python começa a contar do zero # -1 quando não encontrar

#tamanho do texto 

print(len(email_cliente))

#pegar um caractere
print(email_cliente[1])

print(email_cliente[-4])

# pegar um pedaço do texto 
print(email_cliente [:6])

# trocar pedaco de um texto
novo_email = email_cliente.replace("gmail.com, hotmail.com")
print(novo_email)