import pygame
import math
from pygame import mixer

pygame.init()
size = (1400, 850)
fps = 30 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

block_size = 75
red = (200,0,0)
black = (0,0,0)
green = (0,255,0)
white = (255,255,255)
light_blue = (135, 206, 250)

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
ball_2x = pygame.image.load("ball.png")
ball_enemy = pygame.image.load("virus.png")
ball_life = pygame.image.load("heart.png")
ball_enemy_fire = pygame.image.load("fire.png")
doubling_thing = pygame.image.load("doubler.png")
anti_doubling_thing = pygame.image.load("anti_doubler.png")
intro_background = pygame.image.load("intro_bg.jpg")
game_over_background = pygame.image.load("game_over.jpeg")
gameDisplay = pygame.display.set_mode((size[0],size[1]))
pygame.display.set_caption('Bouncing ball')
rings_photo = pygame.image.load("ring.png")
rings_photo2 = pygame.image.load("ring.png")
passed_rings_photo = pygame.image.load("passed_ring.png")
pause_photo = pygame.image.load("pause.png")
resume_photo = pygame.image.load("resume.jpg")
main_menu_photo = pygame.image.load("main_menu.jpg")
restart_photo = pygame.image.load("restart.jpg")
pause_page_photo = pygame.image.load("pause_page_photo.jpg")
second_level_photo = pygame.image.load("lvl2.jpg")

ball_list = [pygame.image.load('ball1.png'), pygame.image.load('ball2.png'),
pygame.image.load('ball3.png'), pygame.image.load('ball4.png')]


door_list = [pygame.image.load('door.png'), pygame.image.load('33.png'),
pygame.image.load('66.png'), pygame.image.load('100.png')]

arrows_list = [pygame.image.load('up-arrow.png'), pygame.image.load('right-arrow.png'),
pygame.image.load('down-arrow.png'), pygame.image.load('left-arrow.png')]

#give correct size

block = pygame.transform.scale(block, (block_size,block_size))
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
resume_photo = pygame.transform.scale(resume_photo,(3 * block_size,2*block_size))
main_menu_photo = pygame.transform.scale(main_menu_photo,(3 * block_size,2*block_size))
restart_photo = pygame.transform.scale(restart_photo,(3 * block_size,2*block_size))


pause_photo = pygame.transform.scale(pause_photo,(2*block_size,2*block_size))
intro_background = pygame.transform.scale(intro_background,(size[0],size[1]))
game_over_background = pygame.transform.scale(game_over_background,(size[0],size[1]))
pause_page_photo= pygame.transform.scale(pause_page_photo,(size[0],size[1]))
second_level_photo= pygame.transform.scale(second_level_photo,(size[0],size[1]))


for i in range(4):
    door_list[i] = pygame.transform.scale(door_list[i],(block_size,block_size))
    ball_list[i] = pygame.transform.scale(ball_list[i],(block_size,block_size))
    arrows_list[i] = pygame.transform.scale(arrows_list[i],(block_size,block_size))



start = False

introduction = True

pause = False

game_over = False

restart = False

# Level!


maps = [[
       "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "b                                           bbbbbbbbb                  bb     bbbbbbbbbbbbb",
       "b                                          r                                              b",
       "b    p                       bbbbbbffbbbbbbbbbbbbbbb               r  bbb      bbbbbbbbbbbb",
       "b    b            e     b                                    bbbfbbbbbbbbbb               b",
       "b    bbbbbbffbbbbbbbbbbbb                           1                               e     b",
       "b    bbbbbbbbbbbbbbbbbbbbbbb                     fbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "b                                   zy     fbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "bbbbbbbbbbbbe    b              bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
       "bbbbbbbffbbbbbbbbb                                                                        b",
       "b                                  bb                                                   r b",
       "b                                 zbby                                                    b",
       "b                                bbbbbb  e      f                                         b",
       "b                           ffbbbbbbbbbbbbbbffbbbbbbb                                     b",
       "b                           bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                             b",
       "d          r  e             bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                             b",
       "bbbbbbggbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbgbbbbb"
       ],
    
[
    "bbbbbbbbbb      bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "b                              bbbbbbbr                     bbb           bbbbbbbbbbbbbbbbbbbb",
    "b                              bbbbbbbbbbbb    bbbbbb      fbb     bbbbbb b               bbbb",
    "b                          r                   bbbbbbb     fbb     bh     bbbbb           bbbb",
    "b      p   rh                                  bbbbbbbb    fbbb    b      bbbbb           bbbb",
    "d     ebbffbb       n f   e   e             e   hbbbbbb    fbbb  bbb     bb               bbbb",
    "bbbbbbbbbbbbb      bbbbbbbbbbbbbbbb    bbbbbbbbbbbbbbb e     r   bbb    fbb              gbbbb",
    "bbbbbbbbbbbbbb     bbbbbbbbbbbbbbb    bbbbbbbbbbbbbbbbbbbbbbbbbbbbbb   fbbb        b     rbbbb",
    "b      bbbbbbbb    bbbbb           bbb                                             b     hbbbb",
    "b  b     bbbbbbb   bbbbb           bbbb                                           bbbbbbbbbbbb",                                                                                                                                    
    "b  bbb    bbbbbb     bbb        bbbbbbbbbbb h ffbbbb         b   e    e  b                bbbb", 
    "b  bbbbb          bb           h bbbbbbbbbbbbbbbbbbbbbb     bbbbbbbbgbbbbb               bbbbb",
    "b     bbbbbbbbbbbbb     bffffbb       bbb                     bbbb             bbbb    bbbbbbb",
    "b               bbbbbbbbbbbbbbbb      bbb                     bbbbh  bbbbbbbbbbbbbb    bbbbbbb",
    "bf     h r e  b       r          b e  bbbr      bbbbb         bbbbbbbbbbbbbbbbbbbbbr hhbbbbbbb",
    "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
]]


