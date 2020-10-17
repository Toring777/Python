import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #희색 
size = (600,900) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")


playing = True

while playing:

    for event in p.event.get(): #사용자가 무엇을 누를는지 감지
        if event.type == p.QUIT:#닷기를 누루면
            playing = False
            p.quit()
            quit()

            
    sc.fill(white) #배경색

    p.display.flip() #화면 업데이트
    
