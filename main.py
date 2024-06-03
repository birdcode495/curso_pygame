import pygame
import constants

pygame.init()



window = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("TreeCode Crypto")

run = True

while run == True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			run = False


pygame.quit()