def recherche(output_file, nom_produit, categorie, prix_min, prix_max):
    """
    Fait une recherche par le nom du produit, par catégorie ou par une tranche de prix
    PRE: output_file : chemin vers le fichier CSV contenant les informations des produits. Le fichier doit être au format CSV : nom, quantité, prix unitaire, catégorie
         nom_produit (str) : le nom du produit à rechercher. Peut être None si aucune recherche par nom n'est effectuée
         categorie (str) : la catégorie des produits à rechercher. Peut être None si aucune recherche par catégorie n'est effectuée
         prix_min (float) : prix minimum. Peut être None si aucune recherche par prix minimum n'est effectuée
         prix_max (float) : prix maximum. Peut être None si aucune recherche par prix maximum n'est effectuée

    POST: Si le produit est trouvé, affiche les détails du produit (quantité, prix et catégorie)
          Si une catégorie est fournie, affiche tous les produits dans cette catégorie
          Si une tranche de prix est fournie, affiche tous les produits dont le prix est compris dans cette tranche ou supérieur ou inférieur
    RAISE: ValueError lors de la lecture du fichier ou de l'analyse des données
    """
    if nom_produit:
        try:
            with open(output_file, 'r', encoding='utf-8') as outfile:
                lines = outfile.readlines()
                l = []
                trouve = False
                for i in lines[1:]:
                    l = i.strip().split(',')
                    if l[0] == nom_produit:
                        trouve = True
                        break
                if trouve:
                    print(f"Le produit {nom_produit} est présent à une quantité {l[1]} à un prix unitaire de {l[2]}€ et est de catégorie {l[3]}")
                else:
                    print(f"Le produit {nom_produit} n'a pas été trouvé")

        except Exception as e:
            print(f"Erreur lors de l'analyse du fichier : {e}")
            raise ValueError("Erreur lors de l'analyse du fichier")

    if categorie:
        try:
            with open(output_file, 'r', encoding='utf-8') as outfile:
                lines = outfile.readlines()
                trouve = False
                produit = []
                for i in lines[1:]:
                    l = i.strip().split(',')
                    if l[3] == categorie:
                        produit.append(l[0])
                        trouve = True
                if trouve:
                    print(f"Les produits pour la catégorie {categorie} sont :")
                    for j in produit:
                        print(j)
                else:
                    print(f"Le produit {nom_produit} n'a pas été trouvé")

        except Exception as e:
            print(f"Erreur lors de l'analyse du fichier : {e}")
            raise ValueError("Erreur lors de l'analyse du fichier")

    if prix_min or prix_max:
        try:
            with open(output_file, 'r', encoding='utf-8') as outfile:
                lines = outfile.readlines()
                trouve = False
                produit = []
                for i in lines[1:]:
                    l = i.strip().split(',')
                    if prix_min is not None and prix_max is not None:
                        if float(prix_min) <= float(l[2]) <= float(prix_max):
                            produit.append(l[0])
                            trouve = True
                    elif prix_min is not None:
                        if float(l[2]) >= float(prix_min):
                            produit.append(l[0])
                            trouve = True
                    elif prix_max is not None:
                        if float(l[2]) <= float(prix_max):
                            produit.append(l[0])
                            trouve = True
                if trouve:
                    if prix_min is not None and prix_max is not None:
                        print(f"Les produits entre {prix_min} et {prix_max} sont :")
                    elif prix_min is not None:
                        print(f"Les produits supérieurs à {prix_min} sont :")
                    elif prix_max is not None:
                        print(f"Les produits inférieurs à {prix_max} sont :")

                    for j in produit:
                        print(j)
                else:
                    print(f"Aucun produit n'a pas été trouvé")

        except Exception as e:
            print(f"Erreur lors de l'analyse du fichier : {e}")
            raise ValueError("Erreur lors de l'analyse du fichier")

