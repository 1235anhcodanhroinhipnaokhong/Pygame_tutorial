import pygame
from sys import exit

pygame.init() #khởi tạo pygame
screen = pygame.display.set_mode((800, 400)) #tạo cửa sổ
pygame.display.set_caption("my Pygame") #đặt caption cho cửa sổ
clock = pygame.time.Clock()
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #quit cửa sổ đồng thời exit chương trình
    pygame.display.update() #chạy cửa sổ 
    clock.tick(60) # vòng lặp k đc chạy quá 60 lần trên giây