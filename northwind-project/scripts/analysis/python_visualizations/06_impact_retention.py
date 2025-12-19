# VISUALISATION 1 : IMPACT DU TAUX DE LIVRAISON SUR LA RÉTENTION CLIENTS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = dataset.copy()
df['total_commandes'] = df['nbr_commande_livrees'] + df['nbr_commande_non_livrees']
df['taux_livraison'] = (df['nbr_commande_livrees'] / df['total_commandes'] * 100)

# Segmenter les clients par taux et analyser leur fidélité (nb de commandes = indicateur)
client_seg = df.groupby('CompanyName').agg({
    'total_commandes': 'sum',
    'taux_livraison': 'mean',
    'id_seqClient': 'count'  # Nombre de transactions
}).reset_index()

client_seg.columns = ['CompanyName', 'total_commandes', 'taux_livraison', 'nb_transactions']

# Créer des bacs de taux
client_seg['segment_taux'] = pd.cut(client_seg['taux_livraison'], 
                                     bins=[0, 70, 85, 95, 100],
                                     labels=['Critique (<70%)', 'Faible (70-85%)', 'Bon (85-95%)', 'Excellent (>95%)'])

# Analyser par segment
segment_analysis = client_seg.groupby('segment_taux').agg({
    'total_commandes': ['count', 'sum', 'mean'],
    'taux_livraison': 'mean',
    'nb_transactions': 'mean'
}).reset_index()

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Graph 1 : Nombre de clients par segment
seg_counts = client_seg.groupby('segment_taux').size()
axes[0, 0].bar(range(len(seg_counts)), seg_counts.values, 
               color=['#c0392b', '#f39c12', '#f1c40f', '#27ae60'], alpha=0.8)
axes[0, 0].set_xticks(range(len(seg_counts)))
axes[0, 0].set_xticklabels(seg_counts.index, rotation=45, ha='right')
axes[0, 0].set_ylabel('Nombre de Clients')
axes[0, 0].set_title('Distribution des Clients par Segment de Qualité')
axes[0, 0].grid(axis='y', alpha=0.3)

# Graph 2 : Commandes moyennes par client
seg_cmd = client_seg.groupby('segment_taux')['total_commandes'].mean()
axes[0, 1].bar(range(len(seg_cmd)), seg_cmd.values, 
               color=['#c0392b', '#f39c12', '#f1c40f', '#27ae60'], alpha=0.8)
axes[0, 1].set_xticks(range(len(seg_cmd)))
axes[0, 1].set_xticklabels(seg_cmd.index, rotation=45, ha='right')
axes[0, 1].set_ylabel('Commandes par Client (moyenne)')
axes[0, 1].set_title('Fidélité Clients par Segment de Qualité')
axes[0, 1].grid(axis='y', alpha=0.3)

# Graph 3 : Taux de livraison moyen
seg_taux = client_seg.groupby('segment_taux')['taux_livraison'].mean()
axes[1, 0].bar(range(len(seg_taux)), seg_taux.values, 
               color=['#c0392b', '#f39c12', '#f1c40f', '#27ae60'], alpha=0.8)
axes[1, 0].set_xticks(range(len(seg_taux)))
axes[1, 0].set_xticklabels(seg_taux.index, rotation=45, ha='right')
axes[1, 0].set_ylabel('Taux de Livraison (%)')
axes[1, 0].set_title('Taux Moyen par Segment')
axes[1, 0].set_ylim(0, 105)
axes[1, 0].grid(axis='y', alpha=0.3)

# Graph 4 : Volume total par segment
seg_vol = client_seg.groupby('segment_taux')['total_commandes'].sum()
axes[1, 1].pie(seg_vol.values, labels=seg_vol.index, autopct='%1.1f%%',
               colors=['#c0392b', '#f39c12', '#f1c40f', '#27ae60'], startangle=90)
axes[1, 1].set_title('Répartition du Volume par Segment')

plt.suptitle('Impact du Taux de Livraison sur la Rétention Clients', 
             fontsize=14, fontweight='bold', y=1.00)
plt.tight_layout()
plt.show()

print("\n=== ANALYSE SEGMENTATION CLIENTS ===")
print(client_seg.sort_values('total_commandes', ascending=False)[['CompanyName', 'segment_taux', 'total_commandes', 'taux_livraison']].head(15))