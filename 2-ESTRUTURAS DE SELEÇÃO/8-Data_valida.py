import datetime as dt

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

try:
    data = dt.date(ano, mes, dia)
    print("Data válida!")

except ValueError:
    print("Data inválida!")
