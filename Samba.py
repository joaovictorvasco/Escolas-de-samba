import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data from Wikipedia
url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'
df = pd.read_html(url, match='Período')[1]

# Clean and transform data
df = df.drop(columns=['#'])
df.columns = ['Escola de Samba', 'Período', 'Títulos']
df['Período'] = df['Período'].str.split('-').str[0].astype(int)

# Streamlit header
st.header('As maiores campeãs do carnaval carioca')

# Slider for selecting year range
min_year = int(df['Período'].min())
max_year = int(df['Período'].max())
selected_years = st.slider('Selecione o intervalo de anos:', min_year, max_year, (min_year, max_year))

# Filter the DataFrame based on the selected year range
filtered_df = df[(df['Período'] >= selected_years[0]) & (df['Período'] <= selected_years[1])]

# Aggregate titles by school within the selected year range
aggregated_df = filtered_df.groupby('Escola de Samba')['Títulos'].sum().reset_index()

# Display the filtered DataFrame
st.write(aggregated_df)

# Create and display the bar chart
fig, ax = plt.subplots()
ax.bar(aggregated_df['Escola de Samba'], aggregated_df['Títulos'])
ax.set_xlabel('Escola de Samba')
ax.set_ylabel('Títulos')
ax.set_xticklabels(aggregated_df['Escola de Samba'], rotation=90)

st.pyplot(fig)

