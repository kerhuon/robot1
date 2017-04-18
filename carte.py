# -*-coding:Utf-8 -*

class Carte:

	"""Classe représentant le labyrinthe (modèle) et la carte (vue)."""
	# Parti pris : on ne se trimballe pas avec deux classes : Classe et Labyrinthe
	# Car il s'agit de la même chose : labyrinthe utilisé pour le traitement, carte pour l'affichage

	
	REPERTOIRE_CARTES = "cartes/"

	def __init__(self, nom, nom_de_fichier):
		self.nom = nom
		self.nom_de_fichier = nom_de_fichier
		
	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def donner_position_robot(self):
		numero_ligne = 0		
		for ligne in self.labyrinthe:
			numero_colonne = 0
			for element in ligne:
				if element == "robot":
					return [numero_ligne, numero_colonne]
				numero_colonne += 1
			numero_ligne += 1

	@property
	def nombre_lignes(self):
		return len(self.liste_contenu)

	@property
	def nombre_colonnes(self):
		return len(self.labyrinthe[0])

	@property
	def contenu(self):
		"""Contenu brut sous forme de chaine, permet l'affichage pour le joueur"""
		fichier = open(Carte.REPERTOIRE_CARTES + self.nom_de_fichier, 'r')
		lecture = fichier.read()
		fichier.close()
		return lecture

	@property
	def liste_contenu(self):
		"""Contenu sous forme de liste de n listes (correspondant à n lignes)"""
		chemin_complet = Carte.REPERTOIRE_CARTES + self.nom_de_fichier
		fichier = open(chemin_complet, "r")
		lecture =  fichier.readlines()
		fichier.close()
		return lecture

	@property
	def labyrinthe(self):
		"""Objet labyrinthe sous forme de liste de listes.
			Valeurs possibles : mur, vide, sortie, robot, porte..."""	
		labyrinthe = []
		for numero_ligne in range(self.nombre_lignes):
			ligne = []
			for element in self.liste_contenu[numero_ligne]:
				if element == "O": ligne.append("mur")
				if element == " ": ligne.append("vide")
				if element == "U": ligne.append("sortie")
				if element == "X": ligne.append("robot")
				if element == ".": ligne.append("porte")
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

	

