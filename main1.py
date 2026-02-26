import pygame
pygame.init()

#Window
RESOLUTION = WIDTH, HEIGHT = (1080, 720)
SCREEN = pygame.display.set_mode(RESOLUTION)
backgroundcolor = (0,0,0)
game_is_running = True

#Sprite
SCALE = 5
FRAME_WIDTH = FRAME_HEIGHT  = 64
player_width, player_height = FRAME_WIDTH * SCALE, FRAME_HEIGHT * SCALE
Spritesheet = pygame.image.load("Swordsman_lvl3_Idle_with_shadow.png")
Spritesheet = Spritesheet.convert_alpha()
Sprite = Spritesheet.subsurface(pygame.Rect(0, 0, FRAME_WIDTH, FRAME_HEIGHT))
Sprite = pygame.transform.scale(Sprite, (player_width, player_height))

#player
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)
player_speed = (15)
player_color = (256, 200, 0)

#Floor
floor_width, floor_height = WIDTH, 20
floor = pygame.Rect(floor_width, floor_height, 0, HEIGHT - floor_height)
floor_color = ('brown')

#physik
velocity_y = 0
gravity = 1
jump_stength = -20


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
    if keys[pygame.K_w]:
        player.y -= player_speed
    if keys[pygame.K_s]:
        player.y += player_speed
    if keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        player.y += jump_stength
    
    #if player went out of map
    if player.y >= HEIGHT - player_height//1.25:
        player.y = HEIGHT - player_height//1.25

    #gravity
    #velocity_y += gravity
    #player.y += velocity_y

    #Screen
    SCREEN.blit(Sprite, player.topleft)
    pygame.draw.rect(SCREEN, floor_color, floor)
    pygame.display.flip()

pygame.quit