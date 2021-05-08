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
    def reset_pos(self):
        self.rect.x = random.randrange(0,screen_width)
        self.rect.y = random.randrange(-300,-20)
    def update(self):
        self.rect.y +=1
        if self.rect.y > 410:
            self.reset_pos()
            
class Player(Block):
    
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
pygame.init()
        
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()


all_sprites_list = pygame.sprite.Group()





for i in range(9999):

    block = Block(black,20,15)
    
    
    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)
    all_sprites_list.add(block)
player =  Block(red,20,50)

all_sprites_list.add(player)
score = 0
font = pygame.font.Font(None,50)



play = True

clock = pygame.time.Clock()
start_ticks=pygame.time.get_ticks()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
    screen.fill(white)
    
    seconds=int((pygame.time.get_ticks()-start_ticks)/1000)
    all_sprites_list.update()
    pos = pygame.mouse.get_pos()
    
    player.rect.x = pos[0]
    player.rect.y = pos[1]
    
    blocks_hit_list = pygame.sprite.spritecollide(player,block_list,False)
    
    for block in blocks_hit_list:
        score += 1
        block.reset_pos()
    all_sprites_list.draw(screen)
    
    message = str(score)+'point'
    text = font.render(message,10,red)
    screen.blit(text,(10,10))
    
    t = font.render(str(seconds),10,red)
    screen.blit(t,(10,40))
    
    if seconds>100000000:
        text = font.rander('gg',50,black)
        screen.blit(text,(100,100))
        play=False
        
    all_sprites_list.draw(screen)
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()