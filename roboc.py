# -*-coding:Utf-8 -*-

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os, carte

from carte import Carte

# On charge les cartes existantes
def charger_cartes():
	cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			# chemin = os.path.join("cartes", nom_fichier)
			nom_carte = nom_fichier[:-3].lower()
			carte = Carte(nom_carte, nom_fichier)
			cartes.append(carte)
	print(cartes)
	return cartes

# Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
liste_cartes = charger_cartes()
for i, carte in enumerate(liste_cartes):
	# affiche nom de carte : exemple --> 1 - facile.
	print("  {} - {}".format(i + 1, carte.nom))

	# affiche carte
	print(liste_cartes[i].contenu)
	print(liste_cartes[i].nom_de_fichier)
	
	print(carte.labyrinthe)
	print('******************************')

	
# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...

