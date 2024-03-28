import pygame

class Enemy:
    def __init__(self, start_pos, player_pos, path):
        self.row, self.col = start_pos
        self.player_row, self.player_col = player_pos
        self.path = path
        self.color = (0, 0, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (10 + self.row * 15, 10 + self.col * 15, 15, 15))

    def move(self):
    # Calculate the direction to move towards the player's position (Blinky's method)
        dx = self.player_row - self.row
        dy = self.player_col - self.col

        if dx == 0 and dy == 0:
            return  # No need to move if already at the player's position

        # Ensure the enemy moves only in one direction (horizontal or vertical) at a time
        if abs(dx) > abs(dy):
            dx = int(dx / abs(dx))  # Normalize the direction
            dy = 0
        elif abs(dy) > 0:  # Ensure dy is not zero to avoid division by zero
            dx = 0
            dy = int(dy / abs(dy))  # Normalize the direction

        new_row = self.row + dx
        new_col = self.col + dy

        # Check if the new position is within the path
        if (new_row, new_col) in self.path:
            self.row = new_row
            self.col = new_col
        return (new_row,new_col)

    def update_player_position(self, player_pos):
        self.player_row, self.player_col = player_pos
