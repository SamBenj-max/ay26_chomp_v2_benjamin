import pygame
from util import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.mixer.init()

pygame.init()


#reused the same stuff for my other backgrounds (see more on Background.py)
def titlescreen(screen):
    
    #Loading specific background image
    space_tile_location = 'image_backgrounds/sunball.png'
    space_tile_surface = pygame.image.load(space_tile_location)


    #Setting up the height and width for printing image
    tile_width = space_tile_surface.get_width()
    tile_height = space_tile_surface.get_height()


    background = pygame.Surface((WIDTH,HEIGHT))

    #Taking each tile and placing it accordingly across the screen to properly blit
    for x in range(0,WIDTH,tile_width):
        for y in range(0,HEIGHT,tile_height):
            background.blit(space_tile_surface,(x,y))
        
    screen.blit(background, (0, 0))
    

   
    




    



        


