#!/usr/bin/env 
# -*-coding:Utf-8 -*-

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os, platform, sys

from carte import Carte
from position import Position
from robot import Robot

# *************** DEFINITION DES FONCTIONS ***************
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

def logo():
	effacer_ecran()
	try:
		fichier_logo = open("logo.txt", 'r')
		logo = fichier_logo.read()
		fichier_logo.close()
		print(logo)
		print("\nBIENVENUE DANS LE JEU DU ROBOT\n")
	except:
		print("\nBIENVENUE DANS LE JEU DU ROBOT\n")

def usage():
	print("Le but du jeu est de faire sortir le robot du labyrinthe en atteignant la sortie 'U'.")
	print("Vous ne pouvez pas traverser les murs 'O' mais vous pouvez franchir les portes '.'.")
	print("Déplacements : indiquez une direction nord, sud, est ou ouest en tapant 'n', 's', 'e' ou 'o'.")
	print("Le robot peut faire plusieurs pas (9 maximum) en indiquant un chiffre après la direction.")
	print("Exemple 's2' pour deux pas vers le sud.\n")
	
# *************** PLACE AU JEU ***************
def main():
			
	# On efface l'écran, on affiche le logo du jeu
	logo()
	usage()

	# On affiche les cartes existantes
	print("Labyrinthes existants :")
	liste_cartes = lister_cartes()
	for i, element_carte in enumerate(liste_cartes):
		# affiche nom de carte : exemple --> 1 - facile.
		print("  {} - {}".format(i + 1, element_carte[0]))	
		
	# Si il y a une partie sauvegardée, on l'affiche, à compléter
	# TODO : vérif sauvegarde
	sauvegarde = input("Il existe une partie sauvegardée, voulez-vous la continuer (oui/non) ? ")

	# Choix de carte
	choix = input("Choisissez votre labyrinthe : ")
	try:
		choix = int(choix)
	except:
		print("Mauvaise saisie")
	try:
		carte = Carte(liste_cartes[choix-1][0], liste_cartes[choix-1][1])
		robot = Robot(carte.position_robot)
	except:
		print("Carte non trouvée")
		sys.exit(-1)

	# Let's play!!!
	carte.afficher_liste_contenu()
	while True:
		reponse = input("\nSaisissez le mouvement souhaité ('quit' pour quitter) : ")
		reponse = reponse.lower()
		if reponse == "quit" or reponse == 'q':
			print("Au revoir !")
			break
		elif len(reponse) > 2:
			print("Mauvaise saisie")
			usage()
			continue
		robot.bouger(carte, reponse[0])
		

if __name__ == '__main__':
	main()

