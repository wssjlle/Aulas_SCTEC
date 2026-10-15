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

