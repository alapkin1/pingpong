from pygame import *


window_size = [700, 500]
#задай фон сцены
window = display.set_mode(window_size)
display.set_caption('ping pong')
background = transform.scale(image.load('fon.jpg'), window_size)


class GameSprite(sprite.Sprite): 
    def __init__(self, player_image,x_size , y_size, x_cor, y_cor, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Rocket(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y < 635:
            self.rect.y += self.speed 

class Rocket2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y < 635:
            self.rect.y += self.speed 

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed



player = Rocket('rocket.png', 40, 150, 0, 350, 5)
player2 = Rocket2('rocket.png', 40, 150, 660, 350, 5)
ball = Ball('ball.jpg', 40, 40, 300, 300, 1)

game = True
FPS = 60
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    window.blit(background, (0,0))    
    player.update()
    player.reset()
    player2.update()
    player2.reset()
    ball.update()
    ball.reset()
    


    display.update()
    clock.tick(FPS)
