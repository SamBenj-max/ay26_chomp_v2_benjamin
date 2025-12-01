import pygame
from planet_class import Planet , planet_assets
from random import choice
from Bemo import Bemo
from util import *
from Background import *
from score import draw_score, reset_score
from finalscorebackground import deathbackground
from difficulty_increase import difficulty_more
from titlescreen import titlescreen


# pygame setup
pygame.init()


# for sound effects
pygame.mixer.init()

# screen properties


#init planets
planet_list = pygame.sprite.Group() 


#set planet count
planet_count = 10


#set game state initial for title screen
game_on = False


#init player1
player1 = Bemo()








#While loop that runs game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Titlescreen loading
    if game_on == False:
        titlescreen(screen)
        start_button = pygame.key.get_pressed()

        #Press Space Bar to start game
        if start_button[pygame.K_SPACE]:
            game_on = True
            reset_score()


    #If game is on == True then we can do the other conditinal if Bemo is alive or not
    elif game_on == True:

        #if He is alive this is our main game when the player is alive
        if player1.is_alive == True:

            #gives Bemo movement 
            player1.move()

            #allows planets to move 
            planet_list.update()

           
            #allows the background to be blitted and scroll 
            background_scoll(screen)
   
        
        
        
            #My loop to keep planets spawning after they are killed The loop gives whatever number i is to make a planet to run it.
            planets = planet_count - len(planet_list)
            for i in range(planets):
                #random planet choice from planet assets allowing random planet color spawning
                new_planets = Planet(choice(planet_assets))
                planet_list.add(new_planets)
                new_planets.y = -10



    
            #actually drawing the planets based off their updates
            planet_list.draw(screen)

    
            #drawing the player (you have to draw these later so that the background and planets dont cover the player)
            player1.draw(screen)
        
            #setting score1 == to the draw score function allowing score keeping
            score1 = draw_score(screen)
            print(score1)

           
        
            #allowing the hearts to be drawn and updated 
            player1.hearts(planet_list, screen)
             
            
            #allowing the difficulty to increase as the score increases
            difficulty_more(score1, planet_list)
                
                
            
        #if bemo is not alive 
        elif player1.is_alive == False:
            #new background will generate with score1 being used as the input to display score
            deathbackground(screen,score1)
            #all planets are killed
            for p in planet_list:
                p.kill()
        

            restart_button = pygame.key.get_pressed()

            #if space is pressed player1 gets hearts back which make the the player alive true now
            if restart_button[pygame.K_SPACE]:
                player1.reset()
                #resets score to 0
                reset_score()
                #empties planet list to allow for a fresh set of planets just for redundancy
                planet_list.empty()

                #resets players position
                player1.x = WIDTH//2
                player1.y = HEIGHT - 150

                continue
        
            

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

