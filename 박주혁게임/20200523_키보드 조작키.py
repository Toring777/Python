import pygame as p

p.init( ) #라이브러리 초기화

size = (400,400)

sc = p.display.set_mode(size)
w = (255,255,255)
b = (0,0,0)
p.display.set_caption("키보드 조작")

playing = True

x= 100
y= 100
while playing:

     for event in p.event.get( ):
         if event.type == p.QUIT:
             playing = False
             p.quit()
             quit
         if event.type == p.KEYDOWN:
             if event.key == p.K_UP:
                print("위")
                y = y - 5
             if event.key == p.K_DOWN:
                print("아래")
                y = y + 5
             if event.key == p.K_RIGHT:
                print("1엽")
                x = x + 5
             if event.key == p.K_LEFT:
                print("2엽")
                x = x - 5
         if event.type == p.KEYUP:
             if event.key == p.K_UP:
                print("위0")
             if event.key == p.K_DOWN:
                print("아래0")
             if event.key == p.K_RIGHT:
                print("1엽0")
             if event.key == p.K_LEFT:
                print("2엽0")

     sc.fill(w) #바탕화면 w색으로
     p.draw.circle(sc,b,(x,y),40) #(x,y),반지름,선두게
     p.display.flip() #화면 업대이트
     
             


