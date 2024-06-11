import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from collections import Counter
 
# URL da Wikipedia com os resultados do Carnaval do Rio de Janeiro
url = "https://pt.wikipedia.org/wiki/Lista_de_campe%C3%B5es_do_carnaval_do_Rio_de_Janeiro"
 
# Fazer a requisição HTTP para obter o conteúdo da página
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
 
# Localizar a tabela com os resultados dos anos 2000 em diante
table = soup.find('table', {'class': 'wikitable'})
 
# Inicializar listas para armazenar os dados
years = []
winners = []
 
# Iterar sobre as linhas da tabela e extrair os dados
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if len(cols) >= 2:
        year = cols[0].text.strip()
        if year.isdigit() and int(year) >= 2000:
            winner_link = cols[1].find('a')
            if winner_link:
                winner = winner_link.text.strip()  # Extrair o texto dentro do link
                years.append(year)
                winners.append(winner)
 
# Contar o número de títulos por escola
winner_counts = Counter(winners)
 
# Preparar os dados para o gráfico
schools = list(winner_counts.keys())
titles = list(winner_counts.values())
 
# Plotar os dados
plt.figure(figsize=(10, 6))
plt.barh(schools, titles, color='skyblue')
plt.xlabel('Número de Títulos')
plt.ylabel('Escola de Samba')
plt.title('Número de Títulos das Escolas de Samba (Desde 2000)')
plt.show()
