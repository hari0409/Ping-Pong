import pygame, sys, random


# CLASSES
class Ball:
    def __init__(self, screen, color, posx, posy, radius):
        self.screen = screen
        self.color = color
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.dx=0
        self.dy=0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posx, self.posy), self.radius)

    def start_moving(self):
        self.dx=0.55
        self.dy=0.55

    def move(self):
        self.posx+=self.dx
        self.posy+=self.dy

    def paddle_collision(self):
        self.dx = -self.dx
    def wall_collision(self):
        self.dy = -self.dy

    def restart_pos(self):
        self.posx=width//2
        self.posy=height//2
        self.dx=0
        self.dy=0
        self.show()
class Paddle:
    def __init__(self,screen,color,posx,posy,width,height):
        self.screen = screen
        self.color = color
        self.posx = posx
        self.posy = posy
        self.width=width
        self.height=height
        self.state="stopped"
        self.show()

    def show(self):
        pygame.draw.rect(self.screen,self.color,(self.posx,self.posy,self.width,self.height))

    def move(self):
        if self.state=="up":
            self.posy-=0.5
        if self.state=="down":
            self.posy+=0.5
        if self.state=="left":
            self.posx-=0.5
        if self.state=="right":
            self.posx+=0.5
    def clamp(self):
        if self.posy<=0:
            self.posy=0
        if self.posy+self.height>=height:
            self.posy=height-self.height
        if self.posx+self.width>=width//2:
            self.posx=width//2-self.width
        if self.posx<=0:
            self.posx=0
        if self.posx+self.width>=width:
            self.posx=width-self.width
    def clamp1(self):
        if self.posy<=0:
            self.posy=0
        if self.posy+self.height>=height:
            self.posy=height-self.height
        if self.posx<=width//2:
            self.posx=width//2
        if self.posx<=0:
            self.posx=0
        if self.posx+self.width>=width:
            self.posx=width-self.width
    def restart_pos(self):
        self.posy=height//2-self.height//2
        self.state="stopped"
        self.show()
class CollisionManager:
    def btw_ball_paddle1(self,ball,paddle1):
        if ball.posy+ball.radius>paddle1.posy and ball.posy-ball.radius<paddle1.posy+paddle1.height:
            if ball.posx-ball.radius<=paddle1.posx+paddle1.width:
                return True
        return False

    def btw_ball_paddle2(self,ball,paddle2):
        if ball.posy +ball.radius>paddle2.posy and ball.posy-ball.radius<paddle2.posy+paddle2.height:
            if ball.posx+ball.radius>=paddle2.posx:
                return True
        return  False

    def btw_ball_wall(self,ball):
        if ball.posy-ball.radius<=0:
            return True
        if ball.posy+ball.radius>=height:
            return True
        return False
    def check_goal1(self,ball):
        return ball.posx-ball.radius>=width
    def check_goal2(self,ball):
        return ball.posx+ball.radius<=0

class Score:
    def __init__(self,screen,points,posx,posy):
        self.screen=screen
        self.points=points
        self.posx=posx
        self.posy=posy
        self.font=pygame.font.SysFont("monospace",75,bold=True)
        self.label=self.font.render(self.points,0,line_color)
        self.show()
    def show(self):
        self.screen.blit(self.label,(self.posx-self.label.get_rect().width//2,self.posy))

    def increase(self):
        points=int(self.points)+1
        self.points=str(points)
        self.label = self.font.render(self.points, 0, line_color)

    def restart(self):
        self.points="0"
        self.label=self.font.render(self.points,0,line_color)
pygame.init()

# CONSTANT
width = 900
height = 500
bgcolor = (0, 0, 0)
line_color = (255, 255, 255)
ball_color=(0,255,0)
# SCREEN FOR THE GAME
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PING PONG")


# FUNCTIONS
def draw_board():
    screen.fill(bgcolor)
    pygame.draw.line(screen, line_color, (width // 2, 0), (width // 2, height), 5)

def restart():
    draw_board()
    score1.restart()
    score2.restart()
    ball.restart_pos()
    paddle1.restart_pos()
    paddle2.restart_pos()

# FUNCTION CALLING
draw_board()
# OBJECTS
ball = Ball(screen, ball_color, width // 2, height // 2, 10)
paddle1=Paddle(screen,line_color,15,height//2-60,20,120)
paddle2=Paddle(screen,line_color,width-20-15,height//2-60,20,120)
collision=CollisionManager()
score1=Score(screen,"0",width//4,15)
score2=Score(screen,"0",width-width//4,15)
playing=False
# MAINLOOP FOR RUNNING
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ball.start_moving()
                playing=True
            if event.key == pygame.K_ESCAPE:
                restart()
                playing = False
            if event .key==pygame.K_w:
                paddle1.state="up"
            if event.key == pygame.K_s:
                paddle1.state = "down"
            # if event.key==pygame.K_a:
            #     paddle1.state="left"
            # if event.key == pygame.K_d:
            #     paddle1.state = "right"
            if event.key==pygame.K_UP:
                paddle2.state="up"
            if event.key==pygame.K_DOWN:
                paddle2.state="down"
            # if event.key==pygame.K_RIGHT:
            #     paddle2.state="right"
            # if event.key==pygame.K_LEFT:
            #     paddle2.state="left"
        if event.type==pygame.KEYUP:
            paddle1.state="stopped"
            paddle2.state="stopped"

    if playing:
        # REMOVE TRACE
        draw_board()
        # BALL MOVE
        ball.move()
        ball.show()
        # PADDLE2 SHOW
        paddle2.show()
        paddle2.move()
        paddle2.clamp1()
        # PADDLE1 SHOW
        paddle1.show()
        paddle1.move()
        paddle1.clamp()
        # CHECK COLLISION
        if collision.btw_ball_paddle1(ball,paddle1):
            ball.paddle_collision()
        if collision.btw_ball_paddle2(ball,paddle2):
            ball.paddle_collision()
        if collision.btw_ball_wall(ball):
            ball.wall_collision()
        if collision.check_goal1(ball):
            score1.increase()
            ball.restart_pos()
            paddle1.restart_pos()
            paddle2.restart_pos()
        if collision.check_goal2(ball):
            score2.increase()
            ball.restart_pos()
            paddle2.restart_pos()
            paddle1.restart_pos()

    score1.show()
    score2.show()
    pygame.display.update()
