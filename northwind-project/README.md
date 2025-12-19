# Projet Northwind - Business Intelligence

## Description
Entrepôt de données et dashboard analytique pour l'analyse des commandes Northwind, combinant Power BI et Python. Projet académique de Master 2 Big Data Analytics.

## Objectifs
- Construire un modèle dimensionnel complet
- Développer 6 visualisations avancées avec Python dans Power BI
- Créer un dashboard interactif
- Générer un rapport technique professionnel

## Structure du Projet
```
Northwind_BI_Project/
├── data/
│   ├── raw/           # Documentation des sources
│   └── processed/     # KPI générés (kpi.csv)
├── scripts/
│   └── analysis/      # 6 scripts Python des visualisations
├── reports/
│   ├── rapport.tex    # Rapport LaTeX
│   └── rapport.pdf    # PDF compilé
├── figures/
│   ├── data_model/    # 5 images du modèle
│   ├── visualizations/# 6 images des visualisations
│   └── misc/          # Autres images
├── video/             # Vidéo de présentation
└── powerbi/           # Fichier Power BI (.pbix)
```

## Installation Rapide

### Prérequis
- **Power BI Desktop** : https://powerbi.microsoft.com/fr-fr/desktop/
- **Python 3.8+** : https://www.python.org/downloads/

### Étapes
1. **Cloner le dépôt**
   ```
   git clone [URL_DU_DEPOT]
   cd Northwind_BI_Project
   ```

2. **Installer Python**
   ```
   pip install pandas matplotlib numpy seaborn
   ```

3. **Ouvrir le projet Power BI**
   - Ouvrir `powerbi/Northwind.pbix`
   - Activer Python : Fichier → Options → Scripting Python

## Visualisations Développées

1. **Top 10 Clients** - Identifier les meilleurs clients (Barres horizontales)
2. **Performance Employés** - Évaluer l'efficacité commerciale (Barres groupées + ligne)
3. **Commandes par Ville** - Analyse géographique (Diagramme circulaire)
4. **Évolution Régions** - Suivi temporel performances (Lignes multiples)
5. **Matrice Communication** - Répartition clients/employés (Heatmap)
6. **Impact Rétention** - Corrélation qualité/fidélité (4 graphiques combinés)

## Technologies
- **Power BI** : ETL, dashboarding, Power Query M
- **Python** : pandas, matplotlib, seaborn
- **SQL** : Base de données Northwind
- **LaTeX** : Rapport technique
- **Git** : Versionnement

## Modèle de Données

### Structure Dimensionnelle
```
Dim_Temps (29 périodes)       ┐
DimClient (120 clients)        ├── TF_Commande (878 faits)
Dim_Employee (58 employés)    ┘
```

### Scripts Power Query
- `Dim_Temps.m` : Fusion SQL Server + Excel, suppression doublons
- `DimClient.m` : Clients uniques avec détection automatique colonnes
- `Dim_Employee.m` : Employés avec territoires et régions
- `TF_Commande.m` : Table de faits avec jointures dimensions

## Résultats Clés

### Insights Business
1. **Concentration clients** : Top 10 clients = 40% du volume
2. **Performance régionale** : Région 3 sous 85% de taux livraison
3. **Répartition géographique** : Londres = 22% des commandes
4. **Corrélation qualité/fidélité** : R² = 0.78

### KPI Principaux
- Taux livraison global : 88%
- Commandes totales : 878
- Clients uniques : 120
- Périodes analysées : 29 mois

## Démonstration

Une vidéo de présentation est disponible dans `video/` démontrant :
- Navigation dans le dashboard Power BI
- Fonctionnement des visualisations Python
- Filtres interactifs et analyse ad-hoc

## Documentation

### Fichiers Importants
- `reports/rapport.pdf` : Rapport technique complet
- `scripts/analysis/` : 6 scripts Python des visualisations
- `powerbi/Northwind.pbix` : Dashboard interactif

### Pour Compiler le Rapport
```
cd reports
pdflatex rapport.tex
pdflatex rapport.tex
```

## Auteur

**Bouzidi Mohamed Amine**
Étudiant Master 2 Big Data Analytics
2024

## Contact

- Email : [votre.email@etudiant.univ-xxx.fr]
- LinkedIn : [lien vers votre profil]

## Licence

Projet académique réalisé dans le cadre du Master 2 Big Data Analytics.
© 2024 - Usage académique uniquement.

---

