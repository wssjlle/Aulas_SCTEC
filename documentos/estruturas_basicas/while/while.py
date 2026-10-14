numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
numero = 1

while numero <= 5:
    print(numero)
    numero += 1


mensagem = ""

while mensagem != "sair":
    mensagem = input(
        "Digite uma mensagem ou 'sair': "
    )

    if mensagem != "sair":
        print(mensagem)
programa_ativo = True

while programa_ativo:
    mensagem = input(
        "Digite uma mensagem ou 'sair': "
    )

    if mensagem == "sair":
        programa_ativo = False
    else:
        print(mensagem)
while True:
    cidade = input(
        "Digite uma cidade ou 'sair': "
    )

    if cidade == "sair":
        break

    print(f"Você informou: {cidade}")
numero = 0

while numero < 10:
    numero += 1

    if numero % 2 == 0:
        continue

    print(numero)
usuarios_pendentes = [
    "Ana",
    "Bruno",
    "Carla"
]

usuarios_confirmados = []

while usuarios_pendentes:
    usuario = usuarios_pendentes.pop()

    print(f"Confirmando {usuario}.")
    usuarios_confirmados.append(usuario)

animais = [
    "gato",
    "cachorro",
    "gato",
    "coelho",
    "gato"
]

while "gato" in animais:
    animais.remove("gato")

print(animais)

respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("Digite seu nome: ")
    linguagem = input(
        "Qual é sua linguagem favorita? "
    )

    respostas[nome] = linguagem

    repetir = input(
        "Outra pessoa responderá? (sim/não): "
    )

    if repetir.lower() == "não":
        pesquisa_ativa = False

for nome, linguagem in respostas.items():
    print(f"{nome}: {linguagem}")
