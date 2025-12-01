import pygame
from random import randint
from random import choice
from util import *



#allows me to have a list of planets to choose from allowing for later random planet genration


class Planet(pygame.sprite.Sprite):
    """
    inherited from pygame.sprite
    """
    def __init__(self, image_filename, screen_width=WIDTH, screen_height=HEIGHT):
        
        super().__init__()

        #size of planet being randomized
        self.size = randint(80,150)
        
        #loading the image and scaling it based of the self.size variable
        planet_image = pygame.image.load(image_filename).convert_alpha()
        self.image = pygame.transform.scale(planet_image, (self.size, self.size))
        
        #allowing for random generation of planets location on the x axis for the screen 
        self.x = randint(self.size, WIDTH - self.size)
        #allowing for the y-axis to be randomly generated but making it start negatvive so it can start a little above the screen
        self.y = randint(-2 * self.size, -self.size)
        
        #getting the rect so the planets will move and we can track it easier
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        #making the planets each spawn with a random y velocity between an integer of 1-8 in order to give each one varibale speed
        self.vy = randint(1,8)

    
    def draw(self, screen):
        # blit the planets surface on my star background
        screen.blit(self.image, self.rect)
    
    
    #update function for planets
    def update(self):
        
        #setting the movement and rect of the planets based off its velocity
        self.y += self.vy
        self.rect.center = (self.x, self.y)


        #meaning if planet falls off screen it will die
        if self.y > HEIGHT + self.size:
            self.kill()
 