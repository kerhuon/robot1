# -*-coding:Utf-8 -*-

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os, platform, sys

from carte import Carte
from position import Position
from robot import Robot

#On efface l'écran
def effacer_ecran():	
	version = platform.system().lower()
	if version == "windows":
		os.system('cls')
	else:
		os.system('clear')

# On liste les cartes existantes
def lister_cartes():
	liste_cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):			
			nom_carte = nom_fichier[:-3].lower()
			liste_cartes.append([nom_carte, nom_fichier])
	return liste_cartes

# On efface l'écran, on affiche le logo du jeu
effacer_ecran()
fichier_logo = open("logo.txt", 'r')
logo = fichier_logo.read()
fichier_logo.close()
print(logo)
print("\nBIENVENUE DANS LE JEU DU ROBOT\n")

# Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
liste_cartes = lister_cartes()
for i, element_carte in enumerate(liste_cartes):
	# affiche nom de carte : exemple --> 1 - facile.
	print("  {} - {}".format(i + 1, element_carte[0]))	
	
# Si il y a une partie sauvegardée, on l'affiche, à compléter
sauvegarde = input("Il existe une partie sauvegardée, voulez-vous la continuer (oui/non) ? ")

# Choix de carte
choix = input("Choisissez votre labyrinthe : ")
try:
	choix = int(choix)
except:
	print("Mauvaise saisie")
try:
	carte = Carte(liste_cartes[choix-1][0], liste_cartes[choix-1][1])
except:
	print("Carte non trouvée")
	sys.exit(-1)

# Let's play!!!
print(carte.contenu)
print(carte.liste_contenu)
print(carte.nombre_lignes)
print(carte.nombre_colonnes)
while True:
	reponse = input("\nSaisissez le mouvement souhaité ('quit' pour quitter) : ")
	if reponse == "quit" or reponse == 'q':
		break
	print(carte.contenu)

