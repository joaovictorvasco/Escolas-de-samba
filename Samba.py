import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'

# Carregar a tabela correta da página da Wikipedia
dfs = pd.read_html(url)
df = dfs[0]  # Assumindo que a primeira tabela é a correta

# Inspecionar as colunas para garantir que estamos pegando as corretas
st.write("Colunas disponíveis na tabela:")
st.write(df.columns)

# Tentar selecionar as colunas corretas
try:
    df = df[['Ano', 'Escola', 'Enredo']]
except KeyError:
    st.error("As colunas 'Ano', 'Escola' e 'Enredo' não foram encontradas na tabela. Verifique os nomes das colunas.")

# Renomear as colunas para padronizar os nomes
df = df.rename(columns={'Ano': 'Ano', 'Escola': 'Escola de Samba', 'Enredo': 'Enredo'})

# Converter a coluna 'Ano' para inteiro
df['Ano'] = pd.to_numeric(df['Ano'], errors='coerce').dropna().astype(int)

# Cabeçalho do Streamlit
st.header('As campeãs do carnaval carioca')

# Slider para selecionar o intervalo de anos
min_year = 1932
max_year = 2024
selected_years = st.slider('Selecione o intervalo de anos:', min_year, max_year, (min_year, max_year))

# Filtrar o DataFrame com base no intervalo de anos selecionado
filtered_df = df[(df['Ano'] >= selected_years[0]) & (df['Ano'] <= selected_years[1])]

# Agrupar títulos por escola de samba dentro do intervalo de anos selecionado
aggregated_df = filtered_df['Escola de Samba'].value_counts().reset_index()
aggregated_df.columns = ['Escola de Samba', 'Títulos']

# Exibir o DataFrame filtrado
st.write(f"Escolas campeãs do carnaval carioca de {selected_years[0]} a {selected_years[1]}")
st.write(filtered_df)

# Criar e exibir o gráfico de barras
fig, ax = plt.subplots()
ax.bar(aggregated_df['Escola de Samba'], aggregated_df['Títulos'])
ax.set_xlabel('Escola de Samba')
ax.set_ylabel('Títulos')
ax.set_xticklabels(aggregated_df['Escola de Samba'], rotation=90)

st.pyplot(fig)

