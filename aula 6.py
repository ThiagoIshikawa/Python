dic_lista_produtos = {"bola de futebol": 4000, "prancha de surf": 20, "cone": 15}
print(dic_lista_produtos["bola de futebol"])

#editar um item do dicionario

dic_lista_produtos["bola de futebol"] = dic_lista_produtos["bola de futebol"] * 2.3
print(dic_lista_produtos)

#quantidade de items no dic

# print(len(dic_lista_produtos))

#retirar item usando .pop

# dic_lista_produtos.pop("cone")
# print(dic_lista_produtos)

#adicionar item
# dic_lista_produtos["rodinha"] = 300
# print(dic_lista_produtos)

nome_produto = input("Nome do produto: ")
preço_produto = input("Preço do produto")


nome_produto = nome_produto.lower
preco_produto = float(preço_produto)

dic_lista_produtos[nome_produto] = preço_produto
print(dic_lista_produtos)
# if "bola_de_futebol" in dic_lista_produtos:
#     print("Existe")
# else:
#     print("Cadastrar novo produto")

