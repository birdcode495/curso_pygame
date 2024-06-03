import pygame
import constants


class Character():

	def __init__(self, x, y):

		self.shape = pygame.Rect(0, 0, constants.WIDTH_CHARACTER, constants.HEIGHT_CHARACTER)
		self.shape.center = (x, y)

	def draw(self, interface):

		pygame.draw.rect(interface, constants.COLOR, self.shape)

