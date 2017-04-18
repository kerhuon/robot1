# -*-coding:Utf-8 -*-

def faire_labyrinthe(nom_de_fichier):
	fichier = open(nom_de_fichier, "r")
	contenu = fichier.readlines()
	labyrinthe = []
	nb_lignes = len(contenu)	
	for index in range(nb_lignes):
		ligne = []
		for truc in contenu[index]:
			if truc == "O": ligne.append("mur")
			if truc == " ": ligne.append("vide")
			if truc == "U": ligne.append("sortie")
			if truc == "X": ligne.append("robot")
			if truc == ".": ligne.append("porte")
		labyrinthe.append(ligne)		
	return labyrinthe

print(faire_labyrinthe("cartes/prison.txt"))

class Test:

	def __init__(self, a, b):
		self.a = a
		self.b = b

	@property
	def fait(self):
		return 2*self.b

	def __repr__(self):
		return "({}, {})".format(self.a, self.b)

test = Test(1,2)
print(test)
print(test.fait)