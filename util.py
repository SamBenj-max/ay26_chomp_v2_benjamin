import pygame
WIDTH = 1000
HEIGHT = 700
x_bounds = 58
y_bounds = 380

pygame.init()

score = 0
font = pygame.font.Font(None, 36)

planet_assets = [
'Planets/planet00.png',
'Planets/planet01.png',
'Planets/planet02.png',
'Planets/planet03.png',
'Planets/planet04.png',
'Planets/planet05.png',
'Planets/planet06.png',
'Planets/planet07.png',
'Planets/planet08.png',
'Planets/planet09.png'
]

    


#score keeping

def draw_score(screen):
    # Make global variables for access in Bemo's update class
    global score
    global font
    
    #Making the Score 
    score_text = f"Score: {score}"
    #Render in white
    score_surface = font.render(score_text, True, (255, 255, 255))
    
    #position of score
    score_rect = score_surface.get_rect()
    score_rect.topleft = (10, 10) 
    
    screen.blit(score_surface, score_rect)