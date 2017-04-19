# -*-coding:Utf-8 -*-

class Position():
	""" ligne et colonne de l'élément.
	(0, 0) est le coin en haut à gauche"""
	def __init__(self, ligne, colonne):
		self.ligne = ligne
		self.colonne = colonne

	def __repr__(self):
		return "({}, {})".format(self.ligne, self.colonne)

	def add(self, direction):
		if direction == "n":
			self.ligne -= 1
		elif direction == "s":
			self.ligne += 1
		elif direction == "e":
			self.colonne += 1
		elif direction == "o":
			self.colonne -= 1