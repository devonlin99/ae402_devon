import pygame
import random

red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

pygame.init()

size = (500)
size2 = (400)
screen = pygame.display.set_mode([size,size2])


player_x = 0
player_y = 0
player_w = 50
player_h = 50

block_w = 50
block_h = 50
block_x = random.randrange(size)
block_y = random.randrange(size2)
pygame.display.set_caption('砰狀')
collision = False

score = 0

font = pygame.font.Font(None,50)

done = False

clock = pygame.time.Clock()




while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    xin = block_x <= player_x <= block_x+block_w or block_x <= player_x+player_w <= block_x+block_w
    yin = block_y <= player_y <= block_y+block_h or block_y <= player_y+player_h <= block_y+block_h
    if xin and yin and not collision:
        collision = True
        score += 1
        
    screen.fill(white)
    
    
    pos = pygame.mouse.get_pos()
    
    player_x = pos[0]
    player_y = pos[1]
    pygame.draw.rect(screen,red,[player_x,player_y,player_w,player_h])
    if not collision:
        pygame.draw.rect(screen,black,[block_x,block_y,block_w,block_h])
        
        
    message = str(score)+' point'
    text = font.render(message,10,black)
    screen.blit(text,(10,10))
        
        
    pygame.display.flip()
        
        
    clock.tick(60)
    
pygame.quit()
        
    