import pygame
from util import *




class Bemo(pygame.sprite.Sprite):
    def __init__(self,x=WIDTH*.5,y=700*.8):

        super().__init__()
        
        #Bemo is alive 
        self.is_alive = True

        #Position on screen of Bemo
        self.x = x
        self.y = y
        
        

        #Velocity of Bemo
        #self.vx += self.x
        #self.vy += self.y

        self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_jump.png').convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        # blit the planets surface on my star background
        if self.is_alive == True:
            screen.blit(self.image, self.rect) 
        
       
        
    
    def move(self):
        #get key for what player pressed
        self.player_key = pygame.key.get_pressed()

        if self.player_key[pygame.K_w]:
            self.y -= 4
        
        if self.player_key[pygame.K_s]:
            self.y += 4
        
        if self.player_key[pygame.K_a]:
            self.x -= 4


        if self.player_key[pygame.K_d]:
            self.x += 4
        
        self.rect.center = (self.x, self.y)


        #Boundaries 

        if self.x <= x_bounds: 
            self.x = x_bounds

        if self.x >= WIDTH - x_bounds:
            self.x = WIDTH - x_bounds


        if self.y <= 48: 
            self.y = 48

        if self.y >= WIDTH - y_bounds:
            self.y = WIDTH - y_bounds


    
    def hearts(self, planet_list, screen):
        global hit_cooldown
        global lives
        

        

        if hit_cooldown > 0:
            hit_cooldown -= 1

            if hit_cooldown == 0:
                self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_jump.png').convert_alpha()

            


        elif pygame.sprite.spritecollide(self, planet_list, False):  
            
            for p in planet_list: 
                
                if pygame.sprite.collide_mask(self, p):
                    p.kill()
                    hit_cooldown = 60
                    print('Bemo was Hit')
                    lives -=1
                    self.image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Characters/platformChar_duck.png').convert_alpha()
                    print(lives)
            
                
            

        if lives <= 0:
            self.is_alive = False
    
        if lives ==3:
            self.heart_image = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image_rect = self.heart_image.get_rect()
            self.heart_image_rect.topright = (WIDTH-80, 10) 
        
            screen.blit(self.heart_image, self.heart_image_rect)


            self.heart_image2 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image2_rect = self.heart_image2.get_rect()
            self.heart_image2_rect.topright = (WIDTH-110, 10) 
        
            screen.blit(self.heart_image2, self.heart_image2_rect)



            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)

        elif lives == 2:
            self.heart_image2 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image2_rect = self.heart_image2.get_rect()
            self.heart_image2_rect.topright = (WIDTH-110, 10) 
        
            screen.blit(self.heart_image2, self.heart_image2_rect)



            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)

        elif lives == 1:
            self.heart_image3 = pygame.image.load('Planets/kenney_simplified-platformer-pack/PNG/Items/platformPack_item017.png')
            self.heart_image3_rect = self.heart_image3.get_rect()
            self.heart_image3_rect.topright = (WIDTH-140, 10) 
        
            screen.blit(self.heart_image3, self.heart_image3_rect)
        
        



        #Collison for Bemo
    #def collide(self, planet_group):
    
        #sprites collide to 
        #collided_planets = pygame.sprite.spritecollide(self, planet_group, True)

        #if collided_planets:
           

           
       #     self.is_alive = False 
        #    print("Bemo was hit and killed!")

    
        