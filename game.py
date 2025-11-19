import pygame
from planet_class import Planet , planet_assets
from random import choice
from Bemo import Bemo
from util import *
from Background import *
from score import *
from finalscorebackground import deathbackground



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


score_list = []


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if player1.is_alive == True:


        player1.move()
        planet_list.update()

        #player1.collide(planet_list)

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
        #player1.collide(planet_list)

        score1 = draw_score(screen)
        print(score1)

        #if score1 > 100:
        #     planet_count += 1
        

        player1.hearts(planet_list, screen)
             
        #if pygame.sprite.collide_circle(player1, planet_list):
         #       player1.is_alive = False

    final_score

    if player1.is_alive == False:
        deathbackground(screen,score1)
        

        restart_button = pygame.key.get_pressed()

    
        if restart_button[pygame.K_SPACE]:
                    player1.is_alive = True
                    print('Bemo is back')
            

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

