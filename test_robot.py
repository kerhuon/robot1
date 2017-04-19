# -*-coding:Utf-8 -*-

from carte import Carte
from robot import Robot
from position import Position

# facile
carte = Carte("fastoche", "facile.txt")
robot = Robot(carte.position_robot)

print(carte.contenu)
print(robot)

print(robot.mouvement_possible(carte, "n"))
print(robot.mouvement_possible(carte, "s"))
print(robot.mouvement_possible(carte, "e"))
print(robot.mouvement_possible(carte, "o"))

# prison
carte = Carte("fastoche", "prison.txt")
robot = Robot(carte.position_robot)

print(carte.contenu)
print(robot)

print(robot.mouvement_possible(carte, "n"))
print(robot.mouvement_possible(carte, "s"))
print(robot.mouvement_possible(carte, "e"))
print(robot.mouvement_possible(carte, "o"))