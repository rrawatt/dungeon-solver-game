import pygame

class SquareButton:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.size = 15  

    def draw(self, surface, x):
        rect = pygame.Rect(10 + self.row * 15, 10 + self.col * 15, 15, 15)
        pygame.draw.rect(surface, x, rect)

    def is_hovered(self, mouse_pos):
        rect = pygame.Rect(10 + self.row * 15, 10 + self.col * 15, 15, 15)
        return rect.collidepoint(mouse_pos)