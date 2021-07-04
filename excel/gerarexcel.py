import pandas as pd

d = {'Nome': ['Ana', 'Joao', 'Maria'], 'Idade': [20, 45, 38], 'Altura': [1.56, 1.78, 1.73]}

dados = pd.DataFrame(data=d)

print(dados)

dados.to_excel('dados.xlsx', index=False)
