# VISUALISATION 1 : MATRICE DE COMMUNICATION - QUI VEND À QUI
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = dataset.copy()
df['Employe'] = df['Nom'] + ' ' + df['Prenom']

# Créer une matrice Employé x Client (Top 10 clients, Top 8 employés)
top_clients = df.groupby('CompanyName')['nbr_commande_livrees'].sum().nlargest(10).index
top_emps = df.groupby('Employe')['nbr_commande_livrees'].sum().nlargest(8).index

df_filtered = df[(df['CompanyName'].isin(top_clients)) & (df['Employe'].isin(top_emps))]

matrice = df_filtered.groupby(['Employe', 'CompanyName'])['nbr_commande_livrees'].sum().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(matrice, annot=True, fmt='g', cmap='YlOrRd', cbar_kws={'label': 'Commandes Livrées'},
            linewidths=0.5, linecolor='gray')
plt.title('Matrice Couverture Clients-Employés\n(Identification des zones de concentration)', 
          fontsize=13, fontweight='bold')
plt.xlabel('Clients (Top 10)', fontweight='bold')
plt.ylabel('Employés (Top 8)', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print("\nAnalyse de concentration :")
total_interactions = (matrice > 0).sum().sum()
print(f"Total interactions: {total_interactions}")
print(f"Clients servis par chaque employé (moyenne): {(matrice > 0).sum(axis=1).mean():.1f}")