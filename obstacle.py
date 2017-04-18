# -*-coding:Utf-8 -*-

class Obstacle(object):
	"""docstring for Obstacle"""
	def __init__(self, type_obstacle, position_obstacle):
		# Valeurs possibles : mur, porte, sortie
		self.type = type_obstacle
		# Valeur : objet position
		self.position = position_obstacle
