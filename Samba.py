# Carregue as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# URL do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/seu-usuario/carnival_champions/main/carnival_champions.csv'

# Carregar os dados do CSV
df = pd.read_csv(url)

# Plotar os dados
plt.figure(figsize=(10, 6))
plt.barh(df['Escola de Samba'], df['Número de Títulos'], color='skyblue')
plt.xlabel('Número de Títulos')
plt.ylabel('Escola de Samba')
plt.title('Número de Títulos das Escolas de Samba (Últimos 24 Anos)')
plt.show()
