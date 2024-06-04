import pygame
import constants
from characters import *

player = Character(200, 400)

pygame.init()



window = pygame.display.set_mode((constants.WIDTH_WINDOW, constants.HEIGHT_WINDOW))
pygame.display.set_caption("TreeCode Crypto")

# Definir variables de movimiento del jugador

move_up = False
move_down = False
move_right = False
move_left = False

# Controlar el frame rate
reloj = pygame.time.Clock()

run = True

while run == True:

	# Que vaya a 60 FPS
	reloj.tick(constants.FPS)



	window.fill(constants.COLOR_BG)

	# Calcular el movimiento del jugador

	delta_x = 0
	delta_y = 0

	if move_right == True:

		delta_x = constants.VELOCITY

	if move_left == True:

		delta_x = -constants.VELOCITY

	if move_up == True:

		delta_y = -constants.VELOCITY

	if move_down == True:

		delta_y = constants.VELOCITY

	# Mover al jugador
	player.movement(delta_x, delta_y)

	player.draw(window)

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			run = False

		if event.type == pygame.KEYDOWN:

			if event.key == pygame.K_a:

				#print("Left")
				move_left = True

			if event.key == pygame.K_d:

				#print("Right")
				move_right = True

			if event.key == pygame.K_w:

				#print("Up")
				move_up = True

			if event.key == pygame.K_s:

				#print("Down")
				move_down = True

		if event.type == pygame.KEYUP:

			if event.key == pygame.K_a:

				move_left = False

			if event.key == pygame.K_d:

				move_right = False

			if event.key == pygame.K_w:

				move_up = False

			if event.key == pygame.K_s:

				move_down = False


	pygame.display.update()


pygame.quit()