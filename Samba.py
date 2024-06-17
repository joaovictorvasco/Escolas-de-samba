import pandas as pd
df = pd.read_html(url, match='Títulos')[1]
df = df.drop(columns=['#', 'Escola de samba', 'Escola de samba.1']).rename(columns={'Escola de samba.2': 'Escola de Samba'})

import seaborn as sns
sns.barplot(data=df, x='Títulos', y='Escola de Samba')
