import pygame as p

p.init( )

w = (255,255,255)
r = (255,0,0)

#이미지 삽입
i = p.image.load("e.png")
o = p.image.load("w.png")
h = p.image.load("q.png")

p.mixer.music.load("ms.mp3")
p.mixer.music.play(0)


size = (400,400)
sc = p.display.set_mode(size)
p.display.set_caption("zzz")

done = False

while not done:

    for event in p.event.get():
        if event.type == p.QUIT:
            done = True


    sc.fill(w)

    sc.blit(i,(10,10))
    sc.blit(h,(10,150))
    sc.blit(o,(15,290))
    
    p.display.flip()
