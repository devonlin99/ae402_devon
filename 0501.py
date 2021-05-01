import pygame
import random
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)

pygame.init()


class Block(pygame.sprite.Sprite):
    
    def __init__(self,color,width,height):
        
        super().__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        
        
        self.rect = self.image.get_rect()
        
pygame.init()
        
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()


all_sprites_list = pygame.sprite.Group()





for i in range(50):
    
    block = Block(black,20,15)
    
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)
    
    all_sprites_list.add(block)
player =  Block(red,20,15)
all_sprites_list.add(player)


play = True

clock = pygame.time.Clock()


while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    screen.fill(white)
    
    
    
    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()