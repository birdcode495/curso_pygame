import pygame
import constants
from characters import *

player = Character(200, 400)

pygame.init()



window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("TreeCode Crypto")

run = True

while run == True:

	player.draw(window)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			run = False


	pygame.display.update()


pygame.quit()