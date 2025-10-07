
# concatenação
# quebra de linha
# formatando decimais
# alterando vírgula e ponto
# if else
import this

nome = "Isabella"
idade = 17
altura = 1.60

# saída de dados
print ('Olá, meu nome é,' + nome + ', tenho ' + str(idade) + ' anos.')

#FIXME - concatenação com + 
print ('Olá, meu nome é,', nome, ', tenho ',idade, ' anos.')

#FIXME - concatenação com format
print ('Olá, meu nome é {}, tenho {} anos.'.format(nome,idade))

#FIXME - concatenação com f-string
print (f'Olá, meu nome é {type(nome)}, e tenho {idade+1} anos.')

# elimando quebra de linha 
print('O sábio sabia', end='')
print('que o sabiá sabia assobiar.')

valor = 1.20000000

# exibindo o valor com duas casas depois da virgula
print(f'{valor:.2f}')

print(50*'=')
peso = input('Digite seu peso: ').replace(',', '.')
peso = float(peso)
print(f'{peso:.2f}').replace('.', ',')

print(30*'-','programa de boas-vindas',30*'_') 

# programa de boas-vindas
nome_usuario = input("Digite seu nome: ")
print('Seja bem-vindo ao sistema python',nome_usuario)
print() 

print(30*'-','programa de variaveis',30*'_') 

# variáveis 
nome = "Isabella"
idade = 17
altura = 1.60
ativo= True

print("O tipo da variavel nome é: ",type(nome))
print("O tipo da variavel idade é: ",type(idade))
print("O tipo da variavel altura é: ",type(altura))
print("O tipo da variavel ativo é: ",type(ativo))


print(30*'-','programa de condicional',30*'_') 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print('Antes do if')
if idade>=18:
    print(f"Você é maior de idade.")
    print('Você está dentro do bloco IF')
else:
    print(f"Você é menor de idade.")
    print('Você está dentro do bloco ELSE')
    print('Você está fora da da estrutura condicional if else')

print(40*'-','Boletim escolar',40*'_') 
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))   
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

# >= 7: aprovado
# >= 5: recuperação
# reprovado
if media >=7:
    print(f'{nome_aluno}!Aluno aprovado!')
    print(f'Nota 1: {nota1}| Nota 2: {nota2}')
    print(f'Nota 3: {nota3}| Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')

elif media >= 5:
    print(f'{nome_aluno}!Aluno em recuperação!')
    print(f'Nota 1: {nota1}| Nota 2: {nota2}')
    print(f'Nota 3: {nota3}| Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')

else:
    print(f'{nome_aluno}!Aluno reprovado!')
    print(f'Nota 1: {nota1}| Nota 2: {nota2}')
    print(f'Nota 3: {nota3}| Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')

print()
print(30*'-','programa de variaveis',30*'_')
# variaveis
nome = "Isabella"
idade = 11
altura = 1.60

# verifica se o usuário posui os requisitos mínimos
if idade >= 12 and altura >= 1.20:
    print(f'A entrada de {nome} está liberada.')
else:
    print(f'A entrada de {nome} não está liberada.')

