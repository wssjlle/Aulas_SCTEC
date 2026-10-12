mensagem = "Olá, mundo!"
print(mensagem)

nome = "Ada Lovelace"
print(nome.title())   # Ada Lovelace
print(nome.upper())   # ADA LOVELACE
print(nome.lower())   # ada lovelace

nome = "Ada"
print(f"Olá, {nome}!")

mensagem = "Isso é uma mensagem"
print(f"{mensagem.upper()}")

status = "Pedido recebido"
print(status)

status = "Pedido enviado"
print(status)

nome_produto = "Café"
qtd_disponivel = 10
preco = 35.5
disponivel = True

print(type(nome_produto))
print(type(qtd_disponivel))
print(type(preco))
print(type(disponivel))

nome_completo = "wanderlei silva dos santos"
print(nome_completo.title())
print(nome_completo.upper())
print(nome_completo.lower())

nome_pessoa = "Wanderlei"
idade_pessoa = 49
print(f"Olá, {nome_pessoa}! você tem {idade_pessoa} anos.")

produto = "Pneu"
qtde = 3
preco = 356.50

total = qtde * preco

print(f"Na compra de {qtde} {produto}, você pagou R$ {total:.2f}.")


valor1 = 10
valor2 = 3

print(f"a soma é: {valor1+valor2}")
print(f"A subtração é: {valor1-valor2}")
print(f"A multiplicação é: {valor1*valor2}")
print(f"A divisão é: {valor1/valor2}")
print(f"A divisão inteira é: {valor1//valor2}")
print(f"O resto da divisão é: {valor1%valor2}")
print(f"A potência é: {valor1**valor2}")

linguagem = "    Python    "

print(f"Original: '{linguagem}'")
print(f"Sem espaços à esquerda: '{linguagem.lstrip()}'")
print(f"Sem espaços à direita: '{linguagem.rstrip()}'")
print(f"Sem espaços nos dois lados: '{linguagem.strip()}'")


nome_do_produto = "Notebook"
preço_unitario = 5_254.10
quantidade = 5
disponibilidade = True

total_estoque = quantidade*preço_unitario

print(f"Ficha do produto {nome_do_produto}:")
print(f"O valor unitário é R$ {preço_unitario:.2f}")
print(f"Temos {quantidade} unidade(s) em estoque")
if (disponibilidade==True):
    print("Produto disponível para venda")
else:
    print("Produto indisponível")
print(f"Valor total do estoque de {nome_do_produto}: R$ {total_estoque:.2f}")

percentual_desconto = 10
preço_camisetas = 40
quantidade_camisetas = 5

valor_sem_desconto = quantidade_camisetas * preço_camisetas
valor_do_desconto = valor_sem_desconto*(percentual_desconto/100)
valor_com_desconto = valor_sem_desconto - valor_do_desconto

print(f"Total sem desconto: R$ {valor_sem_desconto:.2f}")
print(f"Valor do desconto: R$ {valor_do_desconto:.2f}")
print(f"Valor com desconto: R$ {valor_com_desconto:.2f}")

