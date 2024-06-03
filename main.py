import pygame
import constants

pygame.init()



window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

run = True

while run == True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			run = False


pygame.quit()