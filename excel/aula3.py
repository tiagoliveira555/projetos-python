import pandas as pd

x = pd.read_excel('/home/tiago/PycharmProjectsSnap/projetos/excel/pessoas.xlsx')

print('tabela inteira: ')
print(x)
dados_filtrados = x['Idade'] < 20
print('dados_filtrados: ')
print(x[dados_filtrados])
