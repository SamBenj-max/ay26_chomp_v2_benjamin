import pygame
from util import *

class Bemo(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH*.5,y=700*.8):

        super().__init__()
        
        #Position on screen of Bemo
        self.x = x
        self.y = y
        
        #Velocity of Bemo
        #self.vx += self.x
        #self.vy += self.y

        self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_jump.png').convert_alpha()\
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # blit the planets surface on my star background
        screen.blit(self.image, self.rect) 
    
    def move(self, player, group):
        #get key for what player pressed
        self.player_key = pygame.key.get_pressed()

        if self.player_key[pygame.K_w]:
            self.y -= 4
        
        if self.player_key[pygame.K_s]:
            self.y += 4
        
        if self.player_key[pygame.K_a]:
            self.x -= 4


        if self.player_key[pygame.K_d]:
            self.x += 4
        
        self.rect.center = (self.x, self.y)


        #Boundaries 

        if self.x <=48: 
            self.x = 48

        if self.x >= WIDTH-48:
            self.x = WIDTH-48


        if self.y <=38: 
            self.y = 38

        if self.y >= WIDTH-380:
            self.y = WIDTH-380


        

        #Collison for Bemo
        self.collided_planets = pygame.sprite.spritecollide(player, group, False)

        if self.collided_planets:
            self.kill()

    
        