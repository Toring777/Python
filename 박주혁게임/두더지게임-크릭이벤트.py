import pygame as p
import random as r
import time as t

p.init() #라이브러리 초기화
white = (0,0,0) #희색같은 검정
size = (800,400) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True
do = p.image.load("D.png")
do_list = [ ] #변수 여러가지 작성
for x in range(5): #()개만금 반복
    do_rect = do.get_rect(left = r.randint(0,700),top = r.randint(0,300))
    do_list.append(do_rect)
#점수
font = p.font.SysFont("malgungothic",20)
font2 = p.font.SysFont("malgungothic",150)
score = 0
#시간
t1 = int(t.time()) #멈춘시간
#배경음
p.mixer.music.load("go.mp3")

  
playing = True

while playing:
    t2 = int(t.time())#진행중 시간
    timer = 30 - (t2 -t1)
    

    for event in p.event.get(): #사용자가 무엇을 누를는지 감지
        if event.type == p.QUIT:#닷기를 누루면
            playing = False
            p.quit()
            quit()
        if event.type == p.MOUSEBUTTONDOWN: #클릭
            for do_rect in do_list:
                if do_rect.collidepoint(event.pos[0],event.pos[1]):
                    do_list.remove(do_rect)
                    score += 1
                    do_rect = do.get_rect(left = r.randint(0,700),top = r.randint(0,300))
                    do_list.append(do_rect)
                       

    sc.fill(white) #배경색
    for do_rect in do_list:
        sc.blit(do,do_rect)
    text = font.render("디그다를 학살한 양:{}".format(score),True,(141,232,123))
    sc.blit(text,(0,0))
    text2 = font.render("시간:{}".format(timer),True,(141,232,123))
    sc.blit(text2,(300,0))
    if timer == 0:
        playing = False
        text3 = font2.render("Game Over",True,(141,232,123))
        sc.blit(text3,(0,0))
        p.mixer.music.play(1)
        for event in p.event.get(): #사용자가 무엇을 누를는지 감지
            if event.type == p.QUIT:#닷기를 누루면
                playing = False
                p.quit()
                quit()
    p.display.flip() #화면 업데이트
    
