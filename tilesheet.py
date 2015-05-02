import pygame
import pygame.locals

pygame.init()

def tilesheet(filename, tilewidth, tileheight = None):
	if tileheight == None:
		tileheight = tilewidth
	image = pygame.image.load(filename).convert()
	image.set_colorkey((255, 0, 255))
	sheet = []
	image_width, image_height = image.get_size()
	for y in range(image_height / tileheight):
		line = []
		sheet.append(line)
		for x in range(image_width / tilewidth):
			rect = (x * tilewidth, y * tileheight, tilewidth, tileheight)
			line.append(image.subsurface(rect))
	return sheet