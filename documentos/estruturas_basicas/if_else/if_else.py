idade = 20

print(idade >= 18)

idade = 18

print(idade == 18)  # True
print(idade != 18)  # False
print(idade > 18)   # False
print(idade >= 18)  # True

linguagem = "Python"

print(linguagem == "python")
print(linguagem.lower() == "python")

idade = 25
possui_documento = True

print(idade >= 18 and possui_documento)

tem_ingresso = False
esta_na_lista = True

print(tem_ingresso or esta_na_lista)


frutas = ["maçã", "banana", "uva"]

print("banana" in frutas)
print("laranja" not in frutas)

if "banana" in frutas:
    print("Banana está disponível.")


idade = 19

if idade >= 18:
    print("Você é maior de idade.")


if idade >= 18:
    print("Você é maior de idade.")
    print("Seu cadastro pode continuar.")


idade = 16

if idade >= 18:
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")


nota = 7.5

if nota >= 9:
    conceito = "Excelente"
elif nota >= 7:
    conceito = "Aprovado"
elif nota >= 5:
    conceito = "Recuperação"
else:
    conceito = "Reprovado"

print(conceito)

habilidades = ["Python", "SQL"]

if "Python" in habilidades:
    print("Possui conhecimento em Python.")

if "SQL" in habilidades:
    print("Possui conhecimento em SQL.")


produtos = ["arroz", "leite", "café"]

for produto in produtos:
    if produto == "leite":
        print("O leite está em promoção.")
    else:
        print(f"Produto: {produto}")


pedidos = []

if pedidos:
    print("Existem pedidos para processar.")
else:
    print("Não existem pedidos.")


produtos_disponiveis = ["arroz", "feijão", "café"]
produtos_solicitados = ["arroz", "leite", "café"]

for produto in produtos_solicitados:
    if produto in produtos_disponiveis:
        print(f"{produto.title()} adicionado.")
    else:
        print(f"{produto.title()} não está disponível.")


#### Exercícios:

idade = 49

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

numero = 0
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número igual a Zero")

nota = 7

if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")


nota1 = 6.9

if nota1 >= 9:
    print("Excelente")
elif nota1 >=7:
    print("Aprovado")
elif nota1 >=5:
    print("Recuperação")
else:
    print("Reprovado") 

usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == "1234":
    print("Você fez login corretamente")
else:
    print("Dados de login incorretos!")

ingresso = False
lista = False

if ingresso or lista:
    print("Você pode entrar")
else:
    print("Você não pode entrar")

lista_frutas = ["banana", "laranja", "pera", "maçã", "abacaxi"]

if "banana" in lista_frutas:
    print("Banana está na lista")
else:
    print("Banana não está na lista")

usuarios = ["editor", "vendedor", "gerente", "cliente", "admin"]

for usuario in usuarios:
    if usuario.lower() == "admin":
        print("Seja bem vindo Administrador!")
    else:
        print("Bem vindo ao sistema!")

usuarios = []
if usuarios:
    for usuario in usuarios:
        if usuario.lower() == "admin":
            print("Seja bem vindo Administrador!")
        else:
            print("Bem vindo ao sistema!")
else:
    print("A lista está vazia")    


produtos_disponiveis = [
    "notebook",
    "mouse",
    "teclado",
    "monitor"
]

produtos_solicitados = [
    "mouse",
    "impressora",
    "monitor"
]

for solicitado in produtos_solicitados:
    if solicitado in produtos_disponiveis:
        print(f"{solicitado} foi adicionado ao pedido")
    else:
        print(f"{solicitado} não está disonível")
print("Pedido finalizado!")

usuarios_existentes = ["Ana","andré","pedro", "alícia", "sabrina"]
usuarios_novos = ["jasmin", "elias", "pedro", "ana"]

usuarios_existentes_lower = []
for usuarios in usuarios_existentes:
    usuarios_existentes_lower.append(usuarios.lower())

for novos in usuarios_novos:
    if novos.lower() in usuarios_existentes_lower:
         print(f"usuário {novos} já está cadastrado")
    else:
        print(f"usuário {novos} não estava cadastrado")

lista_numeros = list(range(1,10))

for numero in lista_numeros:
    print(f"{numero}º")

""" Uma loja utiliza as seguintes regras:

compras abaixo de R$ 100 não recebem desconto;
compras de R$ 100 até menos de R$ 300 recebem 10%;
compras de R$ 300 até menos de R$ 500 recebem 15%;
compras a partir de R$ 500 recebem 20%;
clientes VIP recebem mais 5% de desconto.
Calcule o valor do desconto e o total final. """

valor_compra = 450
vip = True

if valor_compra < 100:
    desconto = 0
elif valor_compra < 300:
    desconto = 10
elif valor_compra < 500:
    desconto = 15
else: 
    desconto = 20

if vip:
    desconto = desconto + 5

total_desconto = valor_compra * (desconto / 100)

print(f"Valor original: R$ {valor_compra:.2f}")
print(f"percentual de desconto aplicado: {desconto}%")
print(f"total de descontos: R$ {total_desconto:.2f}")
print(f"valor final: R$ {valor_compra-total_desconto:.2f}")