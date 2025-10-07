
# Peça três números e exiba a média aritmética entre eles

print(30*'-','MÉDIA ARITMÉTICA',30*'_')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
print()
media = (num1 + num2 + num3) / 3
print(f'A média aritmética entre: {num1}, {num2} e {num3} é: \n {media:.2f}')
print()
