import pygame
pygame.init()

#Window
RESOLUTION = WIDTH, HEIGHT = (1080, 720)
SCREEN = pygame.display.set_mode(RESOLUTION)
backgroundcolor = (55, 174, 15)
game_is_running = True

n =0

#Sprite standig
SCALE = 2.5
FRAME_WIDTH = FRAME_HEIGHT  = 64
player_width, player_height = FRAME_WIDTH * SCALE, FRAME_HEIGHT * SCALE
Spritesheet = pygame.image.load("Swordsman_lvl3_Idle_with_shadow.png")
Spritesheet = Spritesheet.convert_alpha()

Sprites_Stand = []
animation_index = 0
for i in range(12):
    Sprite = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, n, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite = pygame.transform.scale(Sprite, (player_width, player_height))
    Sprites_Stand.append(Sprite)

#player
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)
player_speed = (5)
player_color = (255, 200, 0)

#Index
animation_index_stand = 0
animation_index_walking = 0
animation_index_attack = 0
attack = False
moving = False
standing = True
Front = FRAME_HEIGHT * 0
Left = FRAME_HEIGHT * 1
Right = FRAME_HEIGHT * 2
Back = FRAME_HEIGHT * 3

#attack animation
Sprites_attack = []
Spritesheet = pygame.image.load('Swordsman_lvl3_attack_with_shadow.png')
Spritesheet = Spritesheet.convert_alpha()

#Attack Animation
for i in range(8):
    Sprite_attack = Spritesheet.subsurface(FRAME_WIDTH * i, n, FRAME_WIDTH, FRAME_WIDTH)
    Sprite_attack = pygame.transform.scale(Sprite_attack, (player_width, player_height))
    Sprites_attack.append(Sprite_attack)

#CLock
clock = pygame.time.Clock()
FPS = (60)
animation_timer = 0

#Game Loop
while game_is_running:
    moving = False
    attack = False
    standing = False
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

    #Sprite wlaking
    Spritesheet = pygame.image.load('Swordsman_lvl3_Walk_with_shadow.png')
    Spritesheet = Spritesheet.convert_alpha()

    #Walking animation
    Sprites_walking = []
    for i in range(6):
        Sprite_walking = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, n, FRAME_WIDTH, FRAME_HEIGHT))
        Sprite_walking= pygame.transform.scale(Sprite_walking, (player_width, player_height))
        Sprites_walking.append(Sprite_walking)
    
    #Player movement
    if keys[pygame.K_w]:
        player.y -= player_speed
        moving = True
        n = Back
    if keys[pygame.K_s]:
        player.y += player_speed
        moving = True
        n = Front
    if keys[pygame.K_a]:
        player.x -= player_speed
        moving = True
        n = Left
    if keys[pygame.K_d]:
        player.x += player_speed
        moving = True
        n = Right
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
            attack_s = True
    if keys[pygame.K_s and event.type == pygame.MOUSEBUTTONDOWN]:
        if event.button == 1:
            player.y += player_speed
            attack = True

    #if player went out of map
    if player.y >= HEIGHT - player_height//1.3:
        player.y = HEIGHT - player_height//1.3
    if player.y <= 0:
        player.y = 0
    if player.x >= WIDTH - player_width//1.6:
        player.x = WIDTH - player_width//1.6
    if player.x <= 0:
        player.x = 0
    


    #Screen
    if moving == True:
        SCREEN.blit(Sprites_walking[animation_index_walking], player.topleft)
    if attack == True:
        SCREEN.blit(Sprites_attack[animation_index_attack], player.topleft)
    elif moving == False:
        SCREEN.blit(Sprites_Stand[animation_index_stand], player.topleft)
    pygame.display.flip()

    if animation_timer == 10:
        animation_index_stand += 1
        animation_index_walking += 1
        animation_index_attack += 1
        if animation_index_stand > 11:
            animation_index_stand = 0
        if animation_index_walking > 5:
            animation_index_walking = 0
        if animation_index_attack > 7:
            animation_index_attack = 0
        animation_timer = 0
    animation_timer += 1

pygame.quit