import pygame
import sys
import random
import time
  
pygame.font.init()
# Define the background colour
# using RGB color coding.
background_colour = (234, 212, 252)
  
# Define the dimensions of
# screen object(width,height)
screen = pygame.display.set_mode((800, 600))
  
# Set the caption of the screen
pygame.display.set_caption('Geeksforgeeks')
  
# Fill the background colour to the screen
screen.fill(background_colour)

STAT_FONT = pygame.font.SysFont("comicsans", 50)

GAP = 200
GRAVITY = 5
SCORE = -1700

"""
The pipes would need to be in a random range of 220 and 520 and then we can create a  list of pipes

"""
  
# Update the display using flip
class Pipes:
    def __init__(self):
        # self.y = 520 # only the head 
        self.up_pipe = pygame.image.load("imgs/pipe.png")
        self.down_pipe = pygame.transform.rotate(self.up_pipe, 180)

        # p2 = Pipe(800, 220)
        # p3 = Pipe(600, 220)
        self.pipes = [[600,random.randrange(220,480)], [800, random.randrange(220,480)] ]

    def render(self):
        # pygame.draw.rect(screen,(255,0,0,) ,pygame.Rect(0,0,200,100))
        counter = 0
        for i in self.pipes:
            # print(f"Pipe {counter}: {i[0]} { i[1]}")
            screen.blit(self.up_pipe, (i[0], i[1]))
            screen.blit(self.down_pipe, (i[0], i[1] - GAP - 300 ))
            counter += 1

    def update(self, player):
        global SCORE
        if(len(self.pipes) < 4):
            self.pipes.append([self.pipes[len(self.pipes) - 1][0] + 200, random.randrange(220,480)])
        if(self.pipes[0][0] < 50):
            self.pipes.pop(0)

        for i in range(len(self.pipes)):
            self.pipes[i][0] -= 5
            global SCORE 
            SCORE += 5
            


class Flappy_Bird:

    def __init__(self):
        self.img1 = pygame.image.load("imgs/bird1.png")
        self.img2 = pygame.image.load("imgs/bird2.png")
        self.img3 = pygame.image.load("imgs/bird3.png")
        self.tilt = 0
        self.x = 0
        self.y = 200
        self.x_vel = 2
        self.y_vel = 0
        self.gravity = GRAVITY
        self.rendered_img = self.img1
        self.player_rect = self.rendered_img.get_rect()

    def render(self):

        if(self.y_vel == 0): 
            self.rendered_img = self.img1

        if(self.y_vel > 0):
            self.rendered_img = pygame.transform.rotate(self.img3, 45)
            screen.blit(self.rendered_img, (self.x,self.y,))

        else:
            self.rendered_img = (pygame.transform.rotate(self.img2, 330))
            screen.blit(self.rendered_img, (self.x, self.y))

    def update(self):
        self.x += self.x_vel
        self.y += self.gravity - self.y_vel
        if(self.y_vel > 0): 
            self.y_vel -= 2
        if(self.x >= 400):
            self.x = 400

        if(self.y >= 500):
            self.y = 200
        
  
class Base:
    def __init__(self):
        self.x = 0;
        self.y = 500;
        self.img = pygame.image.load("imgs/base.png")
        self.img = pygame.transform.scale_by(self.img, 2.5 )
        self.rect = self.img.get_rect()
        # print(self.ground_rect)

    def render(self):
        screen.blit(self.img, (self.x,self.y))

# game loop
running = True

def calculate_collisions(player, pipes, ground):
    global running

    len_pipe = 320
    width_pipe = 52

    #handle the ground collision case
    if(player.y > 470):
        # print(player.y)
        running = False
        # print(f"collision at time {time.ctime()}")
        # running = False
    
    #handle the pipe collision
    for i in pipes.pipes:
        #check for each pipe
        pipe1_x = i[0] # down pipe
        pipe1_y = i[1] 
        # print(f"{pipe1_x} {pipe1_y}")

        pipe2_x = i[0] # up pipe
        pipe2_y = i[1] - 300 - GAP 
        # print(f"{pipe2_x} {pipe2_y}")
        # break

        if((player.x > pipe1_x-10 and player.x < pipe2_x + 42) and ((player.y < pipe2_y + 300 and player.y > pipe2_y) or (player.y > pipe1_y))):
            running = False
        if(pipe2_x -10 < player.x -51 < pipe2_x + 42):
            global SCORE
            SCORE += 1
        

player = Flappy_Bird()
pipes = Pipes()


ground = Base()
clock = pygame.time.Clock()
while running:

    screen.fill(background_colour)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                running = False
                sys.exit(0)

            if event.key == pygame.K_SPACE:
                player.y_vel += 20
            
    clock.tick(30)
    player.update()
    player.render()
    pipes.render()
    pipes.update(player)
    ground.render()

    if(SCORE > 0):
        score_label = STAT_FONT.render("Score: " + str(int(SCORE/ 500) ),1,(255,255,255))
        screen.blit(score_label, (600- score_label.get_width() - 15, 10))
    # print(f"Player: {player.x} {player.y}")
    calculate_collisions(player, pipes, ground)

    pygame.display.flip()
