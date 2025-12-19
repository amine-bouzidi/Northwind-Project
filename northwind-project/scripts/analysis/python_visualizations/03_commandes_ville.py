import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # <-- IMPORT MANQUANT AJOUTÉ ICI

# Colonnes nécessaires : City, nbr_commande_livrees
# Vérification des colonnes disponibles
print("Colonnes disponibles pour ce script :", [col for col in dataset.columns if col in ['City', 'nbr_commande_livrees', 'CompanyName']])

# Agrégation par ville
df = dataset.groupby('City')['nbr_commande_livrees']\
    .sum()\
    .sort_values(ascending=False)\
    .reset_index()

# Calculer les totaux
total_commandes = df['nbr_commande_livrees'].sum()
print(f"Total commandes toutes villes: {total_commandes:,}")

# Prendre top 10 villes
top_n = 10
df_top = df.head(top_n).copy()
autres_total = df.iloc[top_n:]['nbr_commande_livrees'].sum()

# Ajouter la ligne "Autres"
if autres_total > 0:
    df_final = pd.concat([
        df_top,
        pd.DataFrame({'City': ['Autres'], 'nbr_commande_livrees': [autres_total]})
    ])
else:
    df_final = df_top

# Calculer les pourcentages
df_final['pourcentage'] = (df_final['nbr_commande_livrees'] / total_commandes) * 100

# Création du graphique
plt.figure(figsize=(12, 10))

# Palette de couleurs
colors = plt.cm.Set3(np.linspace(0, 1, len(df_final)))

# Diagramme en secteurs
wedges, texts, autotexts = plt.pie(
    df_final['nbr_commande_livrees'], 
    labels=df_final['City'],
    autopct=lambda pct: f'{pct:.1f}%\n({int(pct*total_commandes/100):,})',
    colors=colors,
    startangle=90,
    textprops={'fontsize': 10}
)

# Améliorer la lisibilité
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

plt.title(f'Répartition des Commandes Livrées par Ville\nTotal: {total_commandes:,} commandes', 
          fontsize=14, fontweight='bold')
plt.axis('equal')

# Ajouter une légende avec les valeurs détaillées
plt.legend(
    wedges, 
    [f"{row.City}: {row.nbr_commande_livrees:,} ({row.pourcentage:.1f}%)" 
     for _, row in df_final.iterrows()],
    title="Détails par ville",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1),
    fontsize=9
)

plt.tight_layout()
plt.show()

# Afficher le tableau de données
print("\n" + "="*60)
print("DONNÉES DÉTAILLÉES PAR VILLE")
print("="*60)
print(df_final[['City', 'nbr_commande_livrees', 'pourcentage']].to_string(index=False))