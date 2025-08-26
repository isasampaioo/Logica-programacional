# Peça um valor em dólares e exiba o valor correspondente em reais.
print(30*'-','CONVERSÃO DE CAMBIO',30*'_')
valor_dolares = float(input("Digite o valor em dólares: "))
print()
valor_reais = valor_dolares * 5.41
print(f"O valor em reais é: {valor_reais:.2f}")
print()