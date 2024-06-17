import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'

# Carregar a tabela correta da página da Wikipedia
df = pd.read_html(url, match='Ano')[0]

# Limpar e transformar os dados
df = df[['Ano', 'Escola', 'Enredo']]
df = df.rename(columns={'Ano': 'Ano', 'Escola': 'Escola de Samba', 'Enredo': 'Enredo'})

# Converter a coluna 'Ano' para inteiro
df['Ano'] = df['Ano'].astype(int)

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
