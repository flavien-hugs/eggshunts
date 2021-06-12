# src/spritecart.py

import pygame


class SpriteCart(pygame.sprite.Sprite):
	"""docstring for SpriteCart"""
	def __init__(self, screen_weight, screen_height):
		super(SpriteCart, self).__init__()
		self.health = 50
		self.health_max = 100
		self.image = pygame.image.load("assets/cart.png")
		self.image = pygame.transform.scale(self.image, (110, 110))
		self.rect = self.image.get_rect()
		self.rect.x = (screen_weight / 2) - self.image.get_width() / 2
		self.rect.y = screen_height - 185
		self.velocity = 5
		self.screen_weight = screen_weight

	def add_health(self):
		if (self.health + 5) <= self.health_max:
			print("+5 pooints")
			self.health += 5

	def remove_health(self):
		if (self.health - 2) > 0:
			print("-3 points")
			self.health -= 3
		else:
			print("perdu !")

	def move_right(self):
		if self.rect.x + self.image.get_width() < self.screen_weight:
			self.rect.x += self.velocity

	def move_left(self):
		if self.rect.x > 0:
			self.rect.x -= self.velocity
