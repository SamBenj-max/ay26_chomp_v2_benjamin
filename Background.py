import pygame
from util import *


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

#Loading specific background image
space_tile_location = 'jug.jpg'
space_tile_surface = pygame.image.load(space_tile_location)


#Setting up the height and width for printing image
tile_width = space_tile_surface.get_width()
tile_height = space_tile_surface.get_height()


background = pygame.Surface((WIDTH,HEIGHT))

#Taking each tile and placing it accordingly across the screen to properly blit
for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT,tile_height):
        background.blit(space_tile_surface,(x,y))

y_sand = HEIGHT - tile_height


#background scroll

#background's y position and its vy for it to move in direction
background_y = 0 
scroll_speed = 2



def background_scoll(screen):
   #global in order to update variable outside of function, (don't need to return in this case) 
    global background_y
    global scroll_speed
    
    #make background y be updated constantly by its scrolling speed

    background_y += scroll_speed


    #start first one blit to make it at 0 and in the middle of the y blit
    screen.blit(background, (0, background_y))
    

    #second one to start it at the Height then subtract by Height
    screen.blit(background, (0, background_y - HEIGHT))

    #Make background smooth transition from bottom to top
    if background_y == HEIGHT:
        background_y = 0

    
    
