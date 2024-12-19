def consolidation_fichiers(csv_files, output_file, append,new_line,update,line_to_modify, new_data):
    """
    Consolide plusieursfichiers CSV en un seul, ajoute une ligne, modifie une ligne par une autre
    PRE :
        csv_files : Liste non vide de chemins vers des fichiers CSV existants.
        output_file : Chemin valide pour le fichier de sortie (doit être accessible en écriture).
        Si append est True, new_line doit être une chaîne formatée comme "Produit,Quantité,Prix,Catégorie".
        Si update est True,
            line_to_modify doit être une chaîne formatée comme "Produit,Quantité,Prix,Catégorie".
            new_data doit être une chaîne formatée comme "Produit,Quantité,Prix,Catégorie".
        Les fichiers CSV doivent respecter le format : 4 colonnes (Produit, Quantité, Prix, Catégorie).
        Les champs Quantité et Prix doivent être respectivement des entiers et des flottants.

    POST :
        Les fichiers CSV sont consolidés dans un fichier unique sans doublons (somme des quantités pour les mêmes produits qui sont uniques).
        Si append est utilisé :
            La nouvelle ligne est ajoutée ou mise à jour dans le fichier consolidé
        Si update est utilisé :
            La ligne spécifiée est modifiée ou ajoutée si elle n'existe pas déjà
        Le fichier output_file est créé ou mis à jour avec les données consolidées
    RAISE : ValueError si un argument est manquant ou mal formé.
    """
    try:
        if new_line:
            new_line = new_line.split(',')
        if line_to_modify:
            line_to_modify = line_to_modify.split(',')
        if new_data:
            new_data = new_data.split(',')


        if not append and not update:
            # Dictionnaire pour regrouper les données par produit
            data_dict = {}

            for file in csv_files:
                with open(file, 'r', encoding='utf-8') as infile:
                    header = infile.readline().strip()  # Lire l'en-tête
                    for line in infile:
                        columns = line.strip().split(',')
                        if len(columns) == 4:
                            produit, quantite, prix, categorie = columns
                            quantite = int(quantite)
                            prix = float(prix)

                            if produit in data_dict:
                                # Ajouter la quantité au produit existant
                                data_dict[produit][0] += quantite
                            else:
                                # Ajouter un nouveau produit
                                data_dict[produit] = [quantite, prix, categorie]
                        else:
                            raise ValueError

                # Écrire le fichier consolidé
            with open(output_file, "w", encoding='utf-8') as outfile:
                outfile.write(header + '\n')  # Écrire l'en-tête une seule fois
                for produit, (quantite, prix, categorie) in data_dict.items():
                    outfile.write(f"{produit},{quantite},{prix},{categorie}\n")

            print(f"Fichiers consolidés avec succès dans {output_file}")

        if append:
            try:
                with open(output_file, 'r', encoding='utf-8') as infile:
                    lines = infile.readlines()

                # Construire un dictionnaire des produits existants
                data_dict = {}
                header = lines[0].strip()  # Conserver l'en-tête
                for line in lines[1:]:
                    columns = line.strip().split(',')
                    if len(columns) == 4:
                        produit, quantite, prix, categorie = columns
                        data_dict[produit] = [int(quantite), float(prix), categorie]

                # Nouvelle ligne à traiter
                if new_line and len(new_line) == 4:
                    produit, quantite, prix, categorie = new_line
                    quantite = int(quantite)
                    prix = float(prix)

                    if produit in data_dict:
                        # Si le produit existe, mettre à jour la quantité
                        data_dict[produit][0] += quantite
                    else:
                        # Ajouter le nouveau produit
                        data_dict[produit] = [quantite, prix, categorie]

                    # Réécrire le fichier avec les données mises à jour
                    with open(output_file, 'w', encoding='utf-8') as outfile:
                        outfile.write(header + '\n')  # Réécrire l'en-tête
                        for produit, (quantite, prix, categorie) in data_dict.items():
                            outfile.write(f"{produit},{quantite},{prix},{categorie}\n")

                    print(f"Ligne ajoutée ou mise à jour avec succès dans {output_file}")
                else:
                    print(f"Aucune donnée spécifiée pour l'ajout ou erreur dans les données")
                    raise ValueError("Aucune donnée spécifiée pour l'ajout ou erreur dans les données")

            except Exception as e:
                print(f"Erreur lors de l'ajout des données : {e}")
                raise ValueError(f"Erreur lors de l'ajout des données : {e}")

        if update:
            try:
                if line_to_modify and len(line_to_modify) == 4 and new_data and len(new_data) == 4:
                    # Lire les lignes du fichier de sortie
                    with open(output_file, 'r', encoding='utf-8') as infile:
                        lines = infile.readlines()

                    # Créer un dictionnaire pour stocker les lignes mises à jour
                    updated_lines = []
                    modified = False

                    # Créer un dictionnaire des produits existants
                    header = lines[0].strip()  # Conserver l'en-tête
                    updated_lines.append(header + '\n')  # Réécrire l'en-tête une seule fois

                    for line in lines[1:]:  # Ignorer l'en-tête
                        columns = line.strip().split(',')
                        if len(columns) == 4:
                            produit, quantite, prix, categorie = columns
                            if produit == line_to_modify[0]:  # Utiliser line_to_modify[0] directement
                                # Si le produit à modifier est trouvé, le modifier
                                produit, quantite, prix, categorie = new_data
                                quantite = int(quantite)
                                prix = float(prix)
                                updated_lines.append(f"{produit},{quantite},{prix},{categorie}\n")  # Remplacer la ligne
                                modified = True
                            else:
                                updated_lines.append(line)  # Sinon, garder la ligne inchangée

                    # Si le produit n'a pas été trouvé pour modification, l'ajouter
                    if not modified:
                        produit, quantite, prix, categorie = new_data
                        quantite = int(quantite)
                        prix = float(prix)
                        updated_lines.append(f"{produit},{quantite},{prix},{categorie}\n")
                        modified = True

                    # Si des lignes ont été mises à jour, réécrire le fichier
                    if modified:
                        with open(output_file, 'w', encoding='utf-8') as outfile:
                            outfile.writelines(updated_lines)
                        print(f"Ligne modifiée ou ajoutée avec succès dans {output_file}")
                    else:
                        print(f"Aucune ligne trouvée pour l'identifiant {line_to_modify[0]}")
                        raise ValueError(f"Aucune ligne trouvée pour l'identifiant {line_to_modify[0]}")

                else:
                    print("Les données de modification sont invalides.")
                    raise ValueError("Les données de modification sont invalides.")

            except Exception as e:
                print(f"Erreur lors de la mise à jour des données : {e}")
                raise ValueError(f"Erreur lors de la mise à jour des données : {e}")

    except Exception as e:
        print(f"Erreur lors de la consolidation des fichiers : {e}")
        raise ValueError("Erreur lors de la consolidation des fichiers")
