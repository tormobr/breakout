import pygame

class Ball:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y
        self.rect.left = self.x
        self.rect.top = self.y

