import pygame
from util import *

#pygame.init()

#make difficutly harder
def difficulty_more(score, planets):
    
    #when score increases to above 500 
    if score > 500:
        
           #add extra speed of the planets (break is to make sure its not infintely increasing) 
            for p in planets:
                p.vy += 1

                break
    

    if score > 1000:
         
            
            for p in planets:
                p.vy += 1
                break
    
    
    if score > 1500:
      
            
            for p in planets:
                p.vy += 1
                break
    

    if score > 2000:
     
            
            for p in planets:
                p.vy += 1
                break

    if score > 5000:
           
            
            for p in planets:
                p.vy += 1
                break