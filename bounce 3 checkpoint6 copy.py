import pygame
import math
from pygame import mixer

pygame.init()
size = (1024, 638)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

block_size = 75
red = (200,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 100)
game_over_text = myfont.render("Game over!", False, (255, 0, 0))

######################    load  sound

mixer.music.load('background.ogg')
mixer.music.play(-1)

######################   do not forget

# Load images

block = pygame.image.load("block.png")
blue_block = pygame.image.load("bl_block.png")
ball = pygame.image.load("ball.png")
ball_2x = pygame.image.load("ball.png")
ball_enemy = pygame.image.load("virus.png")
ball_life = pygame.image.load("heart.png")
ball_enemy_fire = pygame.image.load("fire.png")
doubling_thing = pygame.image.load("doubler.png")
anti_doubling_thing = pygame.image.load("anti_doubler.png")
intro_background = pygame.image.load("intro_bg.jpg")
gameDisplay = pygame.display.set_mode((size[0],size[1]))
pygame.display.set_caption('Bouncing ball')
rings_photo = pygame.image.load("ring.png")
rings_photo2 = pygame.image.load("ring.png")
passed_rings_photo = pygame.image.load("passed_ring.png")

#give correct size

block = pygame.transform.scale(block, (block_size,block_size))
ball = pygame.transform.scale(ball, (block_size,block_size))
ball_enemy = pygame.transform.scale(ball_enemy, (block_size, block_size))
ball_life = pygame.transform.scale(ball_life, (block_size,block_size))
ball_enemy_fire = pygame.transform.scale(ball_enemy_fire, (block_size,block_size))
ball_2x = pygame.transform.scale(ball_2x, (2 * block_size, 2 * block_size))
doubling_thing = pygame.transform.scale(doubling_thing, ( block_size, block_size))
anti_doubling_thing = pygame.transform.scale(anti_doubling_thing, ( block_size, block_size))
rings_photo = pygame.transform.scale(rings_photo,(block_size, 2 * block_size))
rings_photo2 = pygame.transform.scale(rings_photo2,(block_size, block_size))
passed_rings_photo = pygame.transform.scale(passed_rings_photo,(block_size, 2 * block_size))
blue_block = pygame.transform.scale(blue_block,(block_size,block_size))
# Level!


map = ["bbbbbbbbbb      bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                bb                bbbbbbb     bbb      b            ",
    "b                              bbbbbbb           b                                                                                                                                ",
    "b       p                      bbbbbbb         b                                                                                                                                ",
    "b       g                   er  f                                                                                                                                               ",
    "b                                               bbbbbb     b                                                                                                                    ",
    "b  h r 2 ef      f   e    f           2     1 2 bbbbb                                                                                                                                  ",
    "bbbbbbbbbbbbbgggggbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                                                                                        ",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb       b       bb       bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb           bbbbbbb     bbb      b            ",
    "b                                                                                                                   ",
    "b                                                                                                                                                                                                              "
    "                                  b     e                                                               ",
    "b                              bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb     bbb      b                                                                                  ",
    "b                                                                                                                          ",
    "b                                                                                                                                        ",
    "b   h r e  2  1   f  r          e      2     1 2 bbbbb                                                                                          ",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                                                         ",
]


class player(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w  #width
        self.h = h  #height
        self.dx = 0
        self.dy = -10
        self.life = 10
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draws(self, s):
        
        s.blit(ball, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x+8, self.y + camera_y+10, 0.8 * self.w, 0.8 * self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "p":
            bounce = player(j * block_size, i * block_size, block_size, block_size)

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  block_size
        self.dx = 3
        self.dy = 10
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(ball_enemy, (self.x +camera_x, self.y + camera_y))
        self.hitbox = (self.x+camera_x, self.y + camera_y, self.w, self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

enemies = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "e":
            enemies.append(Enemy(j * block_size, i * block_size))

class Enemy_fire(object):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.dy = 10
        self.hitbox = (self.x+6, self.y+5, 2*block_size, 2*block_size)
        #self.image =

    def draws(self, s):
        s.blit(ball_enemy_fire, (self.x + camera_x, self.y+ camera_y))
        self.hitbox = (self.x + camera_x+9, self.y+ camera_y, 0.7*self.w, 0.9*self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

fires = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "f":
            fires.append(Enemy_fire(j * block_size, i * block_size,block_size,block_size))

class Ring(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  2 * block_size
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        self.num = 0
        self.initnum = 0

    def draws(self, s):
        s.blit(rings_photo, (self.x +camera_x, self.y - 3 * block_size/4 + camera_y))
        self.hitbox = (self.x+camera_x + block_size/7, self.y  + camera_y - block_size/2, 0.7*self.w, 0.8*self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

rings = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "r":
            rings.append(Ring(j * block_size, i * block_size))

for ring in rings:
    ring.initnum = len(rings)

class Passed_Ring(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  2 * block_size
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        self.num = 0

    def draws(self, s):
        s.blit(passed_rings_photo, (self.x +camera_x, self.y - 3 * block_size/4 + camera_y))
        self.hitbox = (self.x+camera_x + block_size/7, self.y  + camera_y - block_size/2, 0.7*self.w, 0.8*self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

passed_rings = []

class ball_doublers(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  block_size
        self.hitbox = (self.x, self.y, 10, 10)

    def draws(self, s):
        
        s.blit(doubling_thing, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x+15, self.y + camera_y+12, 0.6*self.w, 0.8*self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

doublers= []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "2":
            doublers.append(ball_doublers(j * block_size, i * block_size))

class ball_anti_doublers(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  block_size
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        
        s.blit(anti_doubling_thing, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x+9 , self.y + camera_y , self.w-9,  self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

anti_doublers= []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "1":
            anti_doublers.append(ball_anti_doublers(j * block_size, i * block_size))

class Extra_life(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  block_size
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        self.num = 0
        self.initnum = 0

    def draws(self, s):
        s.blit(ball_life, (self.x +camera_x, self.y + camera_y))
        self.hitbox = (self.x+camera_x, self.y + camera_y, self.w, self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

lifes = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "h":
            lifes.append(Extra_life(j * block_size, i * block_size))

class brown_blocks(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = block_size  #width
        self.h = block_size  #height
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draws(self, s):
        
        s.blit(block, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x, self.y + camera_y, self.w,  self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

brblocks = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "b":
            brblocks.append(brown_blocks(j * block_size, i * block_size))

class blue_blocks(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = block_size  #width
        self.h = block_size  #height
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draws(self, s):
        
        s.blit(blue_block, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x, self.y + camera_y, self.w,  self.h)
        pygame.draw.rect(screen, green, self.hitbox, 1)

bblocks = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "g":
            bblocks.append(blue_blocks(j * block_size, i * block_size))
def move(x,y,w,h,dx,dy, jump_is_allowed = True):
    global map, camera_x,camera_y
    # increase speed
    dy = dy + gravity

    if dy > 30 and y<300:
        dy = 30

    if dy > 10 and y >300:
        dy = 10

    # save x and y
    save_x, save_y = x, y

    # increase y
    y = y + dy

    rect1 = pygame.Rect(x+8, y+10, 0.8*w, 0.8*h)
    collide = False
    
    for brblock in brblocks:
        rect7 = pygame.Rect(brblock.x+9, brblock.y, block_size-9, block_size)
        if rect1.colliderect(rect7):
            collide = True
    
    
    for doubler in doublers:
        rect3 = pygame.Rect(doubler.x+15 , doubler.y +12, 0.6*block_size, 0.8*block_size)
        if rect1.colliderect(rect3):
            collide = True

    for anti_doubler in anti_doublers:
        rect4 = pygame.Rect(anti_doubler.x+9, anti_doubler.y, block_size-9, block_size)
        if rect1.colliderect(rect4):
            collide = True

    for bblock in bblocks:
        rect6 = pygame.Rect(bblock.x+9, bblock.y, block_size-9, block_size)
        if rect1.colliderect(rect6):
            collide = True
            
    if collide:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = 0

    # change x
    x = x + dx

    rect1 = pygame.Rect(x+8, y+10, 0.8*w, 0.8*h)
    collide = False
    for brblock in brblocks:
        rect7 = pygame.Rect(brblock.x+9, brblock.y, block_size-9, block_size)
        if rect1.colliderect(rect7):
            collide = True
    
    for doubler in doublers:
        rect3 = pygame.Rect(doubler.x +15, doubler.y+12, 0.6*block_size, 0.8*block_size)
        if rect1.colliderect(rect3):
            collide = True

    for anti_doubler in anti_doublers:
        rect4 = pygame.Rect(anti_doubler.x+9, anti_doubler.y, block_size-9, block_size)
        if rect1.colliderect(rect4):
            collide = True
    for bblock in bblocks:
        rect6 = pygame.Rect(bblock.x+9, bblock.y, block_size-9, block_size)
        if rect1.colliderect(rect6):
            collide = True

    if collide:
        x = save_x
    return x,y,dx,dy,jump_is_allowed,collide

def move1(x,y,w,h,dx,dy, jump_is_allowed = True):
    global map, camera_x,camera_y
    # increase speed
    dy = dy + gravity

    if dy > 30 and y<300:
        dy = 30

    if dy > 10 and y >300:
        dy = 10

    # save x and y
    save_x, save_y = x, y

    # increase y
    y = y + dy

    rect1 = pygame.Rect(x, y, w, h)
    collide = False
    for brblock in brblocks:
        rect7 = pygame.Rect(brblock.x+9, brblock.y, block_size-9, block_size)
        if rect1.colliderect(rect7):
            collide = True
    
    for doubler in doublers:
        rect3 = pygame.Rect(doubler.x+15 , doubler.y +12, 0.6*block_size, 0.8*block_size)
        if rect1.colliderect(rect3):
            collide = True

    for anti_doubler in anti_doublers:
        rect4 = pygame.Rect(anti_doubler.x+9, anti_doubler.y, block_size-9, block_size)
        if rect1.colliderect(rect4):
            collide = True

    for fire in fires:
        rect5 = pygame.Rect(fire.x +9, fire.y, 0.7*block_size, 0.9*block_size)
        if rect1.colliderect(rect5):
            collide = True
#self.hitbox = (self.x + camera_x+9, self.y+ camera_y, 0.7*self.w, 0.9*self.h)

    if collide:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = 0

    # change x
    x = x + dx

    rect1 = pygame.Rect(x, y, w, h)
    collide = False
    for brblock in brblocks:
        rect7 = pygame.Rect(brblock.x+9, brblock.y, block_size-9, block_size)
        if rect1.colliderect(rect7):
            collide = True

    for doubler in doublers:
        rect3 = pygame.Rect(doubler.x +15, doubler.y+12, 0.6*block_size, 0.8*block_size)
        if rect1.colliderect(rect3):
            collide = True

    for anti_doubler in anti_doublers:
        rect4 = pygame.Rect(anti_doubler.x+9, anti_doubler.y, block_size-9, block_size)
        if rect1.colliderect(rect4):
            collide = True
    for fire in fires:
        rect5 = pygame.Rect(fire.x +9, fire.y, 0.7*block_size, 0.9*block_size)
        if rect1.colliderect(rect5):
            collide = True

    if collide:
        x = save_x
    return x,y,dx,dy,jump_is_allowed,collide


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, ((0,210,255)))
    return textSurface, textSurface.get_rect()
    


def minus_life(bounce_hitbox,enemy_hitbox):
    if bounce.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > enemy.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > enemy.hitbox[0] and bounce.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            return True
    else:
        return False


def minus_life_of_fire(bounce_hitbox,enemy_fire_hitbox):
    if bounce.hitbox[1] < fire.hitbox[1] + fire.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > fire.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > fire.hitbox[0] and bounce.hitbox[0] < fire.hitbox[0] + fire.hitbox[2]:
            return True
    else:
        return False

def distance_between_ring(bounce_hitbox,Ring_hitbox): #distance between ball and ring
    if bounce.hitbox[1] < ring.hitbox[1] + ring.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > ring.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > ring.hitbox[0] and bounce.hitbox[0] < ring.hitbox[0] + ring.hitbox[2]:
            return True
    else:
        return False

def coltojumphigher(bounce_hitbox,bblock_hitbox): #distance between ball and ring
    if bounce.hitbox[1] < bblock.hitbox[1] + bblock.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > bblock.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > bblock.hitbox[0] and bounce.hitbox[0] < bblock.hitbox[0] + bblock.hitbox[2]:
            return True
    else:
        return False
# def doublers_distance(bounce_hitbox,doubler_hitbox):
#     if bounce.hitbox[0] + bounce.hitbox[2] > doubler.hitbox[0] and bounce.hitbox[0]+block_size < doubler.hitbox[0] + doubler.hitbox[2]:
#         if bounce.hitbox[1] + block_size == doubler.hitbox[1] + doubler.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] == doubler.hitbox[1]+block_size:
#             return True
#     else:
#         return False

# def doublers_distance(bounce_hitbox,doubler_hitbox):
   
#     rect1 = pygame.Rect(bounce.hitbox[0],bounce.hitbox[1], bounce.hitbox[2], bounce.hitbox[3])
#     rect2 = pygame.Rect(doubler.hitbox[0], doubler.hitbox[1], doubler.hitbox[2], doubler.hitbox[3])
#     if bounce.hitbox[1] < doubler.hitbox[1]:
#         if rect1.colliderect(rect2):
#             return True
#     else:
#         return False

def anti_doublers_distance(bounce_hitbox,doubler_hitbox):
   
    rect1 = pygame.Rect(bounce.hitbox[0],bounce.hitbox[1], bounce.hitbox[2], bounce.hitbox[3])
    rect2 = pygame.Rect(anti_doubler.hitbox[0], anti_doubler.hitbox[1], anti_doubler.hitbox[2], anti_doubler.hitbox[3])
    if bounce.hitbox[1] < anti_doubler.hitbox[1]:
        if rect1.colliderect(rect2):
            return True
    else:
        return False

def life_distance(bounce_hitbox,life_hitbox):
    if bounce.hitbox[1] < life.hitbox[1] + life.hitbox[3] and bounce.hitbox[1] + bounce.hitbox[3] > life.hitbox[1]:
        if bounce.hitbox[0] + bounce.hitbox[2] > life.hitbox[0] and bounce.hitbox[0] < life.hitbox[0] + life.hitbox[2]:
            return True
    else:
        return False

def game_quit():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ic,action=None):
    global done
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    smallText = pygame.font.Font("freesansbold.ttf",80)

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        if click[0]==1 and action != None:
            if action=='play':
                return True
            elif action=='quit':
                game_quit()
        textSurf, textRect = text_objects2(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)                

    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x+(w/2)),(y+(h/2)))
        screen.blit(textSurf, textRect)


def game_intro():

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
     
        screen.fill(white)
        screen.blit(intro_background, [0, 0])
        Start = button("Start",50,329,235,60,white,'play')
        if Start:
            return False
        button("Quit",675,325,235,60,white,'quit')
        #mouse = pygame.mouse.get_pos()
        pygame.display.update()
        clock.tick(fps)


gravity = 1  # vertical acceleration
jump_is_allowed = False
look_left = False
camera_x = 0
camera_y = 0
game_over = False
right = 1

done= game_intro()
# Game loop


while not done:
    # Draw background with bright-blue, sky-blue
    screen.fill((135, 206, 250))
    # Update game variables

    # increase speed
    bounce.x,bounce.y,bounce.dx,bounce.dy,jump_is_allowed,collide = move(bounce.x,bounce.y,bounce.w,bounce.h,bounce.dx,bounce.dy,jump_is_allowed)

    if bounce.x + camera_x > size[0]*0.8:
        camera_x = camera_x - 10
    if bounce.x + camera_x < size[0]*0.2:
        camera_x = camera_x + 10
    

    if bounce.y + camera_y > size[1]*0.7:
        camera_y = camera_y - 10
    if bounce.y + camera_y < size[1]*0.3:
        camera_y = camera_y + 10
   
    if bounce.y > size[1]:
        game_over = True




    for enemy in enemies:
        enemy.x, enemy.y, enemy.dx, enemy.dy, _jump, collide = move1(enemy.x, enemy.y, enemy.w,enemy.h,enemy.dx, enemy.dy, True)
        if collide:
            enemy.dx = -enemy.dx
    # enemy movement

    # if right == 1:
    #     if enemy.y > enemy.dy:
    #         enemy.y -= enemy.dy
    #     else:
    #         enemy.y += enemy.dy
    #         right = 0
    # else:
    #     if enemy.y < size[1] - enemy.h - enemy.dy:
    #         enemy.y += enemy.dy
    #     else:
    #         enemy.y -= enemy.dy
    #         right = 1

    

    # Read keyboard/mouse for bounce
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:  # Pressed something
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:  # What exactly did we press?
                if jump_is_allowed:
                    bounce.dy = -25
                    jump_is_allowed = False
            if event.key == pygame.K_LEFT:
                bounce.dx = -10
                look_left = True
            if event.key == pygame.K_RIGHT:
                bounce.dx = 10
                look_left = False
        if event.type == pygame.KEYUP:  # Released something
            if event.key == pygame.K_LEFT:
                if bounce.dx < 0:
                    bounce.dx = 0
            if event.key == pygame.K_RIGHT:
                if bounce.dx > 0:
                    bounce.dx = 0
  
    
    
    # losing life from enemy
    for enemy in enemies:
        losing_life = minus_life(bounce.hitbox, enemy.hitbox)
        if losing_life:
            bounce.life -= 1
            losing=mixer.Sound('attack.wav')
            losing.play()
            if (bounce.x - enemy.x) > 0:
                bounce.x = bounce.x + 0.3 * block_size
                #bounce.y = bounce.y - block_size
            else:
                bounce.x = bounce.x - 0.3 * block_size
                #bounce.y = bounce.y - block_size
            
            if bounce.life == 0:
                done = True

    #lose health of fire
    for fire in fires:
        losing_life_from_fire = minus_life_of_fire(bounce.hitbox,fire.hitbox)
        if losing_life_from_fire:
            bounce.life -= 1
            losing=mixer.Sound('attack.wav')
            losing.play()
            if (bounce.x - fire.x) > 0:
                bounce.x = bounce.x + 0.3*block_size
                #bounce.y = bounce.y - block_size
            else:
                bounce.x = bounce.x - 0.3*block_size
                #bounce.y = bounce.y - block_size
            
            if bounce.life == 0:
                done = True
                fail=mixer.Sound('fail.wav')
                fail.play()
    
    # # doubler of ball
    # for doubler in doublers:
    #     doublesize = doublers_distance(bounce.hitbox,doubler.hitbox)

    #     if  bounce.w == 2 * block_size & bounce.h == 2 * block_size:
    #         doublesize = False
    #     if doublesize:
    #         ball = ball_2x
    #         bounce.x = bounce.x + block_size
    #         bounce.w = 2 * block_size
    #         bounce.h = 2 * block_size
    #         if (bounce.x - j*block_size) > 0:
    #             bounce.x = bounce.x + block_size
    #             #bounce.y = bounce.y - block_size
    #         else:
    #             bounce.x = bounce.x - block_size
                #bounce.y = bounce.y - block_size
    
    # anti-doubler
    for anti_doubler in anti_doublers:
        anti_doublesize = anti_doublers_distance(bounce.hitbox,anti_doubler.hitbox)
        if anti_doublesize==True:
            if bounce.w == 2 * block_size & bounce.h == 2 * block_size:
                bounce.w =  block_size
                bounce.h =  block_size
                ball != ball_2x
                if (bounce.x - j*block_size) > 0:
                    bounce.x = bounce.x + block_size
                    #bounce.y = bounce.y - block_size
                else:
                    bounce.x = bounce.x - block_size
                    #bounce.y = bounce.y - block_size
        if bounce.w == block_size & bounce.h == block_size:
            anti_doublesize==False

    # owning extra life
    for life in lifes:
        life_dist = life_distance(bounce.hitbox,life.hitbox)
        if life_dist ==True:
            bounce.life += 1
            lifes.remove(life)
            life_msc=mixer.Sound('life.wav')
            life_msc.play()



    for ring in rings:
        ring.num = len(rings)


#Lets draw objects
    
    for ring in rings:
        turn_passed = distance_between_ring(bounce.hitbox,ring.hitbox)
        if turn_passed:
            ring.num -=1
            passed_rings.append(Passed_Ring(ring.x,ring.y))
            rings.remove(ring)
            ringsound=mixer.Sound('point.wav')
            ringsound.play()
        else:
            ring.draws(screen) 

    for passed_ring in passed_rings:
        passed_ring.draws(screen)

    for doubler in doublers:
        doubler.draws(screen)

    for anti_doubler in anti_doublers:
        anti_doubler.draws(screen)

    for enemy in enemies:
        enemy.draws(screen)
    
    for fire in fires:
        fire.draws(screen)

    for life in lifes:
        life.draws(screen)

    for brblock in brblocks:
        brblock.draws(screen)

    for bblock in bblocks:
        bblock.draws(screen)

    ball = pygame.transform.scale(ball, (bounce.w,bounce.h))
    bounce.draws(screen)

    #draw life
    screen.blit(ball_life, (500,0))
    label_life=myfont.render(str(bounce.life), 1, (0, 0, 0))
    screen.blit(label_life, (575, 0))

    #draw all rings
    screen.blit(rings_photo2, (10,0))
    label_ring = myfont.render(str(ring.initnum-ring.num), 1, (0, 0, 0))
    label_slash = myfont.render(str("/"), 1, (0, 0, 0))
    label_init_ring = myfont.render(str(ring.initnum), 1, (0, 0, 0))
    screen.blit(label_ring, (70, 5))
    screen.blit(label_slash, (105, 5))
    screen.blit(label_init_ring, (120, 5))

    if game_over:
        screen.blit(game_over_text, (50, 50))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
