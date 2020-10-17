import pygame as p

p.init() #라이브러리 초기화
white = (255,255,255) #희색 
size = (800,400) #(가로,세로)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True

sc.fill(white) #배경색
p.display.flip() #화면 업데이트
