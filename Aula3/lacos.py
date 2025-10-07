'''
# sistema de calculo de indice de massa (IMC)
-Crie um sistema que calcule o indice de massa corporal do usuario, mostre o valor do IMC na tela,
e retorne se o usuario esta no peso ideal ou se precisa emagrecer ou engordar mais. Utilize a tabela do IMC para definir os valores.
'''
'''
# tabela de classificação 
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso normal
# Entre 25 e 29.9: Sobrepeso
# Entre 30 e 34.9: Obesidade grau I
# Entre 35 e 39.9: Obesidade grau II
# Acima de 40: Obesidade grau III

# calculo IMC
# IMC = peso / (altura x altura) 
print(30*'-','CALCULADORA DE IMC',30*'-')
nome = input("Digite seu nome: ")
peso = float(input('Digite seu peso: ').replace(',', '.'))
altura = float(input('Digite sua altura: ').replace(',', '.'))
IMC = peso / (altura * altura)
print()
print(f'Seu IMC é: {IMC:.2f}')


if IMC <= 18.5:
    print("Classificação: Abaixo do normal")
elif IMC <= 24.9:
    print("Classificação: Peso normal")
elif IMC <= 29.9:
    print("Classificação: Sobrepeso")
elif IMC <= 34.9:
    print("Classificação: Obesidade grau I")
elif IMC <= 39.9:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")
'''
'''
Problema 2: Um elevador de carga possui capacidade para 200 kg. 
Crie um programa que receba do usuario seu peso e o peso da carga e verifica se a carga está autorizada a usar o elevador ou não.
'''
'''
while True:
    
 print(30*'-','ELEVADOR DE CARGA',30*'-')
 limite = 200 
 peso_usuario = float(input("Digite seu peso: ").replace(',', '.'))
 peso_carga = float(input("Digite o peso da carga: ").replace(',', '.'))

 if (peso_total := peso_usuario + peso_carga) <= limite:
    print("Autorizado a usar o elevador.")
 else:
    print("Não autorizado a usar o elevador.")

 opcao = input('Deseja calcular novamente? S - Sim |N - Não').lower()

 if opcao == 'sim':
    continue
 elif opcao == 'não':
    print('Saindo do sistema...')
    break
 else:
    print('Opção inválida') 
'''
'''
print(30*'-','SISTEMA DE CONSOLE 2DS',30*'-')
print('1 - Calculadora IMC')
print('2 - Maioridade')
print('3 - Calculadora')
print('4 - Dados pessoais')
print('5 - Sair')

opcao = input('Digite uma opção: ')
if opcao == '1':
    pass
elif opcao == '2':
    pass
elif opcao == '3':
    ...
elif opcao == '4':
    ...
elif opcao == '5':
    linhas = 15
    j = 1 

    while j <= linhas:
     espaços = linhas - j
     estrelas = 2 * j - 1
     print(" " * espaços + "^" * estrelas)
     j +=1

elif opcao == '6':
  print("Saindo do sistema...")

'''
print(30*'-','DADOS PESSOAIS',30*'-')
nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
telefone = input("Digite seu telefone: ")
dt_nascimento = input("Digite sua data de nascimento: ")
print(80*'=')

while True:
 #menu principal
 print(30*'-','SISTEMA DE CONSOLE 2DS',30*'-')
 print('1 - Calculadora IMC')
 print('2 - Maioridade')
 print('3 - Calculadora')
 print('4 - Dados pessoais')
 print('5 - Feliz Natal!')
 print('6 - Sair')

 opcao = input('Digite uma opção: ')

 if opcao == '1':
     if opcao == '1':
        peso = float(input('Digite seu peso: ').replace (',','.'))
        altura = float(input('Digite sua altura: ').replace(',','.'))
        imc = peso / (altura*altura)
     print()

     if imc <= 18.5:
      print(10*'-','abaixo do normal',10*'-')
     elif imc <= 24.9:
      print(10*'-','normal',10*'-')
     elif imc <= 29.9:
      print(10*'-','exesso de peso',10*'-')
     elif imc >= 30:
      print(10*'-','obesidade',10*'-')
     elif imc >= 35:
      print(10*'-','obesidade II',10*'-')
     elif imc >= 40:
      print(10*'-','obesidade III',10*'-')
     print()
 elif opcao == '2':
   dt_nascimento = int(input("Digite seu ano de nascimento: "))
   ano_atual =2025
   idade = ano_atual - dt_nascimento
   print()
   print(10*'-', nome , 'é maior de idade.' if idade >=18 else 'é menor de idade', 10*'-')
   print()
 elif opcao == '3':
   n1 = int(input("Digite o primeiro nùmero: ")) 
   n2 = int(input("Digite o segundo número: "))
   print()
   soma = n1+n2
   divisao = n1/n2 # divisao comum
   divisao_inteira = n1 // n2 #divisao_inteira
   multiplicaçao = n1*n2
   exponenciaçao = n1 ** n2
   subtraçao = n1-n2
   resto = n1 %2
   print()
   print(10*'-', "Resultado dos calculos", 10*'-')
   print('Resultado da soma',n1, "+", n2, "é: ",soma)
   print('Resultado da divisao',n1, "/", n2, 'é: ',divisao)
   print('Resultado da divisao',n1, "//", n2,'é: ',divisao_inteira)
   print('Resultado da multiplicaçao',n1, "*", n2, 'é:',multiplicaçao)
   print('Resultado da exponenciaçao é:',exponenciaçao)
   print('Resultado da subtraçao',n1,"-", n2, 'é: ',subtraçao)
   print('Resultado do resto de',n1, 'é:',resto)
   print()       

 elif opcao == '4':
     print(50*'-')
     print(f'Nome: {nome} | Telefone: {telefone}  |')
     print(f'CPF: {cpf} | Data de Nascimento: {dt_nascimento} |')
     print()
     print(50*'-')

 elif opcao == '5':
     print(30*'-','FELIZ NATAL!',30*'-')
     print()
     linhas = 15
     j = 1

     while j <= linhas:
         espaços = linhas - j
         estrelas = 2 * j - 1
         print(" " * espaços + "^" * estrelas)
         j +=1
         print()

 elif opcao == '6':
    print("Saindo do sistema...")
    break
 else:
    print('Opção inválida!') 


