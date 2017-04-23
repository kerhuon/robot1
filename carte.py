# -*-coding:Utf-8 -*

from position import Position

class Carte:

	"""Classe représentant le labyrinthe (modèle) et la carte (vue)."""
	# Parti pris : on ne se trimballe pas avec deux classes : Classe et Labyrinthe
	# Car il s'agit de la même chose : labyrinthe utilisé pour le traitement, carte pour l'affichage

	
	REPERTOIRE_CARTES = "cartes/"
	ROBOT = "X"
	VIDE = " "
	MUR = "O"
	PORTE = "."
	SORTIE = "U"

	def __init__(self, nom, nom_de_fichier):
		self.nom = nom
		self.nom_de_fichier = nom_de_fichier

		# Contenu brut sous forme de chaine, permet l'affichage pour le joueur
		self.contenu = self.charger()

		# Contenu de la carte sous forme de liste de n listes (correspondant à n lignes).
		# De la forme : [['O', 'O', 'O', 'O', 'O', O'], ['O', ' ', ' ', ' ', '.', 'X', ' '], etc...]
		self.liste_contenu = self.charger_comme_liste()

	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	@property
	def position_robot(self):
		"""Renvoie un objet de classe Position contenant la position du robot"""
		pos = Position
		pos.ligne = 0		
		for ligne in self.liste_contenu:
			pos.colonne = 0
			for element in ligne:
				if element == Carte.ROBOT:
					return pos
				pos.colonne += 1
			pos.ligne += 1

	@property
	def position_sortie(self):
		"""Renvoie un objet de classe Position contenant la position de la sortie"""
		pos = Position
		pos.ligne = 0		
		for ligne in self.liste_contenu:
			pos.colonne = 0
			for element in ligne:
				if element == Carte.SORTIE:
					return pos
				pos.colonne += 1
			pos.ligne += 1

	@property
	def nombre_lignes(self):
		"""Nombre de lignes de la carte"""
		return len(self.liste_contenu)

	@property
	def nombre_colonnes(self):
		"""Nombre de colonnes de la carte"""
		return len(self.liste_contenu[0])-1	#on retire le \n
	
	def charger(self):
		"""Depuis le fichier, contenu brut sous forme de chaine, permet l'affichage pour le joueur"""
		fichier = open(Carte.REPERTOIRE_CARTES + self.nom_de_fichier, 'r')
		lecture = fichier.read()
		fichier.close()
		return lecture

	def oter_robot(self):
		"""S'applique à list_contenu, ôte le robot et le remplace par un espace"""
		self.liste_contenu[self.position_robot.ligne][self.position_robot.colonne] = Carte.VIDE

	def charger_comme_liste(self):
		"""Depuis le fichier, contenu de la carte sous forme de liste de n listes (correspondant à n lignes).
		De la forme : [['O', 'O', 'O', 'O', 'O', O'], ['O', ' ', ' ', ' ', '.', 'X', ' '], etc...]"""
		fichier = open(Carte.REPERTOIRE_CARTES + self.nom_de_fichier, 'r')
		lecture =  fichier.readlines()
		fichier.close()
		liste = []
		for ligne in lecture:
			liste.append([element for element in ligne])
		return liste

	def nettoyer(self):
		"""Permet d'enlever tous les \n"""
		for ligne in self.liste_contenu:
			while "\n" in ligne:
				ligne.remove("\n")

	def actualiser_liste_contenu(self, nouvelle_position):
		self.liste_contenu = self.charger_comme_liste()
		self.oter_robot()
		self.nettoyer()
		self.liste_contenu[nouvelle_position.ligne][nouvelle_position.colonne] = Carte.ROBOT	# On affecte nouvelle position robot
		
	def afficher_liste_contenu(self):
		self.nettoyer()
		for ligne in self.liste_contenu:
			chaine=''
			for element in ligne:
				chaine+=element
			print(chaine)

	def sauvegarder(self):
		fichier = open(Carte.REPERTOIRE_CARTES + "_sauvegarde.txt", 'w')
		self.nettoyer()
		for ligne in self.liste_contenu:
			chaine=''
			for element in ligne:
				chaine+=element
			chaine+="\n"
			fichier.write(chaine)
		fichier.close()



	

