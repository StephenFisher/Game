import pygame
import pygame.locals
from constants import *

tiles = tilesheet("Sprites Test.png", 100)
player = tiles[0][0]
enemy = tiles[0][1]

class Battle_scene():
	def __init__(self, screen):
		#screen surface
		self.screen = screen
		self.surface = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.surface.fill((255, 0, 255))
		self.surface.set_colorkey((255, 0, 255))
		#player surface
		self.player_surface = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.player_surface.fill((255, 0, 255))
		self.player_surface.set_colorkey((255, 0, 255))
		#enemy surface
		self.enemy_surface = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.enemy_surface.fill((255, 0, 255))
		self.enemy_surface.set_colorkey((255, 0, 255))
		#player health surface
		self.pHealth_surface = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.pHealth_surface.fill((255, 0, 255))
		self.pHealth_surface.set_colorkey((255, 0, 255))
		#enemy health surface
		self.eHealth_surface = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.eHealth_surface.fill((255, 0, 255))
		self.eHealth_surface.set_colorkey((255, 0, 255))
		#background surface
		self.background = pygame.Surface((SCREENWIDTH, int(SCREENHEIGHT * 0.8)))
		self.background.fill((255, 0, 255))
		self.background.set_colorkey((255, 0, 255))

	def display_player(self):
		self.player_surface.blit(player, ((SCREENWIDTH * 0.2) - (BATTLE_SPRITE_WIDTH / 2), (SCREENHEIGHT / 2) - (BATTLE_SPRITE_HEIGHT / 2)))
		self.screen.blit(self.player_surface, (0, 0))

	def display_enemy(self):
		self.enemy_surface.blit(enemy, ((SCREENWIDTH * 0.8) + (BATTLE_SPRITE_WIDTH / 2), (SCREENHEIGHT / 2) - (BATTLE_SPRITE_HEIGHT / 2)))
		self.screen.blit(self.enemy_surface, (0, 0))

	def display_pHealth(self):
		pass

	def display_eHealth(self):
		pass

	def display_background(self):
		pass