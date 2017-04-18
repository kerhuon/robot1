# -*-coding:Utf-8 -*-

# dico = (20, 20, {(0, 0): 'mur', (0, 1): 'mur', (0, 2): 'mur', (0, 3): 'mur', (0, 4): 'mur', (0, 5): 'mur', (0, 6): 'mur', \
# 	(0, 7): 'mur', (0, 8): 'mur', (0, 9): 'mur', (0, 10): 'mur', (0, 11): 'mur', (0, 12): 'mur', (0, 13): 'mur', \
# 	(0, 14): 'mur', (0, 15): 'mur', (0, 16): 'mur', (0, 17): 'mur', (0, 18): 'mur', (0, 19): 'mur', (1, 0): 'mur', \
# 	(1, 1): 'robot', (1, 2): 'mur', (1, 3): 'vide', (1, 4): 'porte', (1, 5): 'vide', (1, 6): 'mur', (1, 7): 'vide', \
# 	(1, 8): 'vide', (1, 9): 'vide', (1, 10): 'vide', (1, 11): 'mur', (1, 12): 'vide', (1, 13): 'porte', (1, 14): 'vide', \
# 	(1, 15): 'vide', (1, 16): 'vide', (1, 17): 'vide', (1, 18): 'vide', (1, 19): 'mur', (2, 0): 'mur', (2, 1): 'porte', \
# 	(2, 2): 'mur', (2, 3): 'vide', (2, 4): 'mur', (2, 5): 'vide', (2, 6): 'mur', (2, 7): 'vide', (2, 8): 'vide', \
# 	(2, 9): 'vide', (2, 10): 'vide', (2, 11): 'mur', (2, 12): 'vide', (2, 13): 'mur', (2, 14): 'vide', (2, 15): 'vide', \
# 	(2, 16): 'vide', (2, 17): 'vide', (2, 18): 'vide', (2, 19): 'mur', (3, 0): 'mur', (3, 1): 'vide', (3, 2): 'mur', \
# 	(3, 3): 'vide', (3, 4): 'mur', (3, 5): 'vide', (3, 6): 'mur', (3, 7): 'vide', (3, 8): 'vide', (3, 9): 'vide', \
# 	(3, 10): 'vide', (3, 11): 'mur', (3, 12): 'vide', (3, 13): 'mur', (3, 14): 'vide', (3, 15): 'vide', (3, 16): 'vide', \
# 	(3, 17): 'vide', (3, 18): 'vide', (3, 19): 'mur', (4, 0): 'mur', (4, 1): 'porte', (4, 2): 'mur', (4, 3): 'vide', \
# 	(4, 4): 'mur', (4, 5): 'vide', (4, 6): 'porte', (4, 7): 'vide', (4, 8): 'vide', (4, 9): 'vide', (4, 10): 'vide', \
# 	(4, 11): 'mur', (4, 12): 'vide', (4, 13): 'mur', (4, 14): 'vide', (4, 15): 'vide', (4, 16): 'vide', (4, 17): 'vide', \
# 	(4, 18): 'vide', (4, 19): 'mur', (5, 0): 'mur', (5, 1): 'vide', (5, 2): 'mur', (5, 3): 'vide', (5, 4): 'mur', \
# 	(5, 5): 'vide', (5, 6): 'mur', (5, 7): 'mur', (5, 8): 'mur', (5, 9): 'mur', (5, 10): 'mur', (5, 11): 'mur', \
# 	(5, 12): 'vide', (5, 13): 'mur', (5, 14): 'vide', (5, 15): 'vide', (5, 16): 'vide', (5, 17): 'vide', (5, 18): 'vide', \
# 	(5, 19): 'mur', (6, 0): 'mur', (6, 1): 'vide', (6, 2): 'mur', (6, 3): 'vide', (6, 4): 'mur', (6, 5): 'vide', \
# 	(6, 6): 'vide', (6, 7): 'vide', (6, 8): 'vide', (6, 9): 'vide', (6, 10): 'vide', (6, 11): 'vide', (6, 12): 'vide', \
# 	(6, 13): 'mur', (6, 14): 'vide', (6, 15): 'vide', (6, 16): 'vide', (6, 17): 'vide', (6, 18): 'vide', (6, 19): 'mur', \
# 	(7, 0): 'mur', (7, 1): 'vide', (7, 2): 'mur', (7, 3): 'vide', (7, 4): 'mur', (7, 5): 'mur', (7, 6): 'mur', (7, 7): 'mur', \
# 	(7, 8): 'mur', (7, 9): 'mur', (7, 10): 'mur', (7, 11): 'mur', (7, 12): 'mur', (7, 13): 'mur', (7, 14): 'vide', \
# 	(7, 15): 'vide', (7, 16): 'vide', (7, 17): 'vide', (7, 18): 'vide', (7, 19): 'mur', (8, 0): 'mur', (8, 1): 'porte', \
# 	(8, 2): 'mur', (8, 3): 'vide', (8, 4): 'porte', (8, 5): 'vide', (8, 6): 'vide', (8, 7): 'vide', (8, 8): 'vide', (8, 9): 'vide', \
# 	(8, 10): 'vide', (8, 11): 'vide', (8, 12): 'vide', (8, 13): 'mur', (8, 14): 'vide', (8, 15): 'vide', (8, 16): 'vide', (8, 17): 'vide', (8, 18): 'vide', (8, 19): 'mur', (9, 0): 'mur', (9, 1): 'vide', (9, 2): 'mur', (9, 3): 'vide', (9, 4): 'mur', (9, 5): 'vide', (9, 6): 'vide', (9, 7): 'vide', (9, 8): 'vide', (9, 9): 'vide', (9, 10): 'vide', (9, 11): 'vide', (9, 12): 'vide', (9, 13): 'mur', (9, 14): 'vide', (9, 15): 'vide', (9, 16): 'vide', (9, 17): 'vide', (9, 18): 'vide', (9, 19): 'mur', (10, 0): 'mur', (10, 1): 'vide', (10, 2): 'mur', (10, 3): 'vide', (10, 4): 'mur', (10, 5): 'vide', (10, 6): 'vide', (10, 7): 'vide', (10, 8): 'vide', (10, 9): 'vide', (10, 10): 'vide', (10, 11): 'vide', (10, 12): 'vide', (10, 13): 'mur', (10, 14): 'vide', (10, 15): 'vide', (10, 16): 'vide', (10, 17): 'vide', (10, 18): 'vide', (10, 19): 'mur', (11, 0): 'mur', (11, 1): 'vide', (11, 2): 'mur', (11, 3): 'porte', (11, 4): 'mur', (11, 5): 'vide', (11, 6): 'vide', (11, 7): 'vide', (11, 8): 'vide', (11, 9): 'vide', (11, 10): 'vide', (11, 11): 'vide', (11, 12): 'vide', (11, 13): 'mur', (11, 14): 'vide', (11, 15): 'vide', (11, 16): 'vide', (11, 17): 'vide', (11, 18): 'vide', (11, 19): 'mur', (12, 0): 'mur', (12, 1): 'porte', (12, 2): 'mur', (12, 3): 'vide', (12, 4): 'porte', (12, 5): 'vide', (12, 6): 'vide', (12, 7): 'vide', (12, 8): 'vide', (12, 9): 'vide', (12, 10): 'vide', (12, 11): 'vide', (12, 12): 'vide', (12, 13): 'mur', (12, 14): 'vide', (12, 15): 'vide', (12, 16): 'vide', (12, 17): 'vide', (12, 18): 'vide', (12, 19): 'mur', (13, 0): 'mur', (13, 1): 'vide', (13, 2): 'mur', (13, 3): 'vide', (13, 4): 'mur', (13, 5): 'vide', (13, 6): 'vide', (13, 7): 'vide', (13, 8): 'vide', (13, 9): 'vide', (13, 10): 'vide', (13, 11): 'vide', (13, 12): 'vide', (13, 13): 'mur', (13, 14): 'vide', (13, 15): 'vide', (13, 16): 'vide', (13, 17): 'vide', (13, 18): 'vide', (13, 19): 'mur', (14, 0): 'mur', (14, 1): 'vide', (14, 2): 'mur', (14, 3): 'vide', (14, 4): 'mur', (14, 5): 'vide', (14, 6): 'vide', (14, 7): 'vide', (14, 8): 'vide', (14, 9): 'vide', (14, 10): 'vide', (14, 11): 'vide', (14, 12): 'vide', (14, 13): 'mur', (14, 14): 'vide', (14, 15): 'vide', (14, 16): 'vide', (14, 17): 'vide', (14, 18): 'vide', (14, 19): 'mur', (15, 0): 'mur', (15, 1): 'vide', (15, 2): 'mur', (15, 3): 'vide', (15, 4): 'mur', (15, 5): 'vide', (15, 6): 'vide', (15, 7): 'vide', (15, 8): 'vide', (15, 9): 'vide', (15, 10): 'vide', (15, 11): 'vide', (15, 12): 'vide', (15, 13): 'mur', (15, 14): 'vide', (15, 15): 'vide', (15, 16): 'vide', (15, 17): 'vide', (15, 18): 'vide', (15, 19): 'mur', (16, 0): 'mur', (16, 1): 'vide', (16, 2): 'mur', (16, 3): 'vide', (16, 4): 'mur', (16, 5): 'vide', (16, 6): 'vide', (16, 7): 'vide', (16, 8): 'vide', (16, 9): 'vide', (16, 10): 'vide', (16, 11): 'vide', (16, 12): 'vide', (16, 13): 'mur', (16, 14): 'vide', (16, 15): 'vide', (16, 16): 'vide', (16, 17): 'vide', (16, 18): 'vide', (16, 19): 'mur', (17, 0): 'mur', (17, 1): 'porte', (17, 2): 'mur', (17, 3): 'vide', (17, 4): 'mur', (17, 5): 'vide', (17, 6): 'vide', (17, 7): 'vide', (17, 8): 'vide', (17, 9): 'vide', (17, 10): 'vide', (17, 11): 'vide', (17, 12): 'vide', (17, 13): 'mur', (17, 14): 'vide', (17, 15): 'vide', (17, 16): 'vide', (17, 17): 'vide', (17, 18): 'vide', (17, 19): 'mur', (18, 0): 'mur', (18, 1): 'vide', (18, 2): 'vide', (18, 3): 'vide', (18, 4): 'mur', (18, 5): 'vide', (18, 6): 'vide', (18, 7): 'vide', (18, 8): 'vide', (18, 9): 'vide', (18, 10): 'vide', (18, 11): 'vide', (18, 12): 'vide', (18, 13): 'mur', (18, 14): 'vide', (18, 15): 'vide', (18, 16): 'vide', (18, 17): 'vide', (18, 18): 'vide', (18, 19): 'sortie', (19, 0): 'mur', (19, 1): 'mur', (19, 2): 'mur', (19, 3): 'mur', (19, 4): 'mur', (19, 5): 'mur', (19, 6): 'mur', (19, 7): 'mur', (19, 8): 'mur', (19, 9): 'mur', (19, 10): 'mur', (19, 11): 'mur', (19, 12): 'mur', (19, 13): 'mur', (19, 14): 'mur', (19, 15): 'mur', (19, 16): 'mur', (19, 17): 'mur', (19, 18): 'mur', (19, 19): 'mur'})

