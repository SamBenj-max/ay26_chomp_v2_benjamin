import pygame
from util import *

#speed bemo can move at
speed = 8


#hit sound for when bemo hits a planet
hit_sound = pygame.mixer.Sound('sound_effects/laserLarge_002.ogg')



class Bemo(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH*.5,y=700*.8):

        super().__init__()
        
        #Bemo is alive for conditionals later on 
        self.is_alive = True

        #Position on screen of Bemo
        self.x = x
        self.y = y
        
        #giving bemo 3 lives
        self.lives = 3
       
        #setting bemos default image when he spawns in
        self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_jump.png').convert_alpha()
        
        #getting his rect and setting its coordinated for proper tracking and printing of bemo
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # blit bemo on surface if he is alive
        if self.is_alive == True:
            screen.blit(self.image, self.rect) 
        
       
        
    
    def move(self):
        #get key for what player pressed
        self.player_key = pygame.key.get_pressed()

        #Allows player to move left, right, up, and down with either arrow keys or a, d, w, s keys respectively

        if self.player_key[pygame.K_w] or self.player_key[pygame.K_UP]:
            self.y -= speed
       
       
        if self.player_key[pygame.K_s] or self.player_key[pygame.K_DOWN]:
            self.y += speed
        
        
        if self.player_key[pygame.K_a] or self.player_key[pygame.K_LEFT]:
            self.x -= speed


        if self.player_key[pygame.K_d] or self.player_key[pygame.K_RIGHT]:
            self.x += speed
        
        self.rect.center = (self.x, self.y)


        #Boundaries(Bemo will be teleported back if he tries to go past a boundary)

        if self.x <= x_bounds: 
            self.x = x_bounds

        if self.x >= WIDTH - x_bounds:
            self.x = WIDTH - x_bounds


        if self.y <= 48: 
            self.y = 48

        if self.y >= WIDTH - y_bounds:
            self.y = WIDTH - y_bounds


    #function for displaying hearts
    def hearts(self, planet_list, screen):
        #global so i can change varbiable outside of function without need of return or issues with lcoal variables
        global hit_cooldown
      
        

        
        #allows for a 1 second cooldown because once hit it is set to 60 and every frame it subracts one 60 fps means 1 second cooldown
        if hit_cooldown > 0:
            hit_cooldown -= 1
            
        
            #resets bemo back to his normal style 
            if hit_cooldown == 0:
                self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_jump.png').convert_alpha()

            

        #checking if any collisons happen at all between bemo and any planet it in the list
        elif pygame.sprite.spritecollide(self, planet_list, False):  
            
            for p in planet_list: 
                #uses mask to have it check for collision of each individual planet and if it collides
                if pygame.sprite.collide_mask(self, p):
                    #kills planet
                    p.kill()
                    #sets cooldown to 60 from ealeirer
                    hit_cooldown = 60
                    print('Bemo was Hit')
                    #a life is taken away
                    self.lives -=1
                    #While bemo is hit he will in a duck postion until the hit countdown is back to 0
                    self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_duck.png').convert_alpha()
                    print(lives)
                    #plays sound after he is hit
                    hit_sound.play(0)
            
                
            
        #sets bemo to being alive to False which kills himif his lives are equal to less than 0
        if self.lives <= 0:
            self.is_alive = False
            self.kill()

        #if bemo has 3 lives their will be three hearts blit to the screen with a change in x coordinate to offer spacing
        if self.lives ==3:
            #Heart 1
            self.heart_image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image_rect = self.heart_image.get_rect()
            self.heart_image_rect.topright = (WIDTH-80, 10) 
        
            screen.blit(self.heart_image, self.heart_image_rect)

            
            #Heart 2
            self.heart_image2 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image2_rect = self.heart_image2.get_rect()
            self.heart_image2_rect.topright = (WIDTH-110, 10) 
        
            screen.blit(self.heart_image2, self.heart_image2_rect)


            #Heart 3
            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)



        #repeat of last code but subtracts one of the hearts away and removes one of the images blitted
        elif self.lives == 2:
            self.heart_image2 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image2_rect = self.heart_image2.get_rect()
            self.heart_image2_rect.topright = (WIDTH-110, 10) 
        
            screen.blit(self.heart_image2, self.heart_image2_rect)



            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)

        #removes another heart and blits only one heart
        elif self.lives == 1:
            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)
        

    #resets the paramaters and sets bemo alive to true and gives the three hearts back     
    def reset(self):
        self.lives = 3
        self.rect.center = (WIDTH//2 , HEIGHT//2)
        self.is_alive = True


    
        