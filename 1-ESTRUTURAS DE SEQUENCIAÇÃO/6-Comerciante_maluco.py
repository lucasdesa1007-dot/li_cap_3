valor = float(input("Digite o valor da prestação: R$ "))

acrescimo = valor * 0.10
valor_acrescido = valor + acrescimo

desconto = valor_acrescido * 0.10
valor_final = valor_acrescido - desconto

prejuizo = valor_acrescido - valor_final

print(f"Valor com acréscimo: R$ {valor_acrescido:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
print(f"Prejuízo do comerciante: R$ {prejuizo:.2f}")
