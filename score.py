import pygame
from util import *

pygame.init()

score_list = []



clock1 = 0 




def draw_score(screen):
    # Make global variables for access in Bemo's update class
    #global score
    #global clock1
    
    clock2 = pygame.time.get_ticks()

    score = ((clock2 - clock1)//1000)*10
    
    clock2 = clock1


    #Making the Score 
    score_text = f"Score: {score}"
    #Render in white
    score_surface = font.render(score_text, True, (255, 255, 255))
    
    #position of score
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10) 
    
    

    screen.blit(score_surface, score_rect)

    return score

final_score = score



