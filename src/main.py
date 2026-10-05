import os
os.system('cls')

def mostrar_menu():
      '''Exibe as opções disponíveis no menu principal.'''
      
      print('''1 - Adicionar Receitas
2 - Adicionar Despesas
3 - Ver Resumo Financeiro
4 - Sair''')

def ler_opcao():
      '''lê a opção escolhida do usuário e valida o valor escolhido.'''
      
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
      '''coleta os dados de uma receita, valida o valor e retorna um dicionário com as informações da transação.'''
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
      '''coleta os dados de uma despesa, valida o valor e retorna um dicionário com as informações da transação.'''
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

def resumo_financeiro(transacoes):
      '''exibe as receitas, as despesas, os totais, o saldo final e algumas estatísticas das transações.'''
      
      if not transacoes:
            print('\nNenhuma transação registrada ainda.')
            return
      
      
      receitas = [t for t in transacoes if t['tipo'] == 'Receita']
      despesas = [t for t in transacoes if t['tipo'] == 'Despesa']
      
      
      total_receitas = sum(r['valor (R$)'] for r in receitas)
      total_despesas = sum(d['valor (R$)'] for d in despesas)
      saldo = total_receitas - total_despesas
      
      print('\n' + '=' * 40)
      print('RESUMO FINANCEIRO'.center(40))
      print('=' * 40)
      
      
      print('\nRECEITAS:')
      if receitas:
            for r in receitas:
                  print(f'  {r["descrição"][:24]:<24} R$ {r["valor (R$)"]:>10.2f}')
      else:
            print('  Nenhuma receita registrada.')
      
      
      print('\nDESPESAS:')
      if despesas:
            for d in despesas:
                  print(f'  {d["descrição"][:24]:<24} R$ {d["valor (R$)"]:>10.2f}')
      else:
            print('  Nenhuma despesa registrada.')
      
      
      print('\n' + '-' * 40)
      print(f'{"Total de receitas:":<26} R$ {total_receitas:>10.2f}')
      print(f'{"Total de despesas:":<26} R$ {total_despesas:>10.2f}')
      print(f'{"Saldo final:":<26} R$ {saldo:>10.2f}')
      print('-' * 40)
      
      if saldo > 0:
            print('Você está no azul!')
      elif saldo < 0:
            print('Atenção: você está no vermelho!')
      else:
            print('Seu saldo está zerado.')
      
      
      if total_receitas > 0:
            percentual = total_despesas / total_receitas * 100
            print(f'Você gastou {percentual:.1f}% do que recebeu.')
      
      
      if despesas:
            maior = despesas[0]
            for d in despesas:
                  if d['valor (R$)'] > maior['valor (R$)']:
                         maior = d
      
      print('=' * 40)         
      
                       

def main():
      transacoes = []
      
      while True:
            mostrar_menu()
            opcao = ler_opcao()
            
            if opcao == 1:
                  receitas = adicionar_receita()
                  transacoes.append(receitas)
                  
                  
            elif opcao == 2:
                  despesas = adicionar_despesa()
                  transacoes.append(despesas)
                  
                  
            elif opcao == 3:
                  resumo_financeiro(transacoes)
                  
            else:
                  print('encerrando programa...')
                  break
      


main()     