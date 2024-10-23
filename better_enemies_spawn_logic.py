import pygame
from sys import exit
from random import randint
def display_score() : 
    global score
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return score
def obstacle_movement(obstacle_list) :
    global score # chua fix bug score
    if obstacle_list :
        for obstacle_rect in obstacle_list :
            if obstacle_rect.right == 0 : score += 1
            obstacle_rect.x -= 5  
            if obstacle_rect.bottom == 300 : screen.blit(snail_surface, obstacle_rect)
            else : screen.blit(fly_surface, obstacle_rect) # bottom = 300 thi ve con sen, con k thi ve con ruoi
            
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.right > 0]
        return obstacle_list
    else : return []
def collisions(player, obstacles) :
    if obstacles :
        for obstacle_rect in obstacles :
            if player.colliderect(obstacle_rect) : return False
    return True
                
pygame.init()
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("my Pygame")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# Obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

fly_surface = pygame.image.load('graphics/Fly/Fly1.png')

obstacle_rectangle_list = []

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft = (80,300))
player_gravity = 0
# player_stand_scaled = pygame.transform.scale(player_stand, (200, 400)) #phong to buc anh voi ty le 200 * 400
# player_stand = pygame.transform.scale2x(pygame.image.load('graphics/player/player_stand.png').convert_alpha()) # gap doi kich thuoc buc anh
player_stand = pygame.transform.rotozoom(pygame.image.load('graphics/player/player_stand.png').convert_alpha(), 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

title_surface = test_font.render("KHUNG LONG BAO CHUA", True, (111, 196, 169))
title_rectangle = title_surface.get_rect(center = (400, 80))

#Timer 
obstacle_timer = pygame.USEREVENT + 1 # cộng 1 với mỗi event thêm vào để k xung đột với những event trước đó
pygame.time.set_timer(obstacle_timer, 1400)

# text_surface = test_font.render("Score", False, (64,64,64))
# text_rectangle = text_surface.g  et_rect(center = (400, 50))
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if game_active :
            if event.type == pygame.MOUSEBUTTONDOWN and player_rectangle.collidepoint(event.pos):
                player_gravity = -20
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    if player_rectangle.bottom >= 300 : 
                        player_gravity = -20
        else :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                player_rectangle = player_surface.get_rect(bottomleft = (80,300))
                start_time = pygame.time.get_ticks()
                score = 0
        if event.type == obstacle_timer and game_active:
            if randint(0, 2) : # random append ruoi hoac sen -> tra ve 0 hoac 1 (TRue hoac False)
                obstacle_rectangle_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100),300)))
            else :
                obstacle_rectangle_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100),210)))
    if game_active :       
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        # pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos())
        # pygame.draw.rect(screen, '#c0e8ec', text_rectangle)
        # pygame.draw.rect(screen, '#c0e8ec', text_rectangle, 10)
        # screen.blit(text_surface, text_rectangle)
        display_score()
        
        #snail bỏ đoạn này để thay đổi logic xíu
        # if snail_rectangle.right < 0 :
        #     snail_rectangle.left = 800
        #     score += 1
        # screen.blit(snail_surface,snail_rectangle)
        # snail_rectangle.right -= 4
        
        #player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300 
        screen.blit(player_surface, player_rectangle)
        
        # Obstacles movement
        obstacle_rectangle_list = obstacle_movement(obstacle_rectangle_list) #goi ham movement va ghi de list obs-rect
    #collide
        game_active = collisions(player_rectangle, obstacle_rectangle_list) # vấn đề là khi va chạm 1 vật thể, ta sẽ k restart game đc, fix bằng cách clear list khi bị va chạm
    else :
        obstacle_rectangle_list.clear() #fix bug
        player_rectangle.bottomleft = (80,300)
        player_gravity = 0
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rectangle)
        
        screen.blit(title_surface, title_rectangle)
        
        instruction_surface = test_font.render("PRESS SPACE TO START", True, (111, 196, 169))
        instruction_rectangle = instruction_surface.get_rect(center = (400, 350))
        # score_surface = test_font.render(f'Your Score: {your_score}', False, (64,64,64))
        # score_rectangle = score_surface.get_rect(center = (400, 350))
        
        if score == 0 :
            screen.blit(instruction_surface, instruction_rectangle)
        else :
            score_surface = test_font.render(f'Your Score: {score}', False, (64,64,64))
            score_rectangle = score_surface.get_rect(center = (400, 350))
            screen.blit(score_surface, score_rectangle)
        
    # keys = pygame.key.get_pressed()
    # if player_rectangle.right < 0 :
    #    player_rectangle.left = 800
    # player_rectangle.right -= 3
    # if player_rectangle.colliderect(snail_rectangle) :
    #     print("collision")
    # mouse_pos = pygame.mouse.get_pos()
    # if player_rectangle.collidepoint(mouse_pos) :
    #     print(pygame.mouse.get_pressed())
    pygame.display.update()
    clock.tick(60) 
    