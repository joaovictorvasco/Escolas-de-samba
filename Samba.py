import pandas as pd
url='https://pt.wikipedia.org/wiki/Lista_de_campe%C3%A3s_do_carnaval_do_Rio_de_Janeiro'
df = pd.read_html(url, match='Títulos')[1]
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

import seaborn as sns
grafico = sns.barplot(data=df, x='Títulos', y='Escola de Samba')
st.write(grafico)
