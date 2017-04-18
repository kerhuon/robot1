# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		self.robot = robot
		
		# {(0, 0):"mur", (0,1):"mur",...., (3,5):"porte"}
		self.grille = {}

	@property
	def is_move_possible(self, direction):
		#valeurs possibles : est, ouest, nord, sud
		self.direction = direction

