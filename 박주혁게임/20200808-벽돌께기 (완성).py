import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #희색 
size = (600,900) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판") #게임이름

pan = p.image.load("금속.png")
p_rect = pan.get_rect(left=250,top=800)
x = 0

bg = p.image.load("bg1.png")

b = p.image.load("Dss.png")
b_rect = b.get_rect(left = 270,top = 300)
#공속도
b_x=7
b_y=7
block = p.image.load("BL.png")
bl_list = []
for e in range(10):
    for q in range(5):
        bl_rect = block.get_rect(left = 60*e,top = 50*q)
        bl_list.append(bl_rect)
#점수        
score = 0
font = p.font.SysFont("malgungothic",20)
#클리어
font1 = p.font.SysFont("malgungothic",50)
playing = True

while playing:

    for event in p.event.get(): #사용자가 무엇을 누를는지 감지
        if event.type == p.QUIT:#닷기를 누루면
            playing = False
            p.quit()
            quit()
        if event.type == p.KEYDOWN:
            if event.key == p.K_LEFT:
                x = -5
            if event.key == p.K_RIGHT:
                x = 5
        if event.type == p.KEYUP:
            if event.key == p.K_LEFT:
                x = 0
            if event.key == p.K_RIGHT:
                x = 0
        

    p_rect.left += x
            
    sc.fill(white) #배경색

    sc.blit(bg,(0,0))
    sc.blit(pan,p_rect)
    if p_rect.left <= 0:
        p_rect.left = 0
    if p_rect.left >= 500:
        p_rect.left = 500

    
    sc.blit(b,b_rect)
    b_rect.top += b_y
    if b_rect.top >= 870:
         playing = False
    if b_rect.top <= 0:
         b_y = -b_y

    b_rect.left += b_x
    if b_rect.left >= 570:
         b_x = -b_x
    if b_rect.left <= 0:
         b_x = -b_x


    if p_rect.colliderect(b_rect):
        b_y = -8


    for bl_rect in bl_list:
        sc.blit(block,bl_rect)

    for bl_rect in bl_list:
        if b_rect.colliderect(bl_rect):
            bl_list.remove(bl_rect)
            b_y = +8
            score += 1

    text = font.render("점수:{}".format(score),True,(255,255,0))
    text1 = font1.render("클리어",True,(255,255,255))
    sc.blit(text,(500,850))
    

    if len(bl_list) <= 0:
        sc.blit(text1,(225,450))
        playing = False
        
            
            
            
    

    p.display.flip() #화면 업데이트
    
