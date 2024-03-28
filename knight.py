import pygame

class Player:
    def __init__(self, start_pos,path):
        self.row, self.col = start_pos
        self.path=path
        self.color = (125, 125, 125)  

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (10 + self.row * 15, 10 + self.col * 15, 15, 15))

    def move(self, dx, dy):
        new_row = self.row + dx
        new_col = self.col + dy

        if (new_row, new_col) in self.path:
            self.row = new_row
            self.col = new_col
        return (new_row,new_col)