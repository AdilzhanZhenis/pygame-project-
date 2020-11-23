import pygame
from tkinter import *
from tkinter import messagebox
from time import *
pygame.init()
width = 850
height = 460
fps = 20 #frames per second
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BOUNCE")
clock = pygame.time.Clock()

black = (0, 0, 0)
green = (0, 255, 0)
font = pygame.font.SysFont('comicsans', 30, 1)




# load images 
ball = pygame.image.load("img3.png")
ball_enemy = pygame.image.load("img4.png")
bg = pygame.image.load("bg.jpg")
# load sounds
pygame.mixer.init()
pygame.mixer.music.load("spring.wav")
pygame.mixer.music.play(loops = -1)
b_sound = pygame.mixer.Sound("bounce.wav")
h_sound = pygame.mixer.Sound("hit.wav")

block_size = 50



class player(object):
    def __init__(self, x, y, l, b):
        self.x = x
        self.y = y
        self.l = l
        self.b = b
        self.vel = 20
        self.isJump = 0
        self.vel_v = -50
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(ball, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)


class Enemy(object):
    def __init__(self, x, y, l, b):
        self.x = x
        self.y = y
        self.l = l
        self.b = b
        self.vel = 10
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(ball_enemy, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)


def draw_bounce():
    #screen.blit(bg, (0, 0))
    bounce.draws(screen)
    pygame.display.update()


def draw_enemy():
    enemy.draws(screen)
    pygame.display.update()


def redraw():
    #screen.blit(bg, (0, 0))
    text = font.render("SCORE : " + str(score), 1, black)
    screen.blit(text, (360, 10))
    bounce.draws(screen)
    enemy.draws(screen)

    pygame.display.update()


bounce = player(50, 400, 64, 64)
enemy = Enemy(300, 400, 64, 64)

run = True
gravity = 6 #vertical acceleration
ground_y = height - block_size
bounce_is_jumping = True 


while run:
    #change x
    #bounce.x = bounce.x + bounce.vel


    screen.fill((255,255,255))
    pygame.draw.rect(screen, (30,200,30),(0,ground_y,width,block_size))

    pygame.time.delay(100)
    clock.tick(fps)

   

     #increase speed
    bounce.vel_v += gravity
    if bounce.vel_v > 30:
        bounce.vel_v = 30
    
    #increase y
    bounce.y = bounce.y + bounce.vel_v 

    if bounce.y + block_size > ground_y:
        bounce.y = ground_y - block_size
        bounce_is_jumping = False

    











    # Read keyboard/mouse

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: 
            if (event.key == pygame.K_UP or event.key == pygame.K_w):
                if not bounce_is_jumping:
                    bounce.y -= 200
                    bounce_is_jumping = True

            if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and bounce.x > bounce.vel:
                bounce.x -= bounce.vel
        
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and bounce.x > bounce.vel:
                bounce.x += bounce.vel
        

           




        







    


    draw_bounce()
    #draw_enemy()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

Tk().wm_withdraw()
messagebox.showinfo("GAME RESULT", "Your Score is " + str(score))
