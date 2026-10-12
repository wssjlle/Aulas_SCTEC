frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # maçã
print(frutas[1])  # banana
print(frutas[2])  # uva

print(frutas[-1])  # uva
print(frutas[-2])  # banana

print(f"Minha fruta favorita é {frutas[0]}.")


frutas = ["maçã", "banana", "uva"]

frutas[1] = "laranja"

print(frutas)

frutas = ["maçã", "banana"]
frutas.append("uva")

print(frutas)

alunos = []

alunos.append("Ana")
alunos.append("Carlos")
alunos.append("Mariana")

print(alunos)

frutas = ["banana", "uva"]
frutas.insert(0, "maçã")

print(frutas)

frutas = ["maçã", "banana", "uva"]

del frutas[1]

print(frutas)

frutas = ["maçã", "banana", "uva"]

fruta_removida = frutas.pop()

print(frutas)
print(fruta_removida)

fruta_removida = frutas.pop(0)
print(fruta_removida)

frutas = ["maçã", "banana", "uva"]

frutas.remove("banana")

print(frutas)


nomes = ["Carlos", "Ana", "Bruno"]

nomes.sort()

print(nomes)
nomes.sort(reverse=True)
print(nomes)

nomes = ["Carlos", "Ana", "Bruno"]

print(sorted(nomes))
print(nomes)

nomes = ["Ana", "Bruno", "Carlos"]

nomes.reverse()

print(nomes)


frutas = ["maçã", "banana", "uva"]

print(len(frutas))

frutas = ["maçã", "banana", "uva"]

print(frutas[2])
print(frutas[-1])

print(frutas)
print(len(frutas))


#### Exercícios

linguagens = ["php", "javascript", "python", "cobol", "clipper", "pascal", "java", "basic"]

print(linguagens[0])
print(linguagens[2])
print(linguagens[-1])

nomes = ["Alícia", "Sabrina", "Wanderlei"]

print(f"Oi {nomes[0]}, tudo bem?")
print(f"oi {nomes[1]}, seja bem vinda")
print(f"esse é meu nome: {nomes[2]}")

produtos = ["notebook", "televisão", "mouse"]
print(produtos)
produtos[1] = "teclado"
print(produtos)

tarefas = []

tarefas.append("lavar")
tarefas.append("dobrar")
tarefas.append("guardar")
print(tarefas)

cores = ["azul", "verde"]
cores.insert(0,"vermelho")
cores.append("amarelo")
print(cores)

animais = ["gato", "cachorro", "coelho", "papagaio"]

animais.remove("cachorro")
print(animais)
removido=animais.pop(0)
print(animais)
print(f"o animal removido foi {removido}")
del animais[-1]
print(animais)

cidades=["Florianópolis","Curitiba","Blumenau","Gaspar"]
print(cidades)
print(sorted(cidades))
print(cidades)
cidades.sort()
print(cidades)

convidados = ["Alícia", "Sabrina", "Wanderlei", "Sandra"]
total = len(convidados)
print(f"Serão convidados {total} pessoas.")
