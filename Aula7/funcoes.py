
# Crie uma aplicação de banco 

print(30*'-','APLICAÇAO DE BANCO', 30*'-')
class Conta:
    def __init__(self, nome, cpf, numero):
        self.nome = nome
        self.saldo = 0.0
        self.ativa = True
        self.cpf = cpf
        self.numero = numero
        
def menu():
    print("1 - Criar conta")
    print("2 - Exibir dados")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Encerrar conta")
    print("6 - Sair")
    print()
    return input('Digite uma opção: ')
print()

def criar_conta():
    nome = input("Digite seu nome completo: ").strip()
    cpf = input("Digite seu CPF: ").strip()
    numero = input("Digite o número da conta: ").strip()
    return Conta(nome, cpf, numero)



def exibir_dados(conta):
    if not conta:
        print("Conta inexistente.")
        return
    print(f"Nome: {conta.nome}\nCPF: {conta.cpf}\nNumero da conta: {conta.numero}\nSaldo: R${conta.saldo:.2f}\nAtiva: {conta.ativa}")

def depositar(conta):
    v = float(input("Valor depósito: "))
    conta.saldo += v
    print(f"Depósito realizado.\n--Novo saldo: R${conta.saldo:.2f}")

def sacar(conta):
    v = float(input("Valor saque: "))
    if v <= conta.saldo:
        conta.saldo -= v
        print(f"Saque realizado.\n--Novo saldo: R${conta.saldo:.2f}")
        print()
    else:
        print("Saldo insuficiente.")

def encerrar_conta(conta):
    conta.ativa = False
    print("Conta encerrada.")

conta = None
while True:
    op = menu()
    if op == '1':
        conta = criar_conta()
        print("------Conta criada-----\n")
        print()
        
    elif op == '2' and conta:
        exibir_dados(conta)
        print()

    elif op == '3' and conta and conta.ativa:
        depositar(conta)
        print()
    elif op == '4' and conta and conta.ativa:
        sacar(conta)
        print()

    elif op == '5' and conta:
        encerrar_conta(conta)
        print()

    elif op == '6':
        break

    else:
        print("Opção inválida ou conta inexistente.")