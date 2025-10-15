import pygame

# pygame setup
pygame.init()


# screen properties

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

water_tile_lo = 'pattern_56.png'
water_tile_surface = pygame.image.load(water_tile_lo)

tile_width = water_tile_surface.get_width()
tile_height = water_tile_surface.get_height()



background = pygame.Surface((WIDTH,HEIGHT))

for x in range(0,WIDTH,tile_width):
    for y in range(0,HEIGHT,tile_height):
        background.blit(water_tile_surface,(x,y))


y_sand = HEIGHT - tile_height
#for x in range(0,WIDTH,tile_height):








screen.blit(background,(0,0))



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()