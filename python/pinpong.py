from pygame import *


nach = [700, 500]
main_window = display.set_mode(nach)
display.set_caption('ping_pong')


bakfon = transform.scale(image.load('fon.png'), nach)

FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    main_window.blit(backfon,(0, 0))

    display.update()
    clock.tick(FPS)