import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'

# Carregar a tabela correta da página da Wikipedia
df = pd.read_html(url, match='Títulos')[1]

# Limpar e transformar os dados
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

# Criar um DataFrame expandido com colunas 'Escola de Samba', 'Títulos' e 'Ano'
expanded_data = []

# Iterar pelas linhas do DataFrame original para dividir os anos
for _, row in df.iterrows():
    escola = row['Escola de Samba']
    titulos = row['Títulos']
    anos = row['Anos'].split(',')
    for ano in anos:
        expanded_data.append([escola, titulos, int(ano.strip())])

# Criar o DataFrame expandido
df_expanded = pd.DataFrame(expanded_data, columns=['Escola de Samba', 'Títulos', 'Ano'])

# Converter 'Ano' para datetime
df_expanded['Ano'] = pd.to_datetime(df_expanded['Ano'], format='%Y')

# Cabeçalho do Streamlit
st.header('As maiores campeãs do carnaval carioca')

# Slider para selecionar o intervalo de anos
min_year = df_expanded['Ano'].dt.year.min()
max_year = df_expanded['Ano'].dt.year.max()
selected_years = st.slider('Selecione o intervalo de anos:', min_year, max_year, (min_year, max_year))

# Filtrar o DataFrame com base no intervalo de anos selecionado
filtered_df = df_expanded[(df_expanded['Ano'].dt.year >= selected_years[0]) & (df_expanded['Ano'].dt.year <= selected_years[1])]

# Agrupar títulos por escola de samba dentro do intervalo de anos selecionado
aggregated_df = filtered_df.groupby('Escola de Samba').size().reset_index(name='Títulos')

# Exibir o DataFrame filtrado
st.write(aggregated_df)

# Criar e exibir o gráfico de barras
fig, ax = plt.subplots()
ax.bar(aggregated_df['Escola de Samba'], aggregated_df['Títulos'])
ax.set_xlabel('Escola de Samba')
ax.set_ylabel('Títulos')
ax.set_xticklabels(aggregated_df['Escola de Samba'], rotation=90)

st.pyplot(fig)