liste = [['mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur'], ['mur', 'robot', 'mur', 'vide', 'porte', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'porte', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'porte', 'mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'porte', 'mur', 'vide', 'mur', 'vide', 'porte', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'porte', 'mur', 'vide', 'porte', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'porte', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'porte', 'mur', 'vide', 'porte', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'porte', 'mur', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur'], ['mur', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'vide', 'mur', 'vide', 'vide', 'vide', 'vide', 'vide', 'sortie'], ['mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur', 'mur']]

# def creer_chaine_depuis_labyrinthe(objet_laby):
# 		"""Renvoie une chaine de caractères (qui composera le fichier carte.txt
# 		à paritr d'un dictionnaire (contenu d'un objet labyrinthe)"""
# 		chaine = ""
# 		nb_lignes = objet_laby[0]
# 		nb_colonnes = objet_laby[1]
# 		index = 0
# 		indices = [nb_lignes*i for i in range(1, nb_colonnes) ]
# 		print(indices)

# 		for cle, valeur in objet_laby[2].items():
# 			if valeur =="mur": chaine += "O"
# 			if valeur =="vide": chaine += " "
# 			if valeur =="robot": chaine += "X"
# 			if valeur =="porte": chaine += "."
# 			if valeur =="sortie": chaine += "U"
# 			if index + 1 in indices: chaine += "\n"
# 			index += 1
# 		return chaine	

# print(creer_chaine_depuis_labyrinthe(dico))

def creer_chaine_depuis_labyrinthe(liste):
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

print(creer_chaine_depuis_labyrinthe(liste))