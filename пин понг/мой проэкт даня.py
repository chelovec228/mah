from pygame import *
from random import randint
window = display.set_mode((700, 500))
display.set_caption('среншин инфаркт')
background = transform.scale(image.load('fon.jpg'), (700, 500))

clock = time.Clock()
FPS = 60 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > -450:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < 150:
            self.rect.x += self.speed
    
class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > -450:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 150:
            self.rect.x += self.speed  




class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= 600:
            self.rect.y = 150
            

palka = Player('palka1.png', -50, 450, 1000, 50, 7)
palka2 = Player1('palka2.png', 10, 1, 1000, 50, 7)

myc = Enemy('mach.png', 250, 150, 100, 100, 5)


game = True
while game:
    


    window.blit(background,(0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False

        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()

    



    palka.reset()
    palka.update()

    palka2.reset()
    palka2.update()

    myc.reset()
    myc.update()

    

 

   

    clock.tick(FPS)
    display.update()