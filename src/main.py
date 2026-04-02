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
                  

def main():
      while True:
            mostrar_menu()
            opcao = ler_opcao()
            
            if opcao == 1:
                  print('Adicionar Receita')
            elif opcao == 2:
                  print('Adicionar Despesa')
            elif opcao == 3:
                  print('Ver Resumo Financeiro')
            else:
                  print('encerrando programa...')
                  break
      


main()     