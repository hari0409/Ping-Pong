import pygame, sys, random




def ball_animation():
    global ball_speed_y, ball_speed_x, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # BOUNCING OF BALL
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(loose_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) and ball_speed_x > 0:
        # TOLERANCE=10
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def player_animation(player):
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, tc)
        screen.blit(number_three, (screen_width / 4 - 10, screen_height / 2 + 20))
        screen.blit(number_three, (3 * (screen_width / 4) - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2", False, tc)
        screen.blit(number_two, (screen_width / 4 - 10, screen_height / 2 + 20))
        screen.blit(number_two, (3 * (screen_width / 4) - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, tc)
        screen.blit(number_one, (screen_width / 4 - 10, screen_height / 2 + 20))
        screen.blit(number_one, (3 * (screen_width / 4) - 10, screen_height / 2 + 20))
    if 2100 < current_time - score_time < 2800:
        word = game_font.render("START", False, tc)
        screen.blit(word, (3 * (screen_width / 4) - 10, screen_height / 2 + 20))
        screen.blit(word, ((screen_width / 4) - 10, screen_height / 2 + 20))
    if current_time - score_time < 2800:
        ball_speed_x, ball_speed_y = 0, 0
    else:
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))
        score_time = None


# GENERAL INITIALISATION
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
clock = pygame.time.Clock()

# VARIABLES
# bg_color = (255, 255, 255)
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 15
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("Christmas Classically.otf", 32)
pong_sound = pygame.mixer.Sound("pong.mp3")
score_sound = pygame.mixer.Sound("win.mp3")
loose_sound = pygame.mixer.Sound("loose.mp3")
ball_color=[(237,237,208),(33,9,78),(233,59,129),(247,253,4),(222,137,113),"#f5f7b2","#94d0cc","#21097e","#fbc6a4","#f21170","#f0e3ca"]
paddle_color=[(144, 127, 164),(8,18,129),(245,171,201),(249,178,8),(123,96,121),"#1cc5dc","#eec4c4","#511281","#f4a9a8","#72147e","#ff8303"]
text_color=[(166,214,214),(76,161,163),(255,229,226),(255,229,226),(167,208,205),"#890596","#f29191","#4ca1a3","#ce97b0","#fa9905","#a35709"]
background=[(233,59,129),(165,225,173),(182,201,240),(252,84,4),(255,233,214),"#cf0000","#d1d9d9","#a5e1ad","#afb9c8","#ff5200","#1b1a17"]
n=random.randint(0,len(ball_color)-1)
bc=ball_color[n]
pc=paddle_color[n]
tc=text_color[n]
b=background[n]

# MAIN WINDOW
screen_width = 900
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PING PONG")

# SHAPES
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 20, 20)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 200) # pygame.Rect(pox,poy,breath,length)  

# SCORE TIMER
score_time = True

# MAINLOOP
while True:
    # RUNLOOP
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed -= 15
            if event.key == pygame.K_DOWN:
                player_speed += 15
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_speed += 15
            if event.key == pygame.K_DOWN:
                player_speed -= 15


    # BALL AND PADDLE MOVEMENT
    ball_animation()
    player_animation(player)
    player_animation(opponent)
    # AUTOMATIC OPPONENT
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    # DRAW SHAPES AND BACKGROUND
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, pc, player)
    pygame.draw.rect(screen, pc, opponent)
    pygame.draw.ellipse(screen, bc, ball)
    pygame.draw.aaline(screen, pc, (screen_width / 2, 0), (screen_width / 2, screen_height))

    if score_time:
        ball_restart()

    player_text = game_font.render(f"{player_score}", False, tc)
    opponent_text = game_font.render(f"{opponent_score}", False, tc)

    screen.blit(player_text, (screen_width / 2 - 20, screen_height / 2 - 10))
    screen.blit(opponent_text, (screen_width / 2 + 20, screen_height / 2 - 10))
    # FPS AND UPDATE
    clock.tick(60)
    pygame.display.update()
