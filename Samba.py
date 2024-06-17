import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url='https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'

df = pd.read_html(url, match='Títulos')[1]
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

st.header('As maiores campeãs do carnaval carioca')

st.write(df)

fig, ax = plt.subplots()
ax.plot(df['Títulos'], df['Escola de Samba'])

st.pyplot(fig)


