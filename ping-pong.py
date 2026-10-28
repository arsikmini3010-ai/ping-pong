from pygame import *
font.init()

win_size = (700,500)
label_color = (180,25,0)
FPS = 60
p_size = (30, 120)
b_size  = (50,50)
p_speed = 2
b_speed_x = 3
b_speed_y = 3

font = font.SysFont('Arial',35)
lp1 = font.render('p1 lose!',True,label_color)
lp2 = font.render('p2 lose!',True,label_color)

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
ball = GameSprite('ball.png',300,200,b_size)

clock = time.Clock()
finish = True
application = True
while application:
    for e in event.get():
        if e.type == QUIT:
            application = False

    if finish:
        
        window.fill(background)
        ball.rect.x += b_speed_x
        ball.rect.y += b_speed_y
        if ball.rect.bottom > win_size[1] or ball.rect.y < 0:
            b_speed_y *= -1
        if sprite.collide_rect(p1, ball) or sprite.collide_rect(p2, ball):
            b_speed_x *= -1
        if ball.rect.x <= 0:
            window.blit(lp1,(320,220))
            finish = False
        if ball.rect.right >= win_size[0]:
            window.blit(lp2,(300,200))
            finish = False

        p1.update_left()
        p2.update_right()

        ball.draw()
        p1.draw()
        p2.draw()

    display.update()
    clock.tick(FPS)