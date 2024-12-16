
import pygame
from Object import Platform

pygame.init()
screen = pygame.display.set_mode([1440,750],0,255)
w=screen.get_width()
h=screen.get_height()
running=True
clock=pygame.time.Clock()
dt=0
player=pygame.Vector2(w/2,h/2)
Object=pygame.Vector2(w+200,h/2)
view_point=0
PL=[[Platform.a1,Platform.a2,Platform.a3,Platform.a4,Platform.a8,Platform.a9,
    Platform.a10,Platform.a11],[Platform.a5,Platform.a7,Platform.a3]]
speed=200
while running:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.y -= speed*dt
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.y+=speed*dt
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if view_point>0 and player.x<=w/3+w/3:
            view_point-=speed*dt
            if view_point<0:
                view_point=0
        else:
            if player.x-20>0:
                player.x-=speed*dt
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if view_point<1000 and player.x>=w/3:
            view_point+=speed*dt
        else:
            if player.x+20<w:
                player.x+=speed*dt
    index=int(view_point//w)
    for i in PL[index]:
        pygame.draw.rect(screen,i.color,[i.LTPoint-(view_point/i.LTPoint)*i.LTPoint,i.LBPoint,i.width,i.high])
    if index<len(PL)-1:
            for i in PL[index+1]:
                pygame.draw.rect(screen, i.color,[i.LTPoint - view_point , i.LBPoint, i.width, i.high])
    if (((player.x-20<=Object.x-view_point+10<=player.x+20)  or (player.x-20<=Object.x-view_point-10<=player.x+20))
    and Object.y<=player.y+20
    and Object.y>=player.y-20):
        Object.x+=((Object.x-view_point-player.x)/(abs(Object.x-view_point-player.x)))*speed*dt
    pygame.draw.circle(screen,"red",Object - pygame.Vector2(view_point,0),10)
    pygame.draw.circle(screen,"blue",player,20)
    pygame.display.set_caption(f'FPS: {clock.get_fps()}')
    pygame.display.flip()
    dt=clock.tick(1000)/1000
pygame.quit()