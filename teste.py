sal = float(input('Digite seu salário: R$'))
des = sal - (sal * 7.5 / 100) + 30
print(f'Salário Bruto: R${sal:.2f}\n'
      f'Salário Liquido: R${des:.2f}')
