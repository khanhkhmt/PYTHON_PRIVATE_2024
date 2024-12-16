import pygame
from pygame import Vector2


class Platform:
    def __init__(__self__,Point,width,high,color):
        __self__.LTPoint=Point.x
        __self__.LBPoint=Point.y
        __self__.width=width
        __self__.high=high
        __self__.color=color

a1=Platform(pygame.Vector2(100,600),30,100,"red")
a2=Platform(pygame.Vector2(300,600),40,100,"red")
a3=Platform(pygame.Vector2(200,400),20,100,"red")
a4=Platform(pygame.Vector2(10,500),80,1000,"red")
a5=Platform(pygame.Vector2(1450,600),60,100,"red")
a6=Platform(pygame.Vector2(1770,600),40,100,"red")
a7=Platform(pygame.Vector2(1800,600),90,100,"red")
a8=Platform(pygame.Vector2(500,600),10,100,"red")
a9=Platform(pygame.Vector2(700,600),40,100,"red")
a10=Platform(pygame.Vector2(900,600),30,100,"red")
a11=Platform(pygame.Vector2(200,600),20,100,"red")