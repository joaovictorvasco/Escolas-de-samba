import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar dados da Wikipedia
url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'
df = pd.read_html(url, match='Títulos')[1]

# Limpar e transformar os dados
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

# Verificar se a coluna 'Anos' existe
if 'Anos' in df.columns:
    # Limpar e transformar os dados na coluna 'Anos'
    def clean_years(years):
        if isinstance(years, str):
            try:
                return [int(year) for year in years.split(',')]
            except ValueError:
                return []
        return []

    df['Anos'] = df['Anos'].apply(clean_years)

    # Explodir a coluna 'Anos' para ter uma linha por cada ano de título
    df_exploded = df.explode('Anos')

    # Converter a coluna 'Anos' para inteiro
    df_exploded['Anos'] = pd.to_numeric(df_exploded['Anos'], errors='coerce').dropna().astype(int)

    # Cabeçalho do Streamlit
    st.header('As maiores campeãs do carnaval carioca')

    # Slider para selecionar o intervalo de anos
    min_year = int(df_exploded['Anos'].min())
    max_year = int(df_exploded['Anos'].max())
    selected_years = st.slider('Selecione o intervalo de anos:', min_year, max_year, (min_year, max_year))

    # Filtrar o DataFrame com base no intervalo de anos selecionado
    filtered_df = df_exploded[(df_exploded['Anos'] >= selected_years[0]) & (df_exploded['Anos'] <= selected_years[1])]

    # Agrupar títulos por escola de samba dentro do intervalo de anos selecionado
    aggregated_df = filtered_df['Escola de Samba'].value_counts().reset_index()
    aggregated_df.columns = ['Escola de Samba', 'Títulos']

    # Exibir o DataFrame filtrado
    st.write(aggregated_df)

    # Criar e exibir o gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(aggregated_df['Escola de Samba'], aggregated_df['Títulos'])
    ax.set_xlabel('Escola de Samba')
    ax.set_ylabel('Títulos')
    ax.set_xticklabels(aggregated_df['Escola de Samba'], rotation=90)

    st.pyplot(fig)
else:
    st.error("A coluna 'Anos' não foi encontrada na tabela.")
