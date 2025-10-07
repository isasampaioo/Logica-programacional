# importação
import json
try:
    arquivo = input('Digite o nome do arquivo: ').strip().lower()
    
    with open(f'{arquivo}.json', 'r', encoding='utf-8') as f:
        dados = json.load(f) 

    print(f'{"-"*20} DADOS {"-"*20}\n{dados}')
    for dado in dados:
      for chave in dado:
        print(f'{chave.capitalize()}: {dado.get(chave)}')
        print()
        print('-'*40)
except Exception as e:
    print(f'Ocorreu um erro: {e}')

 