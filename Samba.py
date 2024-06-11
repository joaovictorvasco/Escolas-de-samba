# Carregue as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do CSV
df = pd.read_csv(carnival_champions.csv)

# Plotar os dados
plt.figure(figsize=(10, 6))
plt.barh(df['Escola de Samba'], df['Número de Títulos'], color='skyblue')
plt.xlabel('Número de Títulos')
plt.ylabel('Escola de Samba')
plt.title('Número de Títulos das Escolas de Samba (Últimos 24 Anos)')
plt.show()
