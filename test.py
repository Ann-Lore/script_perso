import unittest
import os
from consolidation import consolidation_fichiers
from analyse import recherche
from rapport import generer_rapport

class TestCSVOperations(unittest.TestCase):

    def setUp(self):
        """Prépare les fichiers temporaires pour les tests."""
        self.files = ["test_departement1.csv", "test_departement2.csv"]
        self.output_file = "test_stock.csv"

        # Créer des fichiers CSV pour les tests
        with open(self.files[0], 'w', encoding='utf-8') as f:
            f.write("Produit,Quantite,Prix,Categorie\n")
            f.write("ProduitA,10,5.0,Mobilier\n")
            f.write("ProduitB,20,15.0,Art\n")

        with open(self.files[1], 'w', encoding='utf-8') as f:
            f.write("Produit,Quantite,Prix,Categorie\n")
            f.write("ProduitA,5,5.0,Mobilier\n")
            f.write("ProduitC,30,20.0,Technologie\n")

    def tearDown(self):
        """Supprime les fichiers temporaires après les tests."""
        for file in self.files:
            if os.path.exists(file):
                os.remove(file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists("rapport.txt"):
            os.remove("rapport.txt")

    def test_consolidation_fichiers(self):
        """Teste la consolidation de fichiers CSV."""
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=False, line_to_modify=None, new_data=None)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 4)  # 1 header + 3 lignes consolidées
        self.assertIn("ProduitA,15,5.0,Mobilier\n", lines)
        self.assertIn("ProduitB,20,15.0,Art\n", lines)
        self.assertIn("ProduitC,30,20.0,Technologie\n", lines)

    def test_append_line(self):
        """Teste l'ajout d'une nouvelle ligne au fichier consolidé."""
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=False, line_to_modify=None, new_data=None)
        consolidation_fichiers(self.files, self.output_file, append=True, new_line="ProduitD,10,25.0,Loisir", update=False, line_to_modify=None, new_data=None)

        with open(self.output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertIn("ProduitD,10,25.0,Loisir\n", lines)

    def test_update_line(self):
        """Teste la mise à jour d'une ligne existante."""
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=False, line_to_modify=None, new_data=None)
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=True, line_to_modify="ProduitA,15,5.0,Mobilier", new_data="ProduitA,20,6.0,Mobilier")

        with open(self.output_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.assertIn("ProduitA,20,6.0,Mobilier\n", lines)

    def test_recherche_par_produit(self):
        """Teste la recherche d'un produit spécifique."""
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=False, line_to_modify=None, new_data=None)

        with self.assertLogs(level='INFO') as log:
            recherche(self.output_file, nom_produit="ProduitA", categorie=None, prix_min=None, prix_max=None)

        self.assertIn("Le produit ProduitA est présent", log.output[0])

    def test_generer_rapport(self):
        """Teste la génération d'un rapport."""
        consolidation_fichiers(self.files, self.output_file, append=False, new_line=None, update=False, line_to_modify=None, new_data=None)
        generer_rapport(self.output_file)

        self.assertTrue(os.path.exists("rapport.txt"))
        with open("rapport.txt", 'r', encoding='utf-8') as f:
            content = f.read()

        self.assertIn("Nombre de produits total", content)
        self.assertIn("Prix total du stock", content)

if __name__ == "__main__":
    unittest.main()
