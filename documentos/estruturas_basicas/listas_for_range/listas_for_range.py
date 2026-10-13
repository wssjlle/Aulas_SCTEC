alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(aluno)


alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Olá, {aluno}!")
    print("Bem-vindo à aula de Python.\n")


for aluno in alunos:
    print(f"Olá, {aluno}!")

print("Todos os alunos foram chamados.")


for numero in range(1, 6):
    print(numero)

for numero in range(6):
    print(numero)

for numero in range(2,11, 2):
    print(numero)

numeros = list(range(1, 6))

print(numeros)


quadrados = []

for numero in range(1, 6):
    quadrados.append(numero ** 2)

print(quadrados)


notas = [7.5, 8.0, 6.5, 9.0]

print(min(notas))
print(max(notas))
print(sum(notas))
media = sum(notas) / len(notas)
print(media)

quadrados = [numero ** 2 for numero in range(1, 6)]

print(quadrados)


alunos = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda"]

print(alunos[0:3])

for aluno in alunos[:2]:
    print(aluno)


produtos = ["arroz", "feijão", "leite"]
copia_produtos = produtos[:]

produtos.append("café")
copia_produtos.append("açúcar")

print(produtos)
print(copia_produtos)

dimensoes = (1920, 1080)
print(dimensoes[0])

for dimensao in dimensoes:
    print(dimensao)


disciplinas = ["matemática", "português","inglês","história","geografia"]
for disciplina in disciplinas:
    print(disciplina)

alunos = ["maria", "paula", "amélia"]
for aluno in alunos:
    print(f"mensagem de {aluno} recebida.")

print("mensagens finalizadas")   

for i in range(1,11):
    print(i)

numeros_pares = list(range(2,21,2))

for i in numeros_pares:
    print(i)

print(numeros_pares)

multiplos_tres = list(range(3,31,3))
print(multiplos_tres)

quadrados = []
for i in range(1,11):
    quadrados.append(i**2)
print(quadrados)

notas = [7.5, 8.0, 6.5, 9.5, 8.5]
print(f"a menor nota foi {min(notas)}")
print(f"a maior nota foi {max(notas)}")
print(f"a soma das notas foi {sum(notas)}")
print(f"a media de notas foi {sum(notas)/len(notas)}")
print(f"a quantidade de notas foi {len(notas)}")

linguagens = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "Ruby"
]
print(linguagens[0:3])
print(linguagens[1:4])
print(linguagens[-3:])

comidas = ["arroz", "feijão", "macarrão", "carne", "frango"]
comidas_amigo = comidas[:]
comidas.append("cogumelo")
comidas_amigo.append("abóbora")
print(comidas)
print(comidas_amigo)

""" Exercício 11 — Cardápio fixo com tupla
Um restaurante oferece cinco pratos fixos. Armazene-os em uma tupla e mostre cada prato.

Depois, crie uma nova versão do cardápio, substituindo dois pratos.
 """

cardapio = ("arroz", "feijoada", "linguíça", "lagosta", "pizza")

for item in cardapio:
    print(item)

cardapio = ("macarrão", "entreveiro", "linguíça", "lagosta", "pizza")

for item in cardapio:
    print(item)

vendas = [1200, 950, 1430, 870, 1600, 1100, 1350]
for venda in vendas:
    print(venda)

print(f"a maior venda foi {max(vendas)} e a menor venda foi {min(vendas)}")
print(f"o total vendido foi {sum(vendas)}")
print(f"a média de vendas foi {sum(vendas)/len(vendas):.2f}")
print(vendas[:3])

vendas_copia = vendas[:]
vendas_copia.append(3000)

print(vendas)
print(vendas_copia)