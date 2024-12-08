# Programme de Gestion de Stock

## Description

Ce programme permet de consolider plusieurs fichiers CSV contenant des informations sur les produits, d'effectuer des recherches sur ces produits et de générer des rapports détaillés sur le stock. Le format des fichiers CSV est le suivant :  
- **Nom du Produit**  
- **Quantité**  
- **Prix Unitaire (€)**  
- **Catégorie**

## Installation

### Prérequis

- **Python 3.x** doit être installé sur votre machine.
- Les bibliothèques Python suivantes doivent être installées :
  - `argparse`
  - `csv`

### Étapes d'installation

1. Clonez ou téléchargez ce dépôt sur votre machine locale.
2. Ouvrez un terminal et naviguez dans le répertoire du projet.
3. Si vous n'avez pas encore installé Python, téléchargez-le et installez-le.
4. Assurez-vous que `argparse` et `csv` sont installés.

## Utilisation

Le programme se lance à partir de la ligne de commande avec les paramètres suivants.

### Consolidation de fichiers CSV

Pour consolider plusieurs fichiers CSV en un seul, exécutez la commande suivante :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv

### Ajouter une ligne

Pour ajouter une nouvelle ligne au fichier CSV consolidé :

python main.py --files stock.csv --output stock.csv --append --new_line "ProduitJ,60,35.0,Mobilier"

### Modifier une ligne

Pour modifier une ligne existante dans le fichier CSV :

python main.py --files stock.csv --output stock.csv --update --line_to_modify "ProduitJ,60,35.0,Mobilier" --new_data "ProduitK,90,137.0,Art"

### Information sur un produit par son nom

Pour obtenir des informations sur un produit spécifique :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --info_produit "ProduitA"

### Information sur quels produits sont dans une certaine catégorie

Pour obtenir la liste des produits d'une certaine catégorie :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --produit_par_categorie "Mobilier"


### Produits dans une plage de prix

Pour rechercher les produits dans une plage de prix :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_min 10 --prix_max 34.9

### Produits avec un prix inférieur à un certain montant

Pour rechercher les produits avec un prix inférieur à un montant spécifique :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_max 15.75

### Produits avec un prix supérieur à un certain montant

Pour rechercher les produits avec un prix supérieur à un montant spécifique :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_min 10.5

### Générer un rapport global

Pour générer un rapport global du stock :

python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --rapport
