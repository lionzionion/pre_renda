import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Configurar a página
st.set_page_config(
    page_title="Análise Exploratória da Previsão de Renda",
    page_icon=":bar_chart:",
    layout="wide",
)

# Carregar os dados
renda = pd.read_csv(r'C:\Users\dias_\OneDrive\Desktop\prev_renda\previsao_de_renda.csv')

# Título principal
st.write('# Análise Exploratória da Previsão de Renda')

# Gráficos ao longo do tempo
st.write('## Gráficos ao Longo do Tempo')

# Gráfico 1
st.subheader('Posse de Imóvel x Renda (Histograma)')
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(x='renda', hue='posse_de_imovel', data=renda, ax=ax)
st.pyplot(fig)

# Gráficos 2-8
features = ['posse_de_veiculo', 'qtd_filhos', 'tipo_renda', 'educacao', 'estado_civil', 'tipo_residencia']
st.write('## Gráficos ao Longo do Tempo')

for feature in features:
    st.subheader(f'{feature.capitalize()} x Renda')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='data_ref', y='renda', hue=feature, data=renda, ax=ax)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

# Gráficos Bivariados
st.write('## Gráficos Bivariados')

# Gráficos de barras
for feature in features:
    st.subheader(f'{feature.capitalize()} x Renda (Barplot)')
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=feature, y='renda', data=renda, ax=ax)
    st.pyplot(fig)

