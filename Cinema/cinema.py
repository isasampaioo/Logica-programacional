
# programa para compra de ingressos de cinema

print(30*'-','COMPRA DE INGRESSOS', 30*'-')
print('Bem-vindo ao programa de compra de ingressos de cinema!')
idade = int(input('Digite a sua idade: '))
print()

while True:
    print("Sala 1, filme: Weapons | Classificação indicativa: 18 anos")
    print("Sala 2, filme: Drácula | Classificação indicativa: 16 anos")
    print("Sala 3, filme: Superman | Classificação indicativa: 14 anos")
    print("Sala 4, filme: F1 | Classificação indicativa: 12 anos")
    print("Sala 5, filme: Sexta-feira muito louca | Classificação indicativa: 10 anos") 
    print('Digite ''sair'' para encerrar o programa.')
    print()
    opcao = input('Escolha um filme: ')
    if opcao == "sair":
        print(30*'-','Programa encerrado!',30*'-')
        break
    if opcao == "Weapons":
        if idade >= 18: 
            print(30*'-','Ingresso comprado',30*'-')
            break
        else:
            print('Você não tem idade suficiente para esse filme.')

    elif opcao == "Drácula":
        if idade >= 16: 
            print(30*'-','Ingresso comprado',30*'-')
            break
        else:
            print('Você não tem idade suficiente para esse filme.')

    elif opcao == "Superman":
        if idade >= 14: 
            print(30*'-','Ingresso comprado',30*'-')
            break
        else:
            print('Você não tem idade suficiente para esse filme.')

    elif opcao == "F1":
        if idade >= 12: 
            print(30*'-','Ingresso comprado',30*'-')
            break
        else:
            print('Você não tem idade suficiente para esse filme.')
            
    elif opcao == "Sexta-feira muito louca":
        if idade >= 10: 
            print(30*'-','Ingresso comprado',30*'-')
            break
        else:
            print('Você não tem idade suficiente para esse filme.')
    else: 
        print('Opção inválida, tente novamente.')