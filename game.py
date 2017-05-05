# by Adam Munawar Rahman

import pygame, sys, random
from pygame.locals import *

# Game map dimensions
TILESIZE = 24
MAPWIDTH = 30
MAPHEIGHT = 20

x_dim = MAPWIDTH * TILESIZE
y_dim = MAPHEIGHT * TILESIZE

# Color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Resource constants 
DIRT, GRASS, WATER, COAL = 0, 1, 2, 3

playerPos = [0,0]

# Dictionary mapping resources to textures
textures = {
	DIRT : pygame.image.load('assets/textures/dirt.png'),
	GRASS : pygame.image.load('assets/textures/grass.png'),
	WATER : pygame.image.load('assets/textures/water.png'),
	COAL : pygame.image.load('assets/textures/coal.png')}

inventory = {
	DIRT : 0,
	GRASS : 0, 
	WATER : 0,
	COAL : 0
}

# Using list comprehension to (a) access a list
# of resources (b) form a tilemap
resources = [DIRT, GRASS, WATER, COAL]
tilemap = [[DIRT for w in range(MAPWIDTH)]
			     for h in range(MAPHEIGHT)]

pygame.init()
DSURFACE = pygame.display.set_mode((x_dim, y_dim + 50))
PLAYER = pygame.image.load('assets/textures/player.png').convert_alpha(DSURFACE)
pygame.display.set_caption('Tile Heaven')

INVFONT = pygame.font.Font('assets/fonts/OpenSans-Regular.ttf',18)

for row in range(MAPHEIGHT):
	for col in range(MAPWIDTH):
		rInt = random.randint(0,15)
		if rInt == 0: 
			tile = COAL
		elif rInt == 1 or rInt == 2:
			tile = WATER
		elif rInt >= 3 and rInt <= 7:
			tile = GRASS
		else:
			tile = DIRT
		tilemap[row][col] = tile

# Main game loop
while True:

	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			# Directional movement, accounts for game screen bounding box
			if (event.key == K_RIGHT) and (playerPos[0] < MAPWIDTH - 1):
				playerPos[0] += 1
			if (event.key == K_LEFT) and (playerPos[0] > 0):
				playerPos[0] -= 1
			if (event.key == K_UP) and (playerPos[1] > 0):
				playerPos[1] -= 1
			if (event.key == K_DOWN) and (playerPos[1] < MAPHEIGHT -1):
				playerPos[1] += 1

			if event.key == K_SPACE:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				inventory[currentTile] += 1
				tilemap[playerPos[1]][playerPos[0]] = DIRT

			if event.key == K_1:
				currentTile = tilemap[playerPos[1]][playerPos[0]]
				if inventory[DIRT] >0:
					inventory[DIRT] -= 1
					tilemap[playerPos[1]][playerPos[0]] = DIRT
					inventory[currentTile] += 1

		for row in range(MAPHEIGHT):
			for column in range(MAPWIDTH):
				DSURFACE.blit(
					textures[tilemap[row][column]],
					             (column*TILESIZE,
					             	row*TILESIZE))

		DSURFACE.blit(PLAYER,
					   (playerPos[0]*TILESIZE,
					   	playerPos[1]*TILESIZE))

		placePosition = 10
		for item in resources:
			DSURFACE.blit(textures[item],
						  (placePosition, MAPHEIGHT*TILESIZE+20))
			placePosition += 30
			textObj = INVFONT.render(str(inventory[item]), True, WHITE, BLACK)
			DSURFACE.blit(textObj,(placePosition, MAPHEIGHT*TILESIZE+20))
			placePosition += 50

		pygame.display.update()

