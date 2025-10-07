# Comparador de preços
while True:
 try:
  etanol = float(input("Digite o preço do etanol: ").replace(",", "."))
  gasolina = float(input("Digite o preço da gasolina: ").replace(",", "."))
  calculo = (etanol / gasolina)
  resultado = "Etanol" if calculo < 0.7 else "Gasolina"

  print(f'Resultado = {calculo:.2f}%. Compensa abastecer com {resultado}.')

  opcao = input('Deseja refazer o calculo? (s/n): ').lower().strip()
  match opcao:
   case 's':
    continue
   case 'n':
    break
   case _:
    print('Opção inválida. Por favor, digite "s" ou "n".')
    continue 
   
 except Exception as e:
  print(f'Não foi possível executar a operação. {e}')
  continue













