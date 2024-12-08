def generer_rapport(output_file):
    """
    Génère un rapport sur les produits stockés dans un fichier CSV et l'enregistre dans un fichier texte
    PRE:
     output_file : chemin vers le fichier CSV contenant les informations des produits. Le fichier doit être au format CSV: nom, quantité, prix unitaire, catégorie
    POST: Affiche les informations suivantes à la console :
           Le nombre de produits par catégorie
           Le nombre total de produits en stock
           La valeur totale du stock en euros
           Le prix moyen par article en stock
          Crée un fichier rapport.txt qui contient ces informations
    RAISE: ValueError si une erreur survient lors de la lecture du fichier CSV ou de la génération du rapport
    """
    try :
        with open(output_file, 'r', encoding='utf-8') as outfile:
            lines = outfile.readlines()
            # nbr prod par categ
            dict_categories = {}
            for i in lines[1:]:
                categories = i.strip().split(',')[3]
                if categories not in dict_categories:
                    dict_categories[categories] = [i.strip().split(',')[0]]
                else:
                    dict_categories[categories].append(i.strip().split(',')[0])
            print(dict_categories)
            for i in dict_categories:
                print(f"Pour la catégorie {i}, il y a {len(dict_categories[i])} produits")

            #nombre de prod en stock
            cmt = 0
            for i in lines[1:]:
                cmt += int(i.strip().split(',')[1])
            print(f"Il y a {cmt} produits dans le stock")

            #valeur totale du stock
            prix_total = 0
            for i in lines[1:]:
                prix_total += float(i.strip().split(',')[2])* int(i.strip().split(',')[1])
            print(f"Il y a pour {prix_total:.2f}€ de produits dans le stock")


            #prix moyen par article
            prix_moyen_par_article = prix_total / cmt
            print(f"Le prix moyen par article est de {prix_moyen_par_article:.2f}€")

        with open("rapport.txt", 'w', encoding='utf-8') as file_share:
            for i in dict_categories:
                file_share.write(f"Nombre de produits pour la catégorie {i} : {len(dict_categories[i])}\n")
            file_share.write(f"Nombre de produits total : {cmt} \n")
            file_share.write(f"Prix total du stock: {prix_total:.2f}€ \n")
            file_share.write(f"Prix moyen par article : {prix_moyen_par_article:.2f}€ \n")

    except Exception as e:
        print(f"Erreur lors de la création du rapport globale: {e}")
        raise ValueError("Erreur lors de la création du rapport globale")
