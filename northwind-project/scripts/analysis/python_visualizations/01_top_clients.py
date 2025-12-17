import pandas as pd
import matplotlib.pyplot as plt

# Colonnes nécessaires : CompanyName, nbr_commande_livrees
top_clients = dataset.groupby('CompanyName')['nbr_commande_livrees']\
    .sum()\
    .sort_values(ascending=False)\
    .head(10)

plt.figure(figsize=(12, 6))
bars = plt.barh(top_clients.index, top_clients.values)
plt.xlabel('Nombre de Commandes Livrées')
plt.title('Top 10 Clients par Commandes Livrées')
plt.gca().invert_yaxis()

# Ajouter les valeurs sur les barres
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2, 
             f'{int(width)}', ha='left', va='center')

plt.tight_layout()
plt.show()