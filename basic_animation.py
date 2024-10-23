import pygame
from sys import exit

pygame.init() #khởi tạo pygame
screen = pygame.display.set_mode((800, 400)) #tạo cửa sổ
pygame.display.set_caption("my Pygame") #đặt caption cho cửa sổ
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) #(font=default, size)

sky_surface = pygame.image.load('graphics/Sky.png').convert()#tạo một surface trong display surface
ground_surface = pygame.image.load('graphics/ground.png').convert()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 800

text_surface = test_font.render("My game", False, 'Black') #text, khử răng cưa, color
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #quit cửa sổ đồng thời exit chương trình
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (0, 0))
    if snail_x_pos < -100 :
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos,264))
    snail_x_pos -= 4
    pygame.display.update() #chạy cửa sổ
    clock.tick(60) # vòng lặp k đc chạy quá 60 lần trên giây
    