# 💰 Sistema de Controle Financeiro

Sistema de controle financeiro pessoal executado no terminal, desenvolvido em Python. Permite registrar receitas e despesas e gerar um resumo com totais, saldo final e estatísticas sobre os gastos.

## 📋 Funcionalidades

- **Adicionar receitas:** registra entradas de dinheiro com descrição e valor
- **Adicionar despesas:** registra saídas de dinheiro com descrição e valor
- **Resumo financeiro**, que exibe:
  - Lista de todas as receitas e despesas
  - Total de receitas e total de despesas
  - Saldo final, com indicação se está positivo, negativo ou zerado
  - Percentual da receita que foi gasto
  - Maior despesa registrada
- **Validação de entradas:** o programa não aceita letras onde se espera número, valores negativos ou opções inexistentes no menu

## 🛠️ Tecnologias

- Python 3 (sem bibliotecas externas)

## 💻 Exemplo de uso

```
1 - Adicionar Receitas
2 - Adicionar Despesas
3 - Ver Resumo Financeiro
4 - Sair
Escolha uma das opções: 3

========================================
           RESUMO FINANCEIRO
========================================

RECEITAS:
  Salário                  R$    1500.00

DESPESAS:
  Aluguel                  R$     800.00
  Mercado                  R$     350.50

----------------------------------------
Total de receitas:         R$    1500.00
Total de despesas:         R$    1150.50
Saldo final:               R$     349.50
----------------------------------------
Você está no azul!
Você gastou 76.7% do que recebeu.
Maior despesa: Aluguel (R$ 800.00)
========================================
```

## 📚 Conceitos praticados

- Funções e modularização do código
- Estruturas de repetição (`while`, `for`) e condicionais
- Tratamento de exceções com `try/except`
- Listas e dicionários
- Formatação de saída com f-strings

## 🚀 Próximas melhorias

- [ ] Salvar as transações em arquivo JSON, para os dados não se perderem ao fechar o programa
- [ ] Adicionar categorias (alimentação, transporte, lazer etc.) com total por categoria
- [ ] Registrar a data de cada transação e permitir resumo por mês
- [ ] Exibir valores no formato brasileiro (R$ 1.500,00)
- [ ] Permitir editar e remover transações

