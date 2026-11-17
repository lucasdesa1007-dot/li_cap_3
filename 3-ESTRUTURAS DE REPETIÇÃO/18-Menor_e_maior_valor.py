numeros = []

while True:
    numero = int(input("Digite um número (-1 para sair): "))

    if numero == -1:
        break

    numeros.append(numero)

if numeros:
    print(f"Menor valor: {min(numeros)}")
    print(f"Maior valor: {max(numeros)}")
else:
    print("Nenhum número foi informado.")
