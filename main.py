# python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv
# ajouter une ligne :
    # python main.py --files stock.csv --output stock.csv --append --new_line "ProduitJ,60,35.0,Mobilier"
# modifier une ligne :
    # python main.py --files stock.csv --output stock.csv --update --line_to_modify "ProduitJ,60,35.0,Mobilier" --new_data "ProduitK,90,137.0,Art"

# Info sur un produit :
    # python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --info_produit "ProduitA"

# Produits pour une certaine catégorie
    # python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --produit_par_categorie "Mobilier"
# Produits sup. de 10.5
    # python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_min 10.5

# Produit inf de 15.75
    #  python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_max 15.75
# Produit entre 10 et 34.9
    #python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --analyse --prix_min 10 --prix_max 34.9
# Rapport globale partageable
    #python main.py --files departement1.csv departement2.csv departement3.csv --output stock.csv --rapport

import argparse
from consolidation import consolidation_fichiers
from analyse import recherche
from rapport import generer_rapport

# Fonction principale
def main():
    """
    Fonction principal pour la consolidation des fichiers, de l'analyse et du rapport
    PRE : Les arguments doivent être corrects orthographié
          Les fichiers CSV sont toujours du même format : Nom du Produit,Quantité,Prix Unitaire (€),Catégorie
    POST : Les fichiers CSV sont consolidés, analysés, ou un rapport est généré selon les options
    RAISE : Un fichier n'est pas trouvé
    """
    # Consolidation
    parser = argparse.ArgumentParser(description="Consolider plusieurs fichiers CSV en un seul fichier")
    parser.add_argument("--files", nargs='+', required=True, help="Liste des fichiers CSV à regrouper")
    parser.add_argument("--output", required=True, help="Nom du fichier CSV de sortie")
    parser.add_argument("--append", action='store_true', help="Ajouter des nouvelles données")
    parser.add_argument("--new_line", help=" Nouvvelles données à insérer au format CSV")
    parser.add_argument("--update", action='store_true',help="Modifier une ligne dans le fichier")
    parser.add_argument("--line_to_modify", help="Ligne à mofifer du fichier au format CSV")
    parser.add_argument("--new_data", help="Nouvvelles données à insérer au format CSV")

    # Analyse
    parser.add_argument("--analyse", action='store_true', help="Effectuer une analyse des données après la consolidation")
    parser.add_argument("--info_produit", help="Donne les informations du produit")
    parser.add_argument("--produit_par_categorie", help="Donne les produits pour la catégorie précisée")
    parser.add_argument("--prix_min", help="Donne les produits supérieurs ou égals au prix donné")
    parser.add_argument("--prix_max", help="Donne les produits inférieurs ou égals au prix donné")

    # Rapport
    parser.add_argument("--rapport", action='store_true', help="Fait un rapport du stock")

    args = parser.parse_args()

    try :
        consolidation_fichiers(args.files, args.output, args.append, args.new_line, args.update, args.line_to_modify, args.new_data)

        if args.analyse:
            recherche(args.output, args.info_produit, args.produit_par_categorie, args.prix_min, args.prix_max)

        if args.rapport:
            generer_rapport(args.output)

    except FileNotFoundError:
        raise FileNotFoundError("Les fichiers ne sont pas trouvé")

if __name__ == "__main__":
    main()
