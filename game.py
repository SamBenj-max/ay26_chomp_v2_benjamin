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
for i in range(8):
    random_path = choice(planet_assets)
    planet_list.add(Planet(random_path))


#init player1
player1 = Bemo()






while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player1.move()

    #screen.blit(background,(0,0))
    background_scoll(screen)


    planet_list.update()
    
    planet_list.draw(screen)

    

    player1.draw(screen)

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()