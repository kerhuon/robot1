# -*-coding:Utf-8 -*-
import sys
from carte import Carte
from position import Position

class Robot:
	"""Classe Robot"""
	def __init__(self, position):
		# Attention ne pas faire self.position = position car passage par référence !
		self.position = Position(position.ligne, position.colonne)	

	def __repr__(self):
		return "Robot à la position ({}, {})".format(self.position.ligne, self.position.colonne)

	def bouger(self, carte, direction, nombre_de_pas = 1):
		for index in range(nombre_de_pas):
			if direction == "n" and self.mouvement_possible(carte, "n"):
				self.position.ligne -= 1
			elif direction == "s" and self.mouvement_possible(carte, "s"):
				self.position.ligne += 1
			elif direction == "e" and self.mouvement_possible(carte, "e"):
				self.position.colonne += 1
			elif direction == "o" and self.mouvement_possible(carte, "o"):
				self.position.colonne -= 1
			else:
				print("MOUVEMENT INTERDIT")
			if self.position.ligne == carte.position_sortie.ligne and self.position.colonne == carte.position_sortie.colonne:
				carte.actualiser_liste_contenu(self.position)
				carte.afficher_liste_contenu()				
				print("\nFélicitations ! Vous avez gagné !")
				sys.exit(0)
			carte.actualiser_liste_contenu(self.position)
			carte.afficher_liste_contenu()
			

	def mouvement_possible(self, carte, direction = "n"):
		condition_est = (carte.liste_contenu[self.position.ligne][self.position.colonne + 1] != Carte.MUR)
		condition_ouest = (carte.liste_contenu[self.position.ligne][self.position.colonne - 1] != Carte.MUR)
		condition_nord = (carte.liste_contenu[self.position.ligne - 1][self.position.colonne] != Carte.MUR)
		condition_sud = (carte.liste_contenu[self.position.ligne + 1][self.position.colonne] != Carte.MUR)
		borne_nord = (self.position.ligne == 0)
		borne_sud = (self.position.ligne == carte.nombre_lignes)
		borne_est = (self.position.colonne == carte.nombre_colonnes)
		borne_ouest = (self.position.colonne == 0)
		if direction == "n":
			return not borne_nord and condition_nord
		elif direction =="s":
			return not borne_sud and condition_sud
		elif direction == "e":
			return not borne_est and condition_est
		elif direction == "o":
			return not borne_ouest and condition_ouest
		else:
			return False


		
		