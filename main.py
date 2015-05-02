from battle import *
from entity import *
from tilesheet import *
import pygame
import pygame.locals
from constants import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

tiles = tilesheet()

def main():
	mainbattle = Battle()
	f1 = Entity("Peter", 1, 100, 100, 10, 10, 10, 0)
	f2 = Entity("Stephen", 1, 100, 100, 10, 10, 10, 0)
	mainbattle.add_fighters(f1, f2)
	while (True):
		mainbattle.turn()
		if (raw_input(">") == "exit"):
			return