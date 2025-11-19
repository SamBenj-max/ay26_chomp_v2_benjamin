import pygame
from util import *

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True


pygame.init()

def deathbackground(screen, score):
    
    #Loading specific background image
    space_tile_location = 'endin.png'
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

    score_text = f"Your Final Score was: {score}"
    #Render in white
    score_surface = font.render(score_text, True, (255, 255, 255))
    
    #position of score
    score_rect = score_surface.get_rect()
    score_rect.center = (WIDTH//2, HEIGHT//2) 
    
    screen.blit(score_surface, score_rect)
    

    y_sand = HEIGHT - tile_height



    



        


