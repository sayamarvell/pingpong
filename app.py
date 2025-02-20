from pygame import *


class GameSprite(sprite.Sprite):
   def __init__(self, player_image ,player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image),(width, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y




   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))




class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed


back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))




player1 = Player('racket.png',30,200,4,50,150)
player2 = Player('racket.png',500,200,4,50,150)
ball = GameSprite('Ball.png',200,200,4,50,50)




game = True
finish = False
clock = time.Clock()
FPS = 60

speed_y = 3
speed_x = 3

while game:
   window.fill(back)
   for e in event.get():
       if e.type == QUIT:
           game = False
   player1.reset()
   player1.update_l()
   player2.reset()
   player2.update_r()

   ball.rect.x += speed_x
   ball.rect.y += speed_y

   if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
       speed_x *= -1
       speed_y *= 1

   if ball.rect.y > win_height-50 or ball.rect.y < 0:
       speed_y *= -1    

   ball.reset()
     
   display.update()
   clock.tick(FPS)