walkCount = 0
last_view=[0,1]
class player(object):
    global walkCount
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = block_size  #width
        self.h = block_size  #height
        self.dx = 0
        self.dy = -10
        self.life = 10
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draws(self, s):
        global walkCount,last_view
        self.hitbox = (self.x + camera_x+11, self.y + camera_y+15, 0.7 * self.w, 0.7 * self.h)


        if walkCount + 1 >= 12:
            walkCount = 0

        if walkCount - 1 <= -12:
            walkCount = 0

        elif look_left==True:
            screen.blit(ball_list[walkCount//3], (self.x + camera_x, self.y + camera_y))
            walkCount -= 1
            last_view.append(walkCount//3)
        elif look_right==True:
            screen.blit(ball_list[walkCount//3], (self.x + camera_x, self.y + camera_y))
            walkCount += 1
            last_view.append(walkCount//3)



        else:
            k = last_view[-1]
            screen.blit(ball_list[k], (self.x + camera_x, self.y + camera_y))
            

        

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
        #pygame.draw.rect(screen, green, self.hitbox, 1)




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
        #pygame.draw.rect(screen, green, self.hitbox, 1)


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
        #pygame.draw.rect(screen, green, self.hitbox, 1)





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
        #pygame.draw.rect(screen, green, self.hitbox, 1)


class GameArrows(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w =  block_size
        self.h =  block_size


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
        #pygame.draw.rect(screen, green, self.hitbox, 1)
 

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
        #pygame.draw.rect(screen, green, self.hitbox, 1)

 

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
        #pygame.draw.rect(screen, green, self.hitbox, 1)



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
        #pygame.draw.rect(screen, green, self.hitbox, 1)



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
        #pygame.draw.rect(screen, green, self.hitbox, 1)

 

class Doors(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = block_size  #width
        self.h = block_size  #height
        self.hitbox = (self.x, self.y, 50, 50)
    
    def draws(self, s):
        
        s.blit(door_list, (self.x + camera_x, self.y + camera_y))
        self.hitbox = (self.x + camera_x, self.y + camera_y, self.w,  self.h)
        #pygame.draw.rect(screen, green, self.hitbox, 1)



def move(x,y,w,h,dx,dy, jump_is_allowed = True):
    global map, camera_x,camera_y,change_level
    # increase speed
    dy = dy + gravity

    if dy > 30 and y<300:
        dy = 30

    if dy > 10 and y>300:
        dy = 10

    # save x and y
    save_x, save_y = x, y

    # increase y
    y = y + dy

    rect1 = pygame.Rect(x+11, y+15, 0.7*w, 0.7*h)
    collide = False
    collide_bblock = False
    dbsize = False
    
    for brblock in brblocks:
        rect7 = pygame.Rect(brblock.x+9, brblock.y, block_size-9, block_size)
        if rect1.colliderect(rect7):
            collide = True
    
    
    for doubler in doublers:
        rect3 = pygame.Rect(doubler.x+15 , doubler.y +12, 0.6*block_size, 0.8*block_size)
        if rect1.colliderect(rect3):
            collide = True
            dbsize = True


    for anti_doubler in anti_doublers:
        rect4 = pygame.Rect(anti_doubler.x+9, anti_doubler.y, block_size-9, block_size)
        if rect1.colliderect(rect4):
            collide = True

    for bblock in bblocks:
        rect6 = pygame.Rect(bblock.x+5, bblock.y, block_size-15, block_size)
        if rect1.colliderect(rect6):
            collide_bblock = True

    for door in doors:
        rect8 = pygame.Rect(door.x+9, door.y, block_size-9, block_size)
        if rect1.colliderect(rect8):
            collide= True
            
    if collide:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = 0

    if collide_bblock:
        y = save_y
        # collide while going down?
        if dy > 0:
            jump_is_allowed = True
        dy = -35
    
    if dbsize:
        w = 2 * block_size
        h = 2 * block_size
            #bounce.y = bounce.y - block_size 



    # change x
    x = x + dx

    rect1 = pygame.Rect(x+11, y+15, 0.7*w, 0.7*h)
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
        rect6 = pygame.Rect(bblock.x+5, bblock.y, block_size-15, block_size)
        if rect1.colliderect(rect6):
            collide = True

    for door in doors:
        rect8 = pygame.Rect(door.x+9, door.y, block_size-9, block_size)
        if rect1.colliderect(rect8):
            collide = True
            if ring.num == 0:
                change_level = True

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

    for bblock in bblocks:
        rect6 = pygame.Rect(bblock.x+9, bblock.y, block_size-9, block_size)
        if rect1.colliderect(rect6):
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

    for door in doors:
        rect8 = pygame.Rect(door.x+9, door.y, block_size-9, block_size)
        if rect1.colliderect(rect8):
            collide= True
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

    for bblock in bblocks:
        rect6 = pygame.Rect(bblock.x+9, bblock.y, block_size-9, block_size)
        if rect1.colliderect(rect6):
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

    for door in doors:
        rect8 = pygame.Rect(door.x+9, door.y, block_size-9, block_size)
        if rect1.colliderect(rect8):
            collide= True

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

def button2(msg,x,y,w,h,action=None):
    global done
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    smallText = pygame.font.Font("freesansbold.ttf",80)
    #pygame.draw.rect(screen,green,(x,y,w,h))
    screen.blit(msg,(x-30,y-15))
    

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0]==1 and action != None:
            if action=='play' or action=='main_page' or action=='restart':
                return True
            elif action=='quit':
                game_quit()

                      

        


def game_intro():
    global start

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
                
     
        screen.fill(white)
        screen.blit(intro_background, [0, 0])
        if button("Start",100,430,280,85,white,'play'):
            start = True
        button("Quit",950,430,280,85,white,'quit')
        #mouse = pygame.mouse.get_pos()
        if start:
            intro = False
        pygame.display.update()
        clock.tick(fps)

def game_pause():
    global start,pause,introduction,restart

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
                
     
        screen.fill(white)
        screen.blit(pause_page_photo, [0, 0])
        if button2(resume_photo,250,400,210,140,'play'): #if button2(pause_photo,1300,20,1.5*block_size,1.5*block_size,'play'):
            start = True
            pause = False
        if button2(main_menu_photo,650,400,210,140,'main_page'):
        	introduction = True
        	start = False
        	pause = False
        if button2(restart_photo,1050,400,210,140,'restart'):
        	print("Iwas here")
        	introduction = False
        	pause = False
        	restart = True

        # if button2(Main_menu,1300,20,1.5*block_size,1.5*block_size,'play'):
        #     introduction=True

        #button("Quit",950,430,280,85,white,'quit') #if button2(pause_photo,1300,20,1.5*block_size,1.5*block_size,'play'):
        #mouse = pygame.mouse.get_pos()
        if start or restart or introduction:
            intro = False
        pygame.display.update()
        clock.tick(fps)

def game_over_page():
    global start,game_over
    a=True
    while a:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit()
        screen.fill(white)
        screen.blit(game_over_background,[0,0])
        if button("Restart",1060,150,200,70,white,'play'):
            start = True
            game_over = False
            print("Hello")
        button("Quit",1060,250,200,70,white,'quit')
        if start:
            a=False
        
        pygame.display.update()
        clock.tick(fps)


gravity = 1  # vertical acceleration
jump_is_allowed = False
look_left = False
look_right = False
camera_x = 0
camera_y = 0
right = 1

done= False




# Game loop

doors = []
bblocks = []
brblocks = []
lifes = []
anti_doublers= []
doublers= []
passed_rings = []
rings = []
enemies = []
fires = []
arrows=[]
map = maps[0]
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "p":
            bounce = player(j * block_size, i * block_size)
        if map[i][j] == "e":
            enemies.append(Enemy(j * block_size, i * block_size))
        if map[i][j] == "f":
            fires.append(Enemy_fire(j * block_size, i * block_size,block_size,block_size))
        if map[i][j] == "r":
            rings.append(Ring(j * block_size, i * block_size))
        if map[i][j] == "2":
            doublers.append(ball_doublers(j * block_size, i * block_size))
        if map[i][j] == "1":
            anti_doublers.append(ball_anti_doublers(j * block_size, i * block_size))
        if map[i][j] == "h":
            lifes.append(Extra_life(j * block_size, i * block_size))
        if map[i][j] == "b":
            brblocks.append(brown_blocks(j * block_size, i * block_size))
        if map[i][j] == "g": #blue blocks
            bblocks.append(blue_blocks(j * block_size, i * block_size))
        if map[i][j] == "d": #door
            doors.append(Doors(j * block_size, i * block_size))
        if map[i][j] == "n": #hint=namek
            arrows.append(GameArrows(j * block_size, i * block_size))

for ring in rings:
    ring.initnum = len(rings)
change_level=False

level = 1

while not done:
    

    if introduction:
        game_intro()

    if start:#game_loop
        introduction=False
        change_level=False
        # Draw background with bright-blue, sky-blue
        if level==1:
            screen.fill(light_blue)
        if level ==2:
            screen.blit(second_level_photo, [0, 0])

        # Update game variables

        # increase speed
        bounce.x,bounce.y,bounce.dx,bounce.dy,jump_is_allowed,collide = move(bounce.x,bounce.y,bounce.w,bounce.h,bounce.dx,bounce.dy,jump_is_allowed)

        if bounce.x + camera_x > size[0]*0.8:
            camera_x = camera_x - 10
        if bounce.x + camera_x < size[0]*0.2:
            camera_x = camera_x + 10
        

        if bounce.y + camera_y > size[1]*0.8:
            camera_y = camera_y - 15
        if bounce.y + camera_y < size[1]*0.2:
            camera_y = camera_y + 15


        if bounce.life == 0:
            game_over = True
            fail=mixer.Sound('fail.wav')
            fail.play()








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
                        look_left = False
                        look_right = False

                if event.key == pygame.K_LEFT:
                    bounce.dx = -10
                    look_left = True
                    look_right = False
                if event.key == pygame.K_RIGHT:
                    bounce.dx = 10
                    look_right = True
                    look_left=False
            if event.type == pygame.KEYUP:
                look_left = False
                look_right = False
                




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
                
                # if bounce.life == 0:
                #     done = True

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
        if bounce.life < 0:
            bounce.life = 0       
                
        
        
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

        for door in doors:
            if ring.num == 0:
                if abs(bounce.x - door.x) > 200:
                    screen.blit(door_list[0],(door.x+camera_x,door.y+camera_y))
                if 150<abs(bounce.x - door.x) < 200:
                    screen.blit(door_list[1],(door.x+camera_x,door.y+camera_y))
                if 100<abs(bounce.x - door.x) < 150:
                    screen.blit(door_list[2],(door.x+camera_x,door.y+camera_y))
                if 50<abs(bounce.x - door.x) < 100:
                    screen.blit(door_list[3],(door.x+camera_x,door.y+camera_y))
                


                if abs(bounce.x - door.x) < 30:
                    doors.remove(door)
                
            else:
                screen.blit(door_list[0],(door.x+camera_x,door.y+camera_y))

        for door in doors:
            for arrow in arrows:
                if abs(bounce.x-door.x) > abs(bounce.y-door.y):
                    if bounce.x-door.x > 0:
                        screen.blit(arrows_list[3],(arrow.x+camera_x,arrow.y+camera_y))
                    if bounce.x-door.x < 0:
                        screen.blit(arrows_list[1],(arrow.x+camera_x,arrow.y+camera_y))
                if abs(bounce.x-door.x) < abs(bounce.y-door.y):
                    if bounce.y-door.y > 0:
                        screen.blit(arrows_list[0],(arrow.x+camera_x,arrow.y+camera_y))
                    if bounce.y-door.y < 0:
                        screen.blit(arrows_list[2],(arrow.x+camera_x,arrow.y+camera_y))

        if button2(pause_photo,1300,20,1.5*block_size,1.5*block_size,'play'):
            pause = True
        #screen.blit(pause_photo,(1270,0))
        bounce.draws(screen)



        #draw level number
        #screen.blit(myfont.render(str("LEVEL"), 1, black), (700, 0))
        drw_level=myfont.render("LEVEL "+str(level), 1, black)
        screen.blit(drw_level, (300, 0))



        

        


        #draw life
        screen.blit(ball_life, (700,0))
        label_life=myfont.render(str(bounce.life), 1, black)
        screen.blit(label_life, (780, 0))

        #draw all rings
        screen.blit(rings_photo2, (10,0))
        label_ring = myfont.render(str(ring.initnum-ring.num), 1, black)
        label_slash = myfont.render(str("/"), 1, black)
        label_init_ring = myfont.render(str(ring.initnum), 1, black)
        screen.blit(label_ring, (70, 5))
        screen.blit(label_slash, (105, 5))
        screen.blit(label_init_ring, (120, 5))

        if game_over:
            start = False
        if change_level:
            start = False
            
    if pause:
        game_pause()
        if introduction or restart:
        	for i in range(len(map)):
        		for j in range(len(map[i])):
        			if map[i][j] == "p":
        				bounce = player(j * block_size, i * block_size)
        	rings = []
	        for i in range(len(map)):
	            for j in range(len(map[i])):
	                if map[i][j] == "r":
	                    rings.append(Ring(j * block_size, i * block_size))

	        for ring in rings:
	            ring.initnum = len(rings)

	        passed_rings = []

	        lifes = []

	        for i in range(len(map)):
	            for j in range(len(map[i])):
	                if map[i][j] == "h":
	                    lifes.append(Extra_life(j * block_size, i * block_size))



    if game_over:
        game_over_page()
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "p":
                    bounce = player(j * block_size, i * block_size)
        rings = []
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "r":
                    rings.append(Ring(j * block_size, i * block_size))

        for ring in rings:
            ring.initnum = len(rings)

        passed_rings = []

        lifes = []

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "h":
                    lifes.append(Extra_life(j * block_size, i * block_size))

    if change_level:
        del bblocks[:]
        del brblocks[:]
        del lifes[:]
        del anti_doublers[:]
        del doublers[:]
        del passed_rings[:]
        del rings[:]
        del enemies[:]
        del fires[:]
        del doors[:]
        del arrows[:]
        map = maps[1]
        level=level+1
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == "p":
                    bounce = player(j * block_size, i * block_size)
                if map[i][j] == "e":
                    enemies.append(Enemy(j * block_size, i * block_size))
                if map[i][j] == "f":
                    fires.append(Enemy_fire(j * block_size, i * block_size,block_size,block_size))
                if map[i][j] == "r":
                    rings.append(Ring(j * block_size, i * block_size))
                if map[i][j] == "2":
                    doublers.append(ball_doublers(j * block_size, i * block_size))
                if map[i][j] == "1":
                    anti_doublers.append(ball_anti_doublers(j * block_size, i * block_size))
                if map[i][j] == "h":
                    lifes.append(Extra_life(j * block_size, i * block_size))
                if map[i][j] == "b":
                    brblocks.append(brown_blocks(j * block_size, i * block_size))
                if map[i][j] == "g":
                    bblocks.append(blue_blocks(j * block_size, i * block_size))
                if map[i][j] == "d":
                    doors.append(Doors(j * block_size, i * block_size))
                if map[i][j] == "n": #hint=namek
                    arrows.append(GameArrows(j * block_size, i * block_size))

        
        for ring in rings:
            ring.initnum = len(rings)
        start =True
        





    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
