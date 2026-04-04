def mostrar_menu():
      print('\n1 - Adicionar Receita\n2 - Adicionar Despesas\n3 - Ver Resumo Financeiro\n4 - Sair')

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
      
      descricao = input('Descrição da Receita: ')
      receitas['Descrição'] = descricao
      
      while True:
            try:
                  valor = float(input('Digite o valor da receita: R$ '))
                  if valor > 0:
                        break
                  else:
                        print('Digite um valor positivo!')
            except ValueError:
                  print('Digite um valor Real, Apenas Números!')
      receitas['Valor (R$)'] = valor
      
      return receitas
      
      
      
      
      
      
      
                  

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
                  print('Adicionar Despesa')
            elif opcao == 3:
                  print('Ver Resumo Financeiro')
                  print(transacoes)
            else:
                  print('encerrando programa...')
                  break
      


main()     