# -*-coding:Utf-8 -*-

from carte import Carte
from robot import Robot
from position import Position

# facile
carte = Carte("fastoche", "facile.txt")
robot = Robot(carte.position_robot)

print("Carte.MUR: ", Carte.MUR)

carte.afficher_liste_contenu()
print(robot)

print("OK vers le nord ?", robot.mouvement_possible(carte, "n"))
print("OK vers le sud ?", robot.mouvement_possible(carte, "s"))
print("OK vers l'est ?", robot.mouvement_possible(carte, "e"))
print("OK vers l'ouest ?", robot.mouvement_possible(carte, "o"))

print("\nDEUX pas vers le sud...")
robot.bouger(carte, "s", 2)
# print(robot)
# carte.actualiser_liste_contenu(robot.position)
# carte.afficher_liste_contenu()
print(robot)
print("OK vers le nord ?", robot.mouvement_possible(carte, "n"))
print("OK vers le sud ?", robot.mouvement_possible(carte, "s"))
print("OK vers l'est ?", robot.mouvement_possible(carte, "e"))
print("OK vers l'ouest ?", robot.mouvement_possible(carte, "o"))

print("\nUn autre pas vers le sud...")
robot.bouger(carte, "s")
# print(robot)
# carte.actualiser_liste_contenu(robot.position)
# carte.afficher_liste_contenu()
print(robot)
print("OK vers le nord ?", robot.mouvement_possible(carte, "n"))
print("OK vers le sud ?", robot.mouvement_possible(carte, "s"))
print("OK vers l'est ?", robot.mouvement_possible(carte, "e"))
print("OK vers l'ouest ?", robot.mouvement_possible(carte, "o"))

print("\nUn pas vers l'ouest...")
robot.bouger(carte, "o")
# print(robot)
# carte.actualiser_liste_contenu(robot.position)
# carte.afficher_liste_contenu()
print(robot)
print("OK vers le nord ?", robot.mouvement_possible(carte, "n"))
print("OK vers le sud ?", robot.mouvement_possible(carte, "s"))
print("OK vers l'est ?", robot.mouvement_possible(carte, "e"))
print("OK vers l'ouest ?", robot.mouvement_possible(carte, "o"))

print("\nUn pas vers le nord...")
robot.bouger(carte, "n")
# print(robot)
# carte.actualiser_liste_contenu(robot.position)
# carte.afficher_liste_contenu()
print(robot)
print("OK vers le nord ?", robot.mouvement_possible(carte, "n"))
print("OK vers le sud ?", robot.mouvement_possible(carte, "s"))
print("OK vers l'est ?", robot.mouvement_possible(carte, "e"))
print("OK vers l'ouest ?", robot.mouvement_possible(carte, "o"))
