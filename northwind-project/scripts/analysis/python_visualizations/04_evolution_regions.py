# VISUALISATION 5 : ÉVOLUTION TEMPORELLE DES RÉGIONS
import pandas as pd
import matplotlib.pyplot as plt

df = dataset.copy()

# Analyser taux par région et période
region_time = df.groupby(['RegionID', 'mois_annee']).agg({
    'nbr_commande_livrees': 'sum',
    'nbr_commande_non_livrees': 'sum'
}).reset_index()

region_time['total'] = region_time['nbr_commande_livrees'] + region_time['nbr_commande_non_livrees']
region_time['taux'] = (region_time['nbr_commande_livrees'] / region_time['total'] * 100)

fig, ax = plt.subplots(figsize=(14, 7))

regions = sorted(region_time['RegionID'].unique())
colors_list = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']

for i, region in enumerate(regions):
    data = region_time[region_time['RegionID'] == region].sort_values('mois_annee')
    ax.plot(range(len(data)), data['taux'].values, 'o-', linewidth=2.5, markersize=7,
            label=region, color=colors_list[i % len(colors_list)])

ax.axhline(y=90, color='red', linestyle='--', linewidth=2, alpha=0.6, label='Target (90%)')
ax.set_xlabel('Période', fontweight='bold', fontsize=11)
ax.set_ylabel('Taux de Livraison (%)', fontweight='bold', fontsize=11)
ax.set_title('Évolution Temporelle - Performance par Région\n(Tendances, déviations, convergence)', 
             fontsize=13, fontweight='bold')

# Récupérer les labels de mois uniques
periods = region_time['mois_annee'].unique()
ax.set_xticks(range(len(periods)))
ax.set_xticklabels(periods, rotation=45, ha='right')

ax.set_ylim(70, 105)
ax.grid(True, alpha=0.3)
ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.show()

print("\n=== TENDANCE PAR RÉGION ===")
for region in regions:
    data = region_time[region_time['RegionID'] == region].sort_values('mois_annee')
    first_rate = data['taux'].iloc[0]
    last_rate = data['taux'].iloc[-1]
    trend = "↑" if last_rate > first_rate else "↓" if last_rate < first_rate else "="
    print(f"{region}: {first_rate:.1f}% → {last_rate:.1f}% {trend}")