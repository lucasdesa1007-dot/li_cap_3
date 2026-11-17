idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida!")

elif idade < 16:
    print("Não votante.")

elif idade < 18 or idade > 65:
    print("Eleitor facultativo.")

else:
    print("Eleitor obrigatório.")
