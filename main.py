# -*-coding:Utf-8 -*-

import robot, carte, position

# Vérifier si partie sauvegardée

# Dérouler les cartes disponibles

# test affichage position
ma_position = position.Position(2,3)
print(ma_position)

# Créer objet carte
carte = carte.Carte("fastoche", "facile.txt")
print(carte.nom)
print(carte.contenu)

carte.contenu = "OOOOOOO\nOOOOXOO" #ERROR !!! can't set attribute
print(carte.contenu) 

print(carte.position_robot)

robot = robot.Robot(carte.position_robot)

# Saisie du mouvement souhaité

# while True:
# 	reponse = input("Saisissez le mouvement souhaité (quit pour quitter) : ")
# 	if reponse == "quit":
# 		break
# 	print(carte.contenu)
