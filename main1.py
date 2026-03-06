import pygame
pygame.init()

#Window
RESOLUTION = WIDTH, HEIGHT = (1080, 720)
SCREEN = pygame.display.set_mode(RESOLUTION)
backgroundcolor = (55, 174, 15)
game_is_running = True

#Sprite standig
SCALE = 5
FRAME_WIDTH = FRAME_HEIGHT  = 64
player_width, player_height = FRAME_WIDTH * SCALE, FRAME_HEIGHT * SCALE
Spritesheet = pygame.image.load("Swordsman_lvl3_Idle_with_shadow.png")
Spritesheet = Spritesheet.convert_alpha()

Sprites_Stand = []
animation_index = 0
for i in range(12):
    Sprite = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, 0, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite = pygame.transform.scale(Sprite, (player_width, player_height))
    Sprites_Stand.append(Sprite)

animation_index_stand = 0

#Sprite wlaking
Spritesheet = pygame.image.load('Swordsman_lvl3_Walk_with_shadow.png')
Spritesheet = Spritesheet.convert_alpha()

#Walking animation
Sprites_walk_a = []
Sprites_walk_d = []
Sprites_walk_w = []
Sprites_walk_s = []
for i in range(6):
    Sprite_a = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, FRAME_HEIGHT, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite_a = pygame.transform.scale(Sprite_a, (player_width, player_height))
    Sprites_walk_a.append(Sprite_a)
for i in range(6):
    Sprite_d = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, FRAME_HEIGHT * 2, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite_d = pygame.transform.scale(Sprite_d, (player_width, player_height))
    Sprites_walk_d.append(Sprite_d)
for i in range(6):
    Sprite_s = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, 0, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite_s = pygame.transform.scale(Sprite_s, (player_width, player_height))
    Sprites_walk_s.append(Sprite_s)
for i in range(6):
    Sprite_w = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, FRAME_HEIGHT * 3, FRAME_WIDTH, FRAME_HEIGHT))
    Sprite_w = pygame.transform.scale(Sprite_w, (player_width, player_height))
    Sprites_walk_w.append(Sprite_w)
animation_index_walk_s = 0
animation_index_walk_w = 0
animation_index_walk_a = 0
animation_index_walk_d = 0
animation_index_attack_stand = 0
animation_index_attack = 0
animation_index_attack_d = 0
animation_index_attack_a = 0
animation_index_attack_s = 0
animation_index_attack_w = 0
moving_a = False
moving_d = False
moving_w = False
moving_s = False
attack_a = False
attack_d = False
attack_s = False
attack_w = False
moving = [moving_w, moving_s, moving_a, moving_d]
attack = [attack_a, attack_d, attack_w, attack_s]

#player
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)
player_speed = (5)
player_color = (255, 200, 0)

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
animation_timer = 0

#Game Loop
while game_is_running:
    moving_a = False
    moving_d = False
    moving_s = False
    moving_w = False
    attack_a = False
    attack_d = False
    attack_s = False
    attack_w = False
    moving = False
    attack = False
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
        moving_w = True
        moving = True
    if keys[pygame.K_s]:
        player.y += player_speed
        moving_s = True
        moving = True
    if keys[pygame.K_a]:
        player.x -= player_speed
        moving_a = True
        moving = True
    if keys[pygame.K_d]:
        player.x += player_speed
        moving_d = True
        moving = True
    if keys[pygame.K_SPACE]:
        player.y += jump_stength

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
    if moving_a == True:
        SCREEN.blit(Sprites_walk_a[animation_index_walk_a], player.topleft)
    elif moving_d == True:
        SCREEN.blit(Sprites_walk_d[animation_index_walk_d], player.topleft)
    elif moving_w == True:
        SCREEN.blit(Sprites_walk_w[animation_index_walk_w], player.topleft)
    elif moving_s == True:
        SCREEN.blit(Sprites_walk_s[animation_index_walk_s], player.topleft)
    elif moving == False:
        SCREEN.blit(Sprites_Stand[animation_index_stand], player.topleft)
    pygame.draw.rect(SCREEN, floor_color, floor)
    pygame.display.flip()

    if animation_timer == 10:
        animation_index_stand += 1
        animation_index_walk_a += 1
        animation_index_walk_d += 1
        animation_index_walk_w += 1
        animation_index_walk_s += 1
        animation_index_attack += 1
        animation_index_attack_d += 1
        animation_index_attack_a += 1
        animation_index_attack_s += 1
        animation_index_attack_w += 1
        animation_index_attack_stand += 1
        if animation_index_stand > 11:
            animation_index_stand = 0
        if animation_index_walk_a > 5:
            animation_index_walk_a = 0
        if animation_index_walk_d > 5:
            animation_index_walk_d = 0
        if animation_index_walk_s > 5:
            animation_index_walk_s = 0
        if animation_index_walk_w > 5:
            animation_index_walk_w = 0
        if animation_index_attack_stand > 7:
            animation_index_attack_stand = 0
        if animation_index_attack > 7:
            animation_index_attack = 0
        if animation_index_attack_a > 7:
            animation_index_attack_a = 0
        if animation_index_attack_w > 7:
            animation_index_attack_w = 0
        if animation_index_attack_s > 7:
            animation_index_attack_s = 0
        if animation_index_attack_d > 7:
            animation_index_attack_d = 0
        animation_timer = 0
    animation_timer += 1

pygame.quit