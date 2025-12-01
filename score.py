import pygame
from util import *

#pygame.init()




#settting the start time to 0 for the ability to reset the time later on. 
start_time = 0 




def draw_score(screen):
    
   
    #start the time as the game starts 
    clock = pygame.time.get_ticks()


    #allows for the score to be calculated by each second elasped 10 points will be added(see why clock-startine works below)
    score = ((clock - start_time)//1000)*10
 


    #Making the Score 
    score_text = f"Score: {score}"
    #Render in white
    score_surface = font.render(score_text, True, (255, 255, 255))
    
    #position of score
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10) 
    
    
    #actually drawing the score
    screen.blit(score_surface, score_rect)

    return score



def reset_score(): 
    #can change the variable globally
    global start_time

    #makes the start time = to the current time the game was going so it can then subtract from the ealrier functiion
    start_time = pygame.time.get_ticks()

    
   
   

    
    
    

    
    



