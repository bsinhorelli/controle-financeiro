def mostrar_menu():
      print('\n1 - Adicionar Receitas\n2 - Adicionar Despesas\n3 - Ver Resumo Financeiro\n4 - Sair')

def ler_opcao():
      while True:
                  try:
                        opcao = int(input('Escolha uma das opções: '))
                        if opcao in (1,2,3,4):
                              break
                        else:
                              print('Número Inválido!')
                              
                  except ValueError:
                        print('Digite apenas números!')
      
      return opcao

def adicionar_receita():
      receitas = dict()
      receitas['tipo'] = 'Receita'
      
      receitas['descrição'] = input('Descrição da Receita: ')
      
      while True:
            try:
                  receitas['valor (R$)'] = float(input('Digite o valor da receita: R$ '))
                  if receitas['valor (R$)'] > 0:
                        break
                  else:
                        print('Digite um valor positivo!')
            except ValueError:
                  print('Digite um valor Real, Apenas Números!')
      
      return receitas

def adicionar_despesa():
      despesas = dict()
      despesas['tipo'] = 'Despesa'
      
      despesas['descrição'] = input('Descrição da Despesa: ')
      
      while True:
            try:
                  despesas['valor (R$)'] = float(input('Digite o valor da despesa: R$ '))
                  if despesas['valor (R$)'] > 0:
                        break
                  else:
                        print('Digite um valor positivo!')
            except ValueError:
                  print('Digite um valor Real, Apenas Números!')
                  
      return despesas
                       

def main():
      transacoes = []
      
      while True:
            mostrar_menu()
            opcao = ler_opcao()
            
            if opcao == 1:
                  receitas = adicionar_receita()
                  transacoes.append(receitas)
                  print(receitas)
                  
            elif opcao == 2:
                  despesas = adicionar_despesa()
                  transacoes.append(despesas)
                  print(despesas)
                  
            elif opcao == 3:
                  print('Ver Resumo Financeiro')
                  print(transacoes)
            else:
                  print('encerrando programa...')
                  break
      


main()     