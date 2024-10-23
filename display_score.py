import pygame
from sys import exit

def display_score() : 
    global score
    current_time = pygame.time.get_ticks() - start_time
    score_surface = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)

pygame.init()
screen = pygame.display.set_mode((800, 400)) 
pygame.display.set_caption("my Pygame")
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (800,300))

player_surface = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft = (80,300))
player_gravity = 0

# text_surface = test_font.render("Score", False, (64,64,64))
# text_rectangle = text_surface.get_rect(center = (400, 50))
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
        # pass
        screen.fill("Black")
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
    