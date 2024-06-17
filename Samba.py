import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Ensure html5lib is installed
try:
    import html5lib
except ImportError:
    st.error("Please install html5lib by running `pip install html5lib`")

# Load data from Wikipedia
url = 'https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'
df_list = pd.read_html(url)

# Display all tables and their columns to understand the structure
table_info = []
for i, table in enumerate(df_list):
    table_info.append(f"Table {i}: Columns: {', '.join(table.columns)}")

st.write("Tables and their columns found on the Wikipedia page:")
for info in table_info:
    st.write(info)

# Assuming the table with columns 'Ano' and 'Escola de samba' is at index 0 (please adjust if different)
df = df_list[0]

# Clean and transform data
df = df.rename(columns={df.columns[0]: 'Ano', df.columns[1]: 'Escola de Samba'})

# Ensure 'Ano' is treated as integer
df['Ano'] = df['Ano'].astype(int)

# Streamlit header
st.header('As maiores campeãs do carnaval carioca')

# Slider for selecting year range
min_year = int(df['Ano'].min())
max_year = int(df['Ano'].max())
selected_years = st.slider('Selecione o intervalo de anos:', min_year, max_year, (min_year, max_year))

# Filter the DataFrame based on the selected year range
filtered_df = df[(df['Ano'] >= selected_years[0]) & (df['Ano'] <= selected_years[1])]

# Aggregate titles by school within the selected year range
aggregated_df = filtered_df['Escola de Samba'].value_counts().reset_index()
aggregated_df.columns = ['Escola de Samba', 'Títulos']

# Display the filtered DataFrame
st.write(aggregated_df)

# Create and display the bar chart
fig, ax = plt.subplots()
ax.bar(aggregated_df['Escola de Samba'], aggregated_df['Títulos'])
ax.set_xlabel('Escola de Samba')
ax.set_ylabel('Títulos')
ax.set_xticklabels(aggregated_df['Escola de Samba'], rotation=90)

st.pyplot(fig)



