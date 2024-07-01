import pandas as pd
from tabulate import tabulate

# Dados dos alunos
dados_alunos = {
    'Nome': ['João', 'Maria', 'José', 'Ana'],
    'Idade': [18, 17, 19, 18],
    'Nota': [8.5, 9.0, 7.5, 8.0]
}

# Criar DataFrame
df_alunos = pd.DataFrame(dados_alunos)

# Transformar DataFrame em tabela
tabela = tabulate(df_alunos, headers='keys', tablefmt='pretty')

# Imprimir tabela
print(tabela)
