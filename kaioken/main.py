#SOURCE FROM GITHUB KUB ผมไม่เคยทำ pygame T^T

from itertools import count
from tkinter import Y
import pygame

from pygame import mixer



mixer.init()

clock = pygame.time.Clock()

count = 0

screen = pygame.display.set_mode((780, 780))

# CLASS

class Key():
    def __init__(self,x,y,color1,color2,key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pygame.Rect(self.x,self.y,100,40)
        self.handled = False

# LIST OF KEY

keys = [
    Key(50,500,(255,0,0),(220,0,0),pygame.K_f),
    Key(200,500,(0,255,0),(0,220,0),pygame.K_g),
    Key(350,500,(0,0,255),(0,0,220),pygame.K_j),
    Key(500,500,(255,255,0),(220,220,0),pygame.K_k),
]

# MAP LOADING
def load(map):
    rects = []
    mixer.music.load(map + ".mp3")
    mixer.music.play()
    f = open(map + ".txt", 'r')
    data = f.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,50,25))
    return rects

map_rect = load("tudleaw")

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #LOOP THROUGH KEY : 
    k = pygame.key.get_pressed()
    for key in keys:
        if k[key.key]:
            pygame.draw.rect(screen,key.color1,key.rect)
            key.handled = False
        if not k[key.key]: 
            pygame.draw.rect(screen,key.color2,key.rect)
            key.handled = True
        #
    for rect in map_rect:
        pygame.draw.rect(screen,(200,0,0),rect)
        rect.y += 7
        for key in keys: 
            if key.rect.colliderect(rect) and not key.handled:
                map_rect.remove(rect)
                key.handled = True
                break
    pygame.display.update()
    clock.tick(60)