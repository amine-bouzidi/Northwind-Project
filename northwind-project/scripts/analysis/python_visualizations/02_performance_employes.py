import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Colonnes nécessaires : Nom, Prenom, nbr_commande_livrees, RegionID
# Vérifier quelles colonnes sont disponibles
print("Colonnes disponibles :", dataset.columns.tolist())

# Créer la colonne Employe
df = dataset.copy()
df['Employe'] = df['Nom'] + ' ' + df['Prenom']

# Regrouper par employé et RegionID
perf_employe = df.groupby(['Employe', 'RegionID']).agg({
    'nbr_commande_livrees': 'sum',
    'nbr_commande_non_livrees': 'sum'
}).reset_index()

# Calculer le taux de livraison
perf_employe['total_commandes'] = perf_employe['nbr_commande_livrees'] + perf_employe['nbr_commande_non_livrees']
perf_employe['taux_livraison'] = (perf_employe['nbr_commande_livrees'] / perf_employe['total_commandes']) * 100

# Trier et prendre top 15
perf_employe = perf_employe.sort_values('nbr_commande_livrees', ascending=False).head(15)

# Créer la visualisation
fig, ax1 = plt.subplots(figsize=(14, 8))

x = np.arange(len(perf_employe))
width = 0.35

bars1 = ax1.bar(x - width/2, perf_employe['nbr_commande_livrees'], 
                width, label='Livrées', color='green', alpha=0.7)
bars2 = ax1.bar(x + width/2, perf_employe['nbr_commande_non_livrees'], 
                width, label='Non Livrées', color='red', alpha=0.7)

ax1.set_xlabel('Employé')
ax1.set_ylabel('Nombre de Commandes')
ax1.set_title('Performance des Employés (Top 15)')
ax1.set_xticks(x)
ax1.set_xticklabels(perf_employe['Employe'], rotation=45, ha='right')
ax1.legend()

# Deuxième axe pour le taux de livraison
ax2 = ax1.twinx()
ax2.plot(x, perf_employe['taux_livraison'], 'b--', marker='o', 
         label='Taux Livraison (%)', linewidth=2)
ax2.set_ylabel('Taux de Livraison (%)')
ax2.set_ylim(0, 100)
ax2.legend(loc='upper right')

# Ajouter des annotations
for i, (idx, row) in enumerate(perf_employe.iterrows()):
    ax1.text(i - width/2, row['nbr_commande_livrees'] + 1, 
             str(int(row['nbr_commande_livrees'])), ha='center', va='bottom')
    ax1.text(i + width/2, row['nbr_commande_non_livrees'] + 1, 
             str(int(row['nbr_commande_non_livrees'])), ha='center', va='bottom')
    ax2.text(i, row['taux_livraison'] + 2, f"{row['taux_livraison']:.1f}%", 
             ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Afficher un tableau récapitulatif
print("\nTableau récapitulatif de performance :")
print(perf_employe[['Employe', 'RegionID', 'nbr_commande_livrees', 'nbr_commande_non_livrees', 'taux_livraison']])