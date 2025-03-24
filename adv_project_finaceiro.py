import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("dados_escritorio.xlsx")
df_cut = df[['Advogado', 'Status', 'Receita (R$)', 'Custo (R$)']]
df_finc = df_cut.loc[df_cut['Status'] != 'Ativo']

col_adv = list(df['Advogado'])
list_adv = list(dict.fromkeys(col_adv))

# Lucro por médio por caso

list_lucro_med = {}

for adv in list_adv:
    df_lucro = df_finc.loc[df_finc['Advogado'] == adv]
    col_lucro = list(df_lucro['Receita (R$)'] - df_lucro['Custo (R$)'])

    divisor = len(col_lucro)
    if divisor == 0:
        divisor = 1
    lucro = sum(col_lucro)
    lucro_med = lucro / divisor
    list_lucro_med[adv] = lucro_med

# Gerar tabela (arquivo xlsx) com a relação entre advogados e lucro

df_x = pd.DataFrame(list(list_lucro_med.items()), columns=['Advogados', 'Lucro Médio (R$)'])
df_x.to_excel('lucro_medio_por_advogado.xlsx', index=False)
