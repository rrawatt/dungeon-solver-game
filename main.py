import pygame
from pygame.locals import *
import knight
import button
import hunter
import random
import time
import mazegen

pygame.init()

WIDTH, HEIGHT = 830, 830
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")

black = (0, 0, 0)
white = (255, 255, 255)

def main():
    run = True
    clock = pygame.time.Clock()
    path = mazegen.mazetree()
    print(path[0])
    ppos=path[1][1]
    epos=[random.choice(list(path[0])) for i in range(4)]
    player = knight.Player(ppos,path[0])
    enemy=[hunter.Enemy(i,ppos,path[0]) for i in epos]
    last_move_time = time.time()  # Initialize the last move time

    while run:
        WIN.fill(black)
        mouse_pos = pygame.mouse.get_pos()  # Get mouse position
        
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False

        for i in path[0]:
            x = button.SquareButton(i[0], i[1])
            x.draw(WIN,(95,79,70))

        player.draw(WIN)

        for i in enemy:
            i.draw(WIN)

        keys = pygame.key.get_pressed()
        
        if time.time() - last_move_time > 0.075:  
            if keys[K_UP]:
                ppos=player.move(0, -1)
                for i in enemy:
                    i.update_player_position(ppos)  
                    epos[enemy.index(i)]=i.move()

            elif keys[K_DOWN]:
                ppos=player.move(0, 1)
                for i in enemy:
                    i.update_player_position(ppos)  
                    epos[enemy.index(i)]=i.move()
            elif keys[K_LEFT]:
                ppos=player.move(-1, 0)
                for i in enemy:
                    i.update_player_position(ppos)  
                    epos[enemy.index(i)]=i.move()
            elif keys[K_RIGHT]:
                ppos=player.move(1, 0)
                for i in enemy:
                    i.update_player_position(ppos)  
                    epos[enemy.index(i)]=i.move()
            else:
                for i in enemy:
                    i.update_player_position(ppos)  
                    epos[enemy.index(i)]=i.move()
            last_move_time = time.time() 
         
        end= button.SquareButton(path[1][2][0], path[1][2][1])
        end.draw(WIN, (255,215,0))
        if ppos==path[1][2]:
            break
        if ppos in epos:
            break
            
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
