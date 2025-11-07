import pygame
from util import *

class Bemo(pygame.sprite.Group):
    def __init__(self,x=WIDTH*.5,y=700*.8):

        super().__init__()
        
        #Bemo is alive 
        self.is_alive = True

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
        if self.is_alive == True:
            screen.blit(self.image, self.rect) 
        
    
    def move(self):
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

        if self.x <= x_bounds: 
            self.x = x_bounds

        if self.x >= WIDTH - x_bounds:
            self.x = WIDTH - x_bounds


        if self.y <= 48: 
            self.y = 48

        if self.y >= WIDTH - y_bounds:
            self.y = WIDTH - y_bounds


        

        #Collison for Bemo
    def collide(self, planet_group):
    
    
        collided_planets = pygame.sprite.spritecollide(self, planet_group, True)

        if collided_planets:
           
            score += 10 

            self.kill()
            #self.is_alive = False 
            print("Bemo was hit and killed!")

    
        