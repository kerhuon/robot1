# -*-coding:Utf-8 -*-

class Test:

	REPERTOIRE_CARTES = "cartes/"

	def __init__(self, nom, prenom, nom_de_fichier):
		self.nom = nom
		self.prenom = prenom
		self.nom_de_fichier = nom_de_fichier
		self.contenu = self.charger()
	
	def charger(self):
		"""Contenu brut sous forme de chaine, permet l'affichage pour le joueur"""
		fichier = open(Test.REPERTOIRE_CARTES + self.nom_de_fichier, 'r')
		lecture = fichier.read()
		fichier.close()
		return lecture

	# @property
	# def contenu(self):
	# 	return self.charger()

test = Test("le rohellec", "nico", "facile.txt")
print(test.contenu)
