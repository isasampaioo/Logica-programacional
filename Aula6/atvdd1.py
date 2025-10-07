
# Solicite 2 números e exiba o resultado da divisão do 2 pelo 1 com apenas duas casas decimais

print(30*'-','programa de divisão',30*'_')
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

resultado = num2 / num1
print(30*'-','RESULTADO', 30*'-') 
print(f'Resultado da divisão de {num2} pelo {num1} é: {resultado:.2f}')
print()
