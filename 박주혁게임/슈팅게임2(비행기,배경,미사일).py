import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #희색 
size = (600,900) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")

playing = True

s_image = p.image.load("pl.png") # 비행기
s_rect = s_image.get_rect(left=260,top=800)
x = 0
y = 0
bg1 = p.image.load("bg1.png")
b = p.image.load("g.png")
b_list = []










while playing:

    for event in p.event.get(): #사용자가 무엇을 누를는지 감지
        if event.type == p.QUIT:#닷기를 누루면
            playing = False
            p.quit()
            quit()

        if event.type == p.KEYDOWN:
             if event.key == p.K_UP:
                 y = -3
             if event.key == p.K_DOWN:
                 y = 3
             if event.key == p.K_RIGHT:
                 x = 3    
             if event.key == p.K_LEFT:
                 x = -3
             if event.key == p.K_SPACE:
                 b_rect = b.get_rect(left=s_rect.left,top=s_rect.top)
                 b_list.append(b_rect)

             
        if event.type == p.KEYUP:
             if event.key == p.K_UP:
                 y = 0
             if event.key == p.K_DOWN:
                 y = 0
             if event.key == p.K_RIGHT:
                 x = 0    
             if event.key == p.K_LEFT:
                 x = 0
    s_rect.left += x 
    s_rect.top += y
            

            
    sc.fill(white) #배경색
    sc.blit(bg1,(0,0))
    sc.blit(s_image,s_rect)

    if s_rect.left <= 0:
        s_rect.left = 0
    if s_rect.left >= 520:
        s_rect.left = 520

    for b_rect in b_list:
        sc.blit(b,b_rect)
        b_rect.top -= 50
        if b_rect.top <= 0:
            b_list.remove(b_rect)








    
    p.display.flip() #화면 업데이트
    
