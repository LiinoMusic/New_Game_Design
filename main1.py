import pygame
pygame.init()

#Window
RESOLUTION = WIDTH, HEIGHT = (1080, 720)
SCREEN = pygame.display.set_mode(RESOLUTION)
backgroundcolor = (55, 174, 15)
game_is_running = True

#background 
background = pygame.image.load("Background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
background = background.convert_alpha()

n =0

#Sprite standig
SCALE = 2.5
FRAME_WIDTH = FRAME_HEIGHT  = 64
player_width, player_height = FRAME_WIDTH * SCALE, FRAME_HEIGHT * SCALE

#player
player = pygame.Rect(WIDTH//2, HEIGHT//2, player_width, player_height)
player_speed = (5)
player_color = (255, 200, 0)
player_state = "stand"

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
Sprites_attack_all = {}
attack_sheet = pygame.image.load('Swordsman_lvl3_attack_with_shadow.png').convert_alpha()
for direction in [Front, Left, Right, Back]:
    frames = []
    for i in range(8):
        frame = attack_sheet.subsurface(FRAME_WIDTH * i, direction, FRAME_WIDTH, FRAME_WIDTH)
        frame = pygame.transform.scale(frame, (player_width, player_height))
        frames.append(frame)
    Sprites_attack_all[direction] = frames
    
#Standing Sprite
Sprites_Stand_all = {}
Spritesheet = pygame.image.load("Swordsman_lvl3_Idle_with_shadow.png").convert_alpha()
animation_index = 0
for direction in [Front, Left, Right, Back]:
    frames = []
    for i in range(12):
        frame = Spritesheet.subsurface(pygame.Rect(FRAME_WIDTH * i, direction, FRAME_WIDTH, FRAME_HEIGHT))
        frame = pygame.transform.scale(frame, (player_width, player_height))
        frames.append(frame)
    Sprites_Stand_all[direction] = frames

#Sprite wlaking
Sprites_walking_all = {}
walk_sheet = pygame.image.load('Swordsman_lvl3_Walk_with_shadow.png').convert_alpha()
for direction in [Front, Left, Back, Right]:
    frames = []
    for i in range(6):
        frame = walk_sheet.subsurface(pygame.Rect(FRAME_WIDTH * i, direction, FRAME_WIDTH, FRAME_HEIGHT))
        frame = pygame.transform.scale(frame, (player_width, player_height))
        frames.append(frame)
    Sprites_walking_all[direction] = frames
    
#CLock
clock = pygame.time.Clock()
FPS = (60)
animation_timer = 0

#Game Loop
while game_is_running:
    moving = False
    standing = False
    SCREEN.fill(backgroundcolor)
    clock.tick(FPS)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
        #Fullscreen 
        if keys[pygame.K_F11]:
            pygame.display.toggle_fullscreen()
        #trigger for attack
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.display.toggle_fullscreen()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                    attack = True
                    animation_index_attack = 0

    #Player movement
    if keys[pygame.K_w]:
        player.y -= player_speed
        if not attack:
            moving = True
            n = Back
    if keys[pygame.K_s]:
        player.y += player_speed
        if not attack:
            moving = True
            n = Front
    if keys[pygame.K_a]:
        player.x -= player_speed
        if not attack:
            moving = True
            n = Left
    if keys[pygame.K_d]:
        player.x += player_speed
        if not attack:
            moving = True
            n = Right

    #if player went out of map
    if player.y >= HEIGHT - player_height//1.3:
        player.y = HEIGHT - player_height//1.3
    if player.y <= -35:
        player.y = -35
    if player.x >= WIDTH - player_width//1.6:
        player.x = WIDTH - player_width//1.6
    if player.x <= -35:
        player.x = -35
    


    #Screen
    SCREEN.blit(background, (0, 0))
    if attack == True:
        SCREEN.blit(Sprites_attack_all[n][animation_index_attack], player.topleft)
    elif moving == True:
        SCREEN.blit(Sprites_walking_all[n][animation_index_walking], player.topleft)
    elif moving == False:
        SCREEN.blit(Sprites_Stand_all[n][animation_index_stand], player.topleft)
    pygame.display.flip()

    if animation_timer == 10:
        animation_index_stand += 1
        animation_index_walking += 1
        if n == Back:
            if animation_index_stand > 3:
                animation_index_stand = 0
        elif animation_index_stand > 11:
            animation_index_stand = 0
        if animation_index_walking > 5:
            animation_index_walking = 0
        if attack:
            animation_index_attack += 1
            if animation_index_attack > 7:
                animation_index_attack = 0
                attack = False
        animation_timer = 0
    animation_timer += 1

pygame.quit