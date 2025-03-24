import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df = pd.read_excel("dados_escritorio.xlsx")

coluna_adv = list(df['Advogado'])
advogados = list(dict.fromkeys(coluna_adv))

# Quantos processos cada advogado tem ativo, perdido e ganho

list_ativos = []
list_perdidos = []
list_ganhos = []

status = [list_ativos, list_perdidos, list_ganhos]

for advogado in advogados:
    proc_status = ['Ativo', 'Perdido', 'Ganho']
    df_adv = df.loc[df['Advogado'] == advogado]
    cont = 0

    for proc in proc_status:
        list_status = list(df_adv['Status'])
        count_status = list_status.count(proc)
        st = status[cont]
        st.append(count_status)
        cont += 1

# Plotar gráfico de barras

x = np.arange(len(advogados))

largura = 0.25

plt.bar(x - largura, list_ativos, label=advogados, width=largura, color='skyblue')
plt.bar(x, list_perdidos, label=advogados, width=largura, color='salmon')
plt.bar(x + largura, list_ganhos, label=advogados, width=largura, color='lightgreen')

legend_handles = [
    Line2D([0], [0], marker='o', color='w', markerfacecolor='skyblue', markersize=10, label='Ativos'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='salmon', markersize=10, label='Perdidos'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='lightgreen', markersize=10, label='Ganhos')
]

plt.legend(handles=legend_handles)

plt.xlabel('Advogados')
plt.ylabel('Quantidade de casos')
plt.title(('Quantos Processos Ativos, Perdidos e Ganhadas Cada Advogado Possui').upper())
plt.xticks(x - 0.7, advogados, rotation=28)
plt.yticks(np.arange(0, 5, 1))

plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
