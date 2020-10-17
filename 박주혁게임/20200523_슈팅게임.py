import pygame as p
import random as l

p.init( ) #라이브러리 초기화

size = (800,400)

sc = p.display.set_mode(size)
w = (255,255,255)
b = (0,0,0) 
z = p.image.load("z.png")
c = p.image.load("c.png")
c_1 = c.copy()
r = p.image.load("u.png")
  

p.mixer.music.load("ms.mp3")
p.mixer.music.play(0)

p.display.set_caption("키보드 조작")

playing = True

x= 10
y= 0
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
     y_c += y

     sc.fill(w) #바탕화면 w색으로
     sc.blit(c,(bg_x,0))
     sc.blit(c_1,(bg_x2,0))
     bg_x-= 2
     bg_x2-=2
     if bg_x <= -800:
          bg_x = 800
     if bg_x2 <= -800:
          bg_x2 = 800
     if y_c >=300:
          y = 0
     if y_c <= 0:
          y=0
     sc.blit(r,(z1_x1,z1_y1))
     z1_x1 -= 3
     if z1_x1 <= 0:
          z1_x1 = 800
          z1_y1 = l.randint(0,300)


    
     p.display.flip() #화면 업대이트
     
             


