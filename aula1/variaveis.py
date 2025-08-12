

print(30*'-','nome',30*'_') 
print("    ")
# Nome
nome = "Isabella"
# Ano de nascimento
ano_de_nascimento = 2008
# Idade
idade = 17

print("Ola, me chamo",nome, ",tenho",idade, "anos " "e nasci em",ano_de_nascimento,".")



nome = "Isabella"
idade = 17
altura = 1.60
ativo= True

print("O tipo da variavel nome é: ",type(nome))
print("O tipo da variavel idade é: ",type(idade))
print("O tipo da variavel altura é: ",type(altura))
print("O tipo da variavel ativo é: ",type(ativo))
print("    ")
print("    ")


# Operadores
print(30*'-','operadores',30*'-')
print("    ")

n1 = 10
n2 = 5

soma = n1+n2
divisao = n1/n2 # divisao comum
divisao_inteira = n1 // n2 #divisao_inteira
multiplicaçao = n1*n2
exponenciaçao = n1 ** n2
subtraçao = n1-n2
resto = n1 %2 

print('Resultado da soma',n1, "+", n2, "é: ",soma)
print('Resultado da divisao',n1, "/", n2, 'é: ',divisao)
print('Resultado da divisao',n1, "//", n2,'é: ',divisao_inteira)
print('Resultado da multiplicaçao',n1, "*", n2, 'é:',multiplicaçao)
print('Resultado da exponenciaçao é:',exponenciaçao)
print('Resultado da subtraçao',n1,"-", n2, 'é: ',subtraçao)
print('Resultado do resto de',n1, 'é:',resto)
print("    ")

print(30*'-','operadores de comparação',30*'-')
# operadores de comparação
n1 > n2
n1 < n2
n1 == n2 
n1 >= n2
n1 <= n2
n1 != n2

ano = 2025
print("ano atual=",ano)
ano += 1 
print("ano acrescido=",ano)
ano -= 1 
print("ano decrecido=",ano)

# Operações lógicas
# AND, OR, NOT

print(30*'-','Entrada de dados',30*'-')

nome_usuario = input("Digite seu nome: ")
print('Seja bem-vindo ao sistema python',nome_usuario)

print()

print(30*'-','Calculadora',30*'-')
print()
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
print("Resultado dos calculos")
print('Resultado da soma',n1, "+", n2, "é: ",soma)
print('Resultado da divisao',n1, "/", n2, 'é: ',divisao)
print('Resultado da divisao',n1, "//", n2,'é: ',divisao_inteira)
print('Resultado da multiplicaçao',n1, "*", n2, 'é:',multiplicaçao)
print('Resultado da exponenciaçao é:',exponenciaçao)
print('Resultado da subtraçao',n1,"-", n2, 'é: ',subtraçao)
print('Resultado do resto de',n1, 'é:',resto)
print()

print(30*'-','Convertendo tipos dados',30*'-')
print()

ano_nascimento = input("Digite seu ano de nascimento: ")
print(type(ano_nascimento))

# convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento)) 

n1 = 10 
n2 = 20
print("A soma é: ",n1+n2, type(n1), float(n2))

saudação = input("Digite seu nome: ") 
cpf = input("Digite seu cpf: ")
telefone = input("Digite seu telefone: ")

print(20*'-','Dados pessoais',20*'-')
print("Nome: ",saudação)
print("CPF: ",cpf,'|Telefone: ',telefone)
print(50*'-') 
