# Peça a temperatura em Fahrenheit e exiba o valor convertido para Celsius.
print(30*'-','CONVERSÃO DE TEMPERATURA',30*'_')
temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
print()
temp_celsius = (temp_fahrenheit - 32) * 5/9
print(f"A temperatura em Celsius é: {temp_celsius:.2f}")
print()