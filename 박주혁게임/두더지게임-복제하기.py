import pygame as p
import random as r

p.init() #라이브러리 초기화
white = (255,255,255) #희색 
size = (800,400) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True
do = p.image.load("D.png")
do_list = [ ]
for x in range(9): #
    do_rect = do.get_rect(left = r.randint(0,700),top = r.randint(0,300))
    do_list.append(do_rect)


playing = True

while playing:

    for event in p.event.get(): #사용자가 무엇을 누를는지 감지
        if event.type == p.QUIT:#닷기를 누루면
            playing = False
            p.quit()
            quit()

            
    sc.fill(white) #배경색
    for do_rect in do_list:
        sc.blit(do,do_rect)
        
    p.display.flip() #화면 업데이트
    
