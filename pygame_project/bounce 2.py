import pygame
import math
pygame.init()
size = (1024, 768)
fps = 20 # Frames per second
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

block_size = 59

pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 100)
game_over_text = myfont.render("Game over!", False, (255, 0, 0))

######################    load  sound 
######################   do not forget

# Load images

block = pygame.image.load("block.png")
ball = pygame.image.load("ball.png")
ball_enemy = pygame.image.load("virus.png")
ball_life = pygame.image.load("heart.png")




block = pygame.transform.scale(block, (block_size,block_size))
ball = pygame.transform.scale(ball, (block_size,block_size))
ball_enemy = pygame.transform.scale(ball_enemy, (2 * block_size,2 * block_size))
ball_life = pygame.transform.scale(ball_life, (block_size,block_size))
# Level!
map = [
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                                                                                                                  ",
    "                                                       b                                                           ",
    "                      bb                        b      b                                                              ",
    "                 bb                bbbbbbb     bbb      b                                     ",
    "         bbbbb                                bbbbb      b                                    ",
    "                          bbbbbbb           bbbbbbbbb     b                                         ",
    "                                        bbbbbbbbb                                                                  ",
    "bbbbbbbb bbbbb bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb                                                                                              ",
]



class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.l = block_size
        self.b = block_size
        self.dx = 0
        self.dy = -5
        self.life = 7
        self.hitbox = (self.x+6, self.y+5, 50, 50)
    def draws(self, s):
        s.blit(ball, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)



bounce = player(50, 400)

class Enemy(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.l = block_size
        self.b = block_size
        self.dy = 10
        self.hitbox = (self.x+6, self.y+5, 50, 50)

    def draws(self, s):
        s.blit(ball_enemy, (self.x, self.y))
        self.hitbox = (self.x+6, self.y+5, 50, 50)
        pygame.draw.rect(screen, green, self.hitbox, 1)


enemy = Enemy(200, 400)



def minus_life(bounce_x,bounce_y,enemy_x,enemy_y):
    distance = math.sqrt((math.pow(enemy_x-bounce_x + block_size/2,2))+(math.pow(enemy_y-bounce_y - block_size/2,2)))
    if distance < 75:
        return True
    else:
        return False





gravity = 1  # vertical acceleration
jump_is_allowed = False
look_left = False
camera_x = 0
game_over = False
right = 1

# Game loop
done = False
while not done:
    # Update game variables

    # increase speed
    bounce.dy = bounce.dy + gravity
    if bounce.dy > 10:
        bounce.dy = 10

    # save x and y
    save_x, save_y = bounce.x, bounce.y

    # increase y
    bounce.y = bounce.y + bounce.dy

    rect1 = pygame.Rect(bounce.x, bounce.y, block_size, block_size)
    collide = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True

    if collide:
        bounce.y = save_y
        # collide while going down?
        if bounce.dy > 0:
            jump_is_allowed = True
        bounce.dy = 0

    if bounce.y > size[1]:
        game_over = True

    # change x
    bounce.x = bounce.x + bounce.dx

    rect1 = pygame.Rect(bounce.x, bounce.y, block_size, block_size)
    collide = False
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                rect2 = pygame.Rect(j*block_size, i*block_size, block_size, block_size)
                if rect1.colliderect(rect2):
                    collide = True

    if collide:
        bounce.x = save_x

    if bounce.x + camera_x > size[0]*0.8:
        camera_x = camera_x - 10
    if bounce.x + camera_x < size[0]*0.2:
        camera_x = camera_x + 10

    # Draw background
    screen.fill((135, 206, 250))

    # pygame.draw.rect(screen, (30,200,30), (0,ground_y,size[0],block_size))

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


    # enemy movement

    if right == 1:
        if enemy.y > enemy.dy:
            enemy.y -= enemy.dy
        else:
            enemy.y += enemy.dy
            right = 0
    else:
        if enemy.y < size[1] - enemy.b - enemy.dy:
            enemy.y += enemy.dy
        else:
            enemy.y -= enemy.dy
            right = 1
    
    #draw ball_enemy
    screen.blit(ball_enemy, (camera_x + enemy.x, enemy.y - 1.5 * block_size))




    # losing life/hp
    losing_life = minus_life(bounce.x,bounce.y,enemy.x,enemy.y)
    if losing_life:
        bounce.life -= 1
        if (bounce.x - enemy.x) > 0:
            bounce.x = bounce.x + block_size
            #bounce.y = bounce.y - block_size 
        else:
            bounce.x = bounce.x - block_size
            #bounce.y = bounce.y - block_size 
        
        if bounce.life == 0:
            done = True
    #draw life
    screen.blit(ball_life, (500,0))
    label_life=myfont.render(str(bounce.life), 1, (0, 0, 0))
    screen.blit(label_life, (565, 0))









    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "b":
                screen.blit(block, (j*block_size + camera_x, i*block_size))
           


    if look_left:
        screen.blit(ball, (bounce.x + camera_x, bounce.y))
    else:
        screen.blit(ball, (bounce.x + camera_x, bounce.y))


    

    if game_over:
        screen.blit(game_over_text, (50, 50))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()