from pygame import *

win_size = (700,500)
FPS = 60
p_size = (30, 120)
p_speed = 2

window = display.set_mode(win_size)
display.set_caption('ping-pong')
background = (255,255,255)

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, size, speed = 0):
        super().__init__()
        self.image = transform.scale(image.load(img), size)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.bottom < win_size[1]:
            self.rect.y += self.speed
    def update_right(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.bottom < win_size[1]:
            self.rect.y += self.speed

p1 = Player('platform.png',30, 100,p_size,p_speed)
p2 = Player('platform.png',640,100,p_size,p_speed)

clock = time.Clock()
application = True
while application:
    for e in event.get():
        if e.type == QUIT:
            application = False

    p1.update_left()
    p2.update_right()

    window.fill(background)
    p1.draw()
    p2.draw()

    display.update()
    clock.tick(FPS)
