# -*-coding:Utf-8 -*-
import position
class Robot:
	"""Classe Robot"""
	def __init__(self, position):
		self.position = position

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
				pass

	def mouvement_possible(self, carte, direction = "n"):
		condition_est = (carte.liste_contenu[self.position.ligne][self.position.colonne - 1] != "O")
		condition_ouest = (carte.liste_contenu[self.position.ligne][self.position.colonne +1] != "O")
		condition_nord = (carte.liste_contenu[self.position.ligne - 1][self.position.colonne] != "O")
		condition_sud = (carte.liste_contenu[self.position.ligne + 1][self.position.colonne] != "O")
		borne_nord = (self.position.ligne == 0)
		borne_sud = (self.position.ligne == carte.nombre_lignes - 1)
		borne_est = (self.position.colonne == carte.nombre_colonnes - 1)
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


		
		