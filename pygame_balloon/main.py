import pygame
import os
pygame.font.init()

width,height =900,500
white_color=(255,255,255)
fps= 60
winner_font=pygame.font.SysFont("comicsans",30)
balloon_image=pygame.image.load('balloon.png')
balloon_resize=pygame.transform.scale(balloon_image,(40,45))
shooter_image=pygame.image.load('shooter.png')
shooter_resize=pygame.transform.scale(shooter_image,(40,45))
text="Bullet collided with balloon"
text1="Missed shots: "
bullet_image=pygame.image.load('bullet.png')
bullet_resize=pygame.transform.scale(bullet_image,(25,20))

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("Balloon shooting game")

def draw_window(balloon_1,bullet_1):
    win.fill(white_color)
    score_text=winner_font.render(text1,1,(255,0,0))
    win.blit(score_text, (550,50))
    win.blit(balloon_resize,(balloon_1.x,balloon_1.y))
    win.blit(shooter_resize,(750,350))
    win.blit(bullet_resize,(bullet_1.x,bullet_1.y))
    pygame.display.update()

def draw_winner(text,temp):
    draw_text=winner_font.render(text,1,(255,0,0))
    win.blit(draw_text, (350,250))
    temp1=str(temp)
    draw_text1=winner_font.render(temp1,1,(255,0,0))
    win.blit(draw_text1, (790,50))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()

def main():
    balloon_1=pygame.Rect(150,50,40,45)
    bullet_1= pygame.Rect(745,350,25,20)
    temp=0
    z=0
    k=0
    za=0
    k1=0
    clock_fps=pygame.time.Clock()
    run= True
    while run:
        clock_fps.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        if k==0:
           balloon_1.y+=1
        if balloon_1.y==400:
            k=1
        if k==1:
            balloon_1.y-=1
            if balloon_1.y==50:
                k=0
        keys_pressed= pygame.key.get_pressed()
        if keys_pressed[pygame.K_SPACE]: #it releases the bullets.
            k1=1
            z=10
        bullet_1.x-=z
        if balloon_1.colliderect(bullet_1):
            collision="Collided with balloon"
            draw_winner(text,za) 
        if bullet_1.x<=2 and k1==1:
            bullet_1= pygame.Rect(745,350,25,20)
            za+=1
            keys_pressed1= pygame.key.get_pressed()
            if keys_pressed1[pygame.K_SPACE]: #it releases the bullets.
                z=10
            bullet_1.x-=z
        draw_window(balloon_1,bullet_1)
    pygame.quit()
if __name__== "__main__" :
     main()

