
# Gerenciador de biblioteca

print(30*'-','Gerenciador de biblioteca',30*'-')
print()

import json
import os

usuario = []
nome_arquivo = ""

usuarios = []

caminho_livros = 'c:/Users/IsabellaPrazeresSamp/Documents/Logica_programacional/Biblioteca/livros.json'

# livros 
if os.path.exists(caminho_livros):
    with open(caminho_livros, 'r', encoding='utf-8') as f:
        usuarios = json.load(f)
else:
    usuarios = []

while True:
    print('1 - Cadastro de livros ')
    print('2 - Listar livros ')
    print('3 - Atualizar lista ')
    print('4 - Excluir livros ')
    print('5 - Sair')


    opcao = input('Digite a opção desejada: ')
    match opcao:
        case '1':
            usuario = {}
            usuario['Livro: '] = input('Informe o Nome do livro: ')
            usuarios.append(usuario)
            with open(caminho_livros, 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)

            print('---Livro cadastrado com sucesso!')
            print()
            continue

        case '2':
            print(30*'-','LISTA DE LIVROS DISPONIVEIS',30*'-')
            for usuario in usuarios:
                for chave in usuario:
                    print(f'{chave.capitalize()} : {usuario.get(chave)}')
                print()
            continue

    
        case '3':
            nome_antigo = input('Digite o nome do livro que deseja atualizar: ').strip()
            encontrado = False
            for usuario in usuarios:
                if usuario['Livro: '].lower() == nome_antigo.lower():
                    novo_nome = input('Digite o novo nome do livro: ').strip()
                    usuario['Livro: '] = novo_nome
                    encontrado = True
                    break
            if encontrado:
                with open(caminho_livros, 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print(f'Livro "{nome_antigo}" atualizado com sucesso!')
                print()
            else:
                print(f'Livro "{nome_antigo}" não encontrado!')
                print()
            continue
        
        case '4':
            nome_excluir = input('Digite o nome do livro que deseja excluir: ').strip()
            novo_usuarios = [usuario for usuario in usuarios if usuario['Livro: '].lower() != nome_excluir.lower()]
            if len(novo_usuarios) < len(usuarios):
                usuarios = novo_usuarios
                with open(caminho_livros, 'w', encoding='utf-8') as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                print(f'Livro "{nome_excluir}" excluído com sucesso!')
                print()
            else:
                print(f'Livro "{nome_excluir}" não encontrado!')
            continue
        
        case '5':
            print('Saindo...')
            break
        