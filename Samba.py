import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from Wikipedia
url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'
df = pd.read_html(url, match='Títulos')[1]
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

# Streamlit header
st.header('As maiores campeãs do carnaval carioca')

# Slider for filtering by number of titles
min_titles = int(df['Títulos'].min())
max_titles = int(df['Títulos'].max())
selected_titles = st.slider('Selecione o número mínimo de títulos para filtrar:', min_titles, max_titles, min_titles)

# Filter the DataFrame based on the selected number of titles
filtered_df = df[df['Títulos'] >= selected_titles]

# Display the filtered DataFrame
st.write(filtered_df)

# Create and display the bar chart
fig, ax = plt.subplots()
ax.bar(filtered_df['Escola de Samba'], filtered_df['Títulos'])
ax.set_xlabel('Escola de Samba')
ax.set_ylabel('Títulos')
ax.set_xticklabels(filtered_df['Escola de Samba'], rotation=90)

st.pyplot(fig)


