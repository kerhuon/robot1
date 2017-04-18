# -*-coding:Utf-8 -*

class Carte:

	"""Objet représentant le labyrinthe (modèle) et la carte (vue)."""
	# Parti pris : on ne se trimballe pas avec deux classes : Classe et Labyrinthe

	
	REPERTOIRE_CARTES = "cartes/"

	def __init__(self, nom, nom_de_fichier):
		self.nom = nom
		self.nom_de_fichier = nom_de_fichier
		
	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def donner_position_robot(self):
		pass
	
	@property
	def contenu(self):
		fichier = open(Carte.REPERTOIRE_CARTES + self.nom_de_fichier, 'r')
		return fichier.read()

	@property
	def labyrinthe(self):		
		labyrinthe = []
		nb_lignes = len(self.contenu)	
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

	@classmethod
	def creer_chaine(cls, liste):
		"""Renvoie une chaine de caractères (qui composera le fichier carte.txt)
		à partir d'un objet labyrinthe"""
		nb_lignes = len(liste)
		chaine = ''
		for ligne in liste:
			for element in ligne:
				if element =="mur": chaine += "O"
				if element =="vide": chaine += " "
				if element =="robot": chaine += "X"
				if element =="porte": chaine += "."
				if element =="sortie": chaine += "U"
			chaine += "\n"
		return chaine

	# @classmethod
	# def importer_carte(cls, nom_de_fichier):
	# 	chemin_complet = Carte.REPERTOIRE_CARTES + nom_de_fichier
	# 	fichier = open(chemin_complet, "r")
	# 	contenu = fichier.readlines()
	# 	return contenu

