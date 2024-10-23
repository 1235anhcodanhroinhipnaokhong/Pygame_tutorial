import pygame
from sys import exit

def display_score() : 
    global score
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return score
pygame.init()
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("my Pygame")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False # Bắt đầu với cửa sổ giới thiệu
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (800,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft = (80,300))
player_gravity = 0
# player_stand_scaled = pygame.transform.scale(player_stand, (200, 400)) #phong to buc anh voi ty le 200 * 400
# player_stand = pygame.transform.scale2x(pygame.image.load('graphics/player/player_stand.png').convert_alpha()) # gap doi kich thuoc buc anh
player_stand = pygame.transform.rotozoom(pygame.image.load('graphics/player/player_stand.png').convert_alpha(), 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

title_surface = test_font.render("KHUNG LONG BAO CHUA", True, (111, 196, 169))
title_rectangle = title_surface.get_rect(center = (400, 80)) # tên game


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
                snail_rectangle = snail_surface.get_rect(bottomright = (800,300))
                player_rectangle = player_surface.get_rect(bottomleft = (80,300))
                start_time = pygame.time.get_ticks()
                score = 0
    if game_active :       
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        
        # pygame.draw.line(screen, 'Gold', (0,0), pygame.mouse.get_pos())
        # pygame.draw.rect(screen, '#c0e8ec', text_rectangle)
        # pygame.draw.rect(screen, '#c0e8ec', text_rectangle, 10)
        # screen.blit(text_surface, text_rectangle)
        display_score()
        
        #snail
        if snail_rectangle.right < 0 :
            snail_rectangle.left = 800
            score += 1
        screen.blit(snail_surface,snail_rectangle)
        snail_rectangle.right -= 4
        
        #player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300 
        screen.blit(player_surface, player_rectangle)
        
    #collide
        if snail_rectangle.colliderect(player_rectangle) :
            game_active = False
    else :
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rectangle) #goi buc anh da duoc phong to
        
        screen.blit(title_surface, title_rectangle)
        
        instruction_surface = test_font.render("PRESS SPACE TO START", True, (111, 196, 169))
        instruction_rectangle = instruction_surface.get_rect(center = (400, 350)) # hướng dẫn
        # score_surface = test_font.render(f'Your Score: {your_score}', False, (64,64,64))
        # score_rectangle = score_surface.get_rect(center = (400, 350))
        
        if score == 0 :
            screen.blit(instruction_surface, instruction_rectangle) # nếu 0 điểm thì hướng dẫn hiện ra
        else :
            score_surface = test_font.render(f'Your Score: {score}', False, (64,64,64))
            score_rectangle = score_surface.get_rect(center = (400, 350))
            screen.blit(score_surface, score_rectangle) # còn không thì in ra số điểm
        
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
    