dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Não é possível dividir por zero!")
else:
    quociente = 0
    resto = abs(dividendo)
    divisor_absoluto = abs(divisor)

    while resto >= divisor_absoluto:
        resto -= divisor_absoluto
        quociente += 1

    if (dividendo < 0) != (divisor < 0):
        quociente = -quociente

    print(f"Quociente inteiro: {quociente}")
