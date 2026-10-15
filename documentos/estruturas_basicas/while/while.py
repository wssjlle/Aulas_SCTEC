nome = input("Digite seu nome:")
print(f"seu nome é {nome}")

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
print(f"a soma é {num1 + num2}")

resp = int(input("quantas pessoas? "))
if resp > 8 :
    print("aguarde")
else:
    print("mesa pronta")

num = int(input("Digite um número: "))
if num % 10 == 0:
    print("multiplo de 10")
else:
    print("não é multiplo de 10")

num=10
while num > 0:
    print(num)
    num -= 1
print("fim")

ingrediente = ""
while ingrediente != "sair":
    ingrediente = input("Digite o ingrediente: ")
    print(f"{ingrediente} adicionado!")
print("finalizado")

while True:
    idade = input("Digite a idade: ")
    if idade == "sair":
        break
    elif int(idade) < 3:
        print(f"ingresso para {idade} é gratuito")
    elif int(idade) <= 12:
        print(f"ingresso para {idade} custa R$ 10,00")
    else:
        print(f"ingresso para {idade} custa R$ 15,00")
print("você saiu")

num=0
while num < 20:
    num += 1
    if num % 2 == 0:
        continue
    print(num)


pedidos_pendentes = [
    "pedido_101",
    "pedido_102",
    "pedido_103"
]

pedidos_concluidos = []

while pedidos_pendentes:
    pedido = pedidos_pendentes.pop(0)

    print(f"Processando {pedido}.")
    pedidos_concluidos.append(pedido)

print("\nPedidos concluídos:")

for pedido in pedidos_concluidos:
    print(pedido)

produtos = [
    "notebook",
    "indisponível",
    "mouse",
    "indisponível",
    "teclado"
]

while "indisponível" in produtos:
    produtos.remove("indisponível")

print(produtos)


respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("\nDigite seu nome: ")
    linguagem = input(
        "Qual é sua linguagem favorita? "
    )

    respostas[nome] = linguagem

    continuar = input(
        "Outra pessoa responderá? (sim/não): "
    )

    if continuar.lower() == "não":
        pesquisa_ativa = False

print("\nResultados da pesquisa:")

for nome, linguagem in respostas.items():
    print(
        f"{nome} escolheu {linguagem}."
    )


senha_correta = "python123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido.")
        break

    tentativas_restantes = limite - tentativas

    if tentativas_restantes > 0:
        print(
            f"Senha incorreta. "
            f"Restam {tentativas_restantes} tentativa(s)."
        )
    else:
        print("Acesso bloqueado.")


pedido = {}

while True:
    produto = input(
        "Digite o produto ou 'finalizar': "
    )

    if produto.lower() == "finalizar":
        break

    quantidade = int(
        input("Digite a quantidade: ")
    )

    if produto in pedido:
        pedido[produto] += quantidade
    else:
        pedido[produto] = quantidade

print("\nResumo do pedido:")

if pedido:
    for produto, quantidade in pedido.items():
        print(
            f"{produto.title()}: {quantidade} unidade(s)"
        )
else:
    print("Nenhum produto foi adicionado.")
