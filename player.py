import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def move(self, movement):
        self.x += movement
        self.rect.left = self.x

