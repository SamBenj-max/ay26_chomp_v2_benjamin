import pygame
from random import randint
from random import choice
from util import *




random_path = choice(planet_assets)

class Planet(pygame.sprite.Sprite):
    """
    inherited from pygame.sprite
    """
    def __init__(self, image_filename, screen_width=WIDTH, screen_height=HEIGHT):
        
        super().__init__()
        self.size = randint(80,150)
        
        planet_image = pygame.image.load(image_filename).convert_alpha()
        self.image = pygame.transform.scale(planet_image, (self.size, self.size))
        
        self.x = randint(self.size, screen_width - self.size)
        self.y = randint(self.size, screen_height//2 - self.size)
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.vx = 0

        self.vy = randint(1,5)

    
    def draw(self, screen):
        # blit the planets surface on my star background
        screen.blit(self.image, self.rect)
    
    
    
    def update(self):
        #self.vx = vx
        self.y += self.vy
        self.rect.center = (self.x, self.y)

        if self.y > HEIGHT + self.size:
            self.kill()
            



            #self.y = 0
            #self.x = randint(40,WIDTH-40)
           #random_path = choice(planet_assets)

        




        



#random_path = choice(planet_assets)

#planet_list = []
#for i in range(20):
   # planet_list.append(Planet(choice(planet_assets)))
