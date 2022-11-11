import pygame
import sys
import time
import random

pygame.init()
#This puts a title on the screen 
pygame.display.set_caption('Pinball blast')

#this loads the sprites image
pinolaimg = pygame.image.load('Pinola looking left.png')
#this reduces the size of the image by x0.2
pinolaimg=pygame.transform.scale(pinolaimg,(167,162))
#This create the main playing screen and set the backround to grey
screen = pygame.display.set_mode((800,800))

#This is the class for pinola sprite
class pinola():
        # defining attributes for class
        def __init__ (self, x, y, image, scale, active):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.vel = 2
            #getting the cooridnates of the image
            self.rect = pinolaimg.get_rect()
            #setting the coordinates to the top left of the image
            self.rect.topleft = [x,y]
            self.rect.x = 2
        def draw(self):
                screen.blit(pinolaimg,(100,647))
                self.vel += 2
                
            
pinola_group = [5]

pino1 = pinola(100,638,10,1,True)

pinola_group[0] = pino1

#game loop
#speed at which it is moving 
vel=2
run = True
while True:
        #This makes the backround grey
        screen.fill((211,211,211))
        #this puts the sprite in the game 
        pinola_group[0].draw()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        run = False
                #regestring a key being pressed
                if event.type == pygame.KEYDOWN:
                        # if the a key is pressed
                        if event.key == pygame.K_a:
                                print(self.rect.x)
                                
