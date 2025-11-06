import pygame
from planet_class import Planet , planet_assets
from random import choice
from Bemo import Bemo
from util import *
from Background import *




# pygame setup
pygame.init()


# screen properties






#print('blueS')

#init planets
planet_list = pygame.sprite.Group() 

#for i in range(8):
#    random_path = choice(planet_assets)
#    planet_list.add(Planet(random_path))

planet_count = 10






#init player1
player1 = Bemo()






while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player1.move(player1,planet_list)
    planet_list.update()

    #screen.blit(background,(0,0))
    background_scoll(screen)

    #My loop to keep planets spawning after they are killed The loop gives whatever number i is to make a planet to run it.
    planets = planet_count - len(planet_list)
    for i in range(planets):
        new_planets = Planet(choice(planet_assets))
        planet_list.add(new_planets)
        new_planets.y = -10


    
    
    planet_list.draw(screen)

    

    player1.draw(screen)

    



    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()