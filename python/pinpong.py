from pygame import *


window_size = [700, 500]
#задай фон сцены
window = display.set_mode(window_size)
display.set_caption('ping pong')
background = transform.scale(image.load('fon.jpg'), window_size)


class GameSprite(sprite.Sprite): 
    def __init__(self, player_image,x_size , y_size, x_cor, y_cor, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Rocket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed_y

class Rocket2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y 
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 460:
            self.speed_y *= -1
        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(player2.rect):
            self.speed_x *= -1
            self.speed_y *= 1


player = Rocket('rocket.png', 40, 150, 0, 350, 0, 5)
player2 = Rocket2('rocket.png', 40, 150, 660, 350, 0, 5)
ball = Ball('ball.jpg', 40, 40, 300, 300, 3, 3)

font.init()  
form = font.SysFont('Arial', 30)

score_l = 0
score_r = 0

finish = True
game = True
FPS = 60
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish == True:
        window.blit(background, (0,0))  

        player.update()
        player.reset()
        player2.update()
        player2.reset()
        ball.update()
        ball.reset()

        if ball.rect.x <= -80:
            score_l += 1
            ball.rect.x = 350
        elif ball.rect.x >= 780:
            score_r += 1
            ball.rect.x = 350 

        pl1_score = form.render('Player1:' + str(score_r), True, [0, 0, 0])
        pl2_score = form.render('Player2:' + str(score_l), True, [0, 0, 0])

        window.blit(pl1_score, (0, 25))
        window.blit(pl2_score, (0, 50))


    if score_l == 3:
        finish = False
        form = font.SysFont('Arial', 50)
        pl_fin = form.render('Player2 win', True, [0, 0, 0])
        window.blit(pl_fin, (250, 250))
    if score_r == 3:
        finish = False
        form = font.SysFont('Arial', 50)
        pl_fin1 = form.render('Player1 win', True, [0, 0, 0])
        window.blit(pl_fin1, (250, 250))



    display.update()
    clock.tick(FPS)
