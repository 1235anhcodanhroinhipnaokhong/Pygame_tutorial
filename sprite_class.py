import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.gravity = 0
        player_surface_1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_surface_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_surface_1, player_surface_2]
        self.player_index = 0
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(bottomleft = (50,300)) # phải đặt đúng là image và rect
        
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.1)
    def player_input(self) :
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300 :
            self.gravity = -20
            self.jump_sound.play()
    def apply_gravity(self) :
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300 :
            self.rect.bottom = 300    
    
    def player_animation(self) :
        if self.rect.bottom < 300 :
            self.image = self.player_jump
        else :
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk) : #2
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)] 
    def update(self) :
        self.player_input()
        self.apply_gravity()
        self.player_animation()
        
class Obstacle(pygame.sprite.Sprite) :
    def __init__(self, type):
        super().__init__()   
        if type == 'fly' :
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png')
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png')
            self.frames = [fly_1, fly_2]
            y_pos = 210
            # fly_frame_index = 0
            # fly_surface = fly_frames[fly_frame_index]   
        else : 
            snail_1 = pygame.image.load('graphics/snail/snail1.png')
            snail_2 = pygame.image.load('graphics/snail/snail2.png')
            self.frames = [snail_1, snail_2]
            y_pos = 300
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    def obstacle_animation(self) :
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames) : #2
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)] 
    def update(self) :
        self.obstacle_animation()
        self.rect.x -= 6
        self.destroy() 
    def destroy(self) :
        global score
        if self.rect.right < 0 :
            score += 1
            self.kill() # xóa mỗi obs đi ra ngoài màn hình
def display_score(score) : 
    score_surface = test_font.render(f'Score: {score}', False, (64,64,64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
def display_score_or_instruction(score) : 
    
    if score == 0 : screen.blit(instruction_surface, instruction_rectangle)
    else :
        score_surface = test_font.render(f'Your Score: {score}', False, (64,64,64))
        score_rectangle = score_surface.get_rect(center = (400, 350))
        screen.blit(score_surface, score_rectangle)

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, True) :#COLLIDE SE K HOAT DONG DUNG CACH NEU NHU K CO GROUP, O DAY TA TRUYEN PLAYER GROUP VA OBSTACLE GROUP
    # True thì sẽ xóa sên
        obstacle_group.empty()
        return False
    return True

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

score = 0
bg_Music = pygame.mixer.Sound('audio/bremen.flac')
bg_Music.set_volume(0.5)
bg_Music.play(loops=-1)
#GROUP
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

player_stand = pygame.transform.rotozoom(pygame.image.load('graphics/player/player_stand.png').convert_alpha(), 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400,200))

title_surface = test_font.render("KHUNG LONG BAO CHUA", True, (111, 196, 169))
title_rectangle = title_surface.get_rect(center = (400, 80))

#Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if game_active :
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
        else :
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                
    if game_active :       
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        display_score(score)
        
        player.draw(screen) # DRAW ALL SURFACE
        player.update() #UPDATE ALL METHOD
        
        obstacle_group.draw(screen)
        obstacle_group.update() 
        game_active = collision_sprite()
    else :
        score = 0
        # player_rectangle.bottomleft = (80,300)
        # player_gravity = 0
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rectangle)
        
        screen.blit(title_surface, title_rectangle)
        
        instruction_surface = test_font.render("PRESS SPACE TO START", True, (111, 196, 169))
        instruction_rectangle = instruction_surface.get_rect(center = (400, 350))
        display_score_or_instruction(score)
            
    
    pygame.display.update()
    clock.tick(60) 
    