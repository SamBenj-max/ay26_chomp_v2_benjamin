import pygame
from random import randint

D_WIDTH = 1000
D_HEIGHT = 700

class Planet(pygame.sprite.Sprite):
    """
    inherited from pygame.sprite
    """
    def __init__(self, image_filename, screen_width=D_WIDTH, screen_height=D_HEIGHT):
        
        super().__init__()
        self.size = randint(100,300)
        
        planet_image = pygame.image.load(image_filename).convert_alpha()
        self.image = pygame.transform.scale(planet_image, (self.size, self.size))
        
        self.x = randint(self.size, screen_width - self.size)
        self.y = randint(self.size, screen_height - self.size)
        
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def draw(self, screen):
        # blit the planets surface on my star background
        screen.blit(self.image, self.rect)