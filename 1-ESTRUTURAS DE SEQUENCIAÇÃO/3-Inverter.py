try:
    numero = int(input("Digite um número para invertelo: "))
    print("Número invertido:", int(str(numero)[::-1]))
except ValueError as erro:
    print(f"Erro: {erro}")
