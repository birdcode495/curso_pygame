import pygame


class Character():

	def __init__(self, x, y):

		self.shape = pygame.Rect(0, 0, 20, 20)
		self.shape.center = (x, y)

	def draw(self, interface):

		pygame.draw.rect(interface, (255, 0, 0), self.shape)

