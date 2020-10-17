import pygame as p
import random as l

p.init( ) #라이브러리 초기화

size = (800,400)

sc = p.display.set_mode(size)
w = (255,255,255)
b = (0,0,0)
z = p.image.load("z.png")
#이미지 ==>좌표화
z_rect = z.get_rect(left = 10 , top = 0) # left = x , top = y

c = p.image.load("c.png")
c_1 = c.copy()
r = p.image.load("u.png")
r_rect = r.get_rect(left = 700 , top = 200)
m = p.image.load("m.png")
font = p.font.SysFont('malgungothic',20)
font1 = p.font.SysFont('malgungothic',50)
socre = 0

p.mixer.music.load("ms.mp3")
p.mixer.music.play(0)


p.display.set_caption("키보드 조작")

playing = True

y = 0
y_c = 0
bg_x = 0
bg_x2 = 800
z1_x1 =700
z1_y1 =0
z2_x2 =700
z2_y2 =200
while playing:

     for event in p.event.get( ):
         if event.type == p.QUIT:
             playing = False
             p.quit()
             quit
         if event.type == p.KEYDOWN:
             if event.key == p.K_UP:
                y = -3
             if event.key == p.K_DOWN:
                y -=  -3
         if event.type == p.KEYUP:
             if event.key == p.K_UP or event.key == p.K_DOWN:
                 y = 0
     z_rect.top += y

     sc.fill(w) #바탕화면 w색으로
     sc.blit(c,(bg_x,0))
     sc.blit(c_1,(bg_x2,0))
     bg_x-= 2
     bg_x2-=2
     if bg_x <= -800:
          bg_x = 800
     if bg_x2 <= -800:
          bg_x2 = 800
     sc.blit(z,z_rect)
     if z_rect.top >=300:
          y = 0
     if z_rect.top <= 0:
          y=0
     sc.blit(r,r_rect)
     r_rect.left -= 3
     if r_rect.left <= 0:
          r_rect.left = 800
          r_rect.top = l.randint(0,300)
          socre = 1 + socre

     text = font.render('점수 : {}'.format(socre),True,(0,0,0))
     text1 = font1.render('Game Over',True,(255,0,0))
     sc.blit(text,(700,0))

     if z_rect.colliderect(r_rect):
         sc.blit(m,z_rect)
         p.mixer.music.load("ms.mp3")
         p.mixer.music.play(1)
         p.mixer.music.load("jon1.mp3")
         p.mixer.music.play(0)
         sc.blit(text1,(300,150))
         playing = False
         


     
     p.display.flip() #화면 업대이트
     
             


