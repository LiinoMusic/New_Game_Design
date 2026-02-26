import pygame
pygame.init()

#Window
RESOLUTION = WIDTH, HEIGHT = (1080, 720)
SCREEN = pygame.display.set_mode(RESOLUTION)
backgroundcolor = (0,0,0)
game_is_running = True

#player 
player_size = player_width, player_height = (50, 50)
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)
player_speed = (10)
player_color = (155, 200, 0)

#CLock
clock = pygame.time.Clock()
FPS = (60)

#Game Loop
while game_is_running:
    SCREEN.fill(backgroundcolor)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    keys = pygame.key.get_pressed()
    #Fullscreen 
    if keys[pygame.K_F11]:
        pygame.display.toggle_fullscreen()
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
        pygame.display.toggle_fullscreen()
    
    #Player movement
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    #Screen
    pygame.draw.rect(SCREEN, player_color, player)
    pygame.display.flip()

pygame.quit