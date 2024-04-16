import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    tori = pg.image.load("fig/3.png")
    tori_img = pg.transform.flip(tori, True, False)
    tori_rct = tori.get_rect()
    tori_rct.center = 300,200
    tmr = 0
    a=0
    b=0
    mode=0
    while True:
        for event in pg.event.get():
            key_lst = pg.key.get_pressed()
        if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if mode ==0:
            d=[a-1,0]
            if key_lst[pg.K_UP]:
                d=[a-1, b-1]
            if key_lst[pg.K_DOWN]:
                d=[a-1, b+1]            
            if key_lst[pg.K_LEFT]:
                d=[a-1, 0]            
            if key_lst[pg.K_RIGHT]:
                d=[a+2, 0]
            tori_rct.move_ip(d)
        
        x = tmr % 3200
        
        screen.blit(bg_img,[-x,0])
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(bg_img2,[-x+4800,0])        
        screen.blit(tori_img, tori_rct)
        
        
        screen.blit(tori_img,tori_rct)
        pg.display.update()
        tmr += 1
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()