#!/usr/bin/env python3

import pygame
from random import randint
from math import sqrt, fabs
from characters import *

class Character():
    def __init__(self, xcoord, ycoord):
        self.xcoord = xcoord
        self.ycoord = ycoord
    def movenorth(self, screen):
        if self.ycoord > 20:
            self.ycoord -=15
        else:
            self.ycoord = 450
        screen.blit(self.image, (self.xcoord,self.ycoord))
    def movesouth(self, screen):
        if self.ycoord < 460:
            self.ycoord +=15
        else:
            self.ycoord = 15
        screen.blit(self.image, (self.xcoord,self.ycoord))
    def moveeast(self, screen):
        if self.xcoord <500:
            self.xcoord +=15
        else:
            self.xcoord = 15
        screen.blit(self.image, (self.xcoord,self.ycoord))
    def movewest(self, screen):
        if self.xcoord > 20:
            self.xcoord -=15
        else:
            self.xcoord = 490
        screen.blit(self.image, (self.xcoord,self.ycoord))
    def movenorthwest(self, screen):
        self.movenorth(screen)
        self.movewest(screen)
    def movesouthwest(self, screen):
        self.movesouth(screen)
        self.movewest(screen)
    def movenortheast(self, screen):
        self.movenorth(screen)
        self.moveeast(screen)
    def movesoutheast(self, screen):
        self.movesouth(screen)
        self.moveeast(screen)
    def stay(self, screen):
        screen.blit(self.image, (self.xcoord,self.ycoord))

class Hero(Character):
    def __init__(self, xcoord = 243, ycoord = 228):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.image = pygame.image.load("images/hero.png")
        self.limiter = 5
    def move(self, screen, framecount):
        if framecount%self.limiter == 0:
            if self.ycoord > 15 and pygame.key.get_pressed()[pygame.K_UP]:
                self.movenorth(screen)
            elif self.ycoord < 450 and pygame.key.get_pressed()[pygame.K_DOWN]:
                self.movesouth(screen)
            elif self.xcoord > 15 and pygame.key.get_pressed()[pygame.K_LEFT]:
                self.movewest(screen)
            elif self.xcoord < 490 and pygame.key.get_pressed()[pygame.K_RIGHT]:
                self.moveeast(screen)  
            else:
                self.stay(screen) 
        else:
            self.stay(screen)

class Enemy(Character):
     def __init__(self, xcoord = randint(20,480) , ycoord = randint(20,460)):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.limiter = 60
     def movemonster(self, screen, framecount):
        moves = [self.movenorth, 
                self.movesouth, 
                self.moveeast, 
                self.movewest, 
                self.movenortheast, 
                self.movenorthwest,
                self.movesouthwest,
                self.movesoutheast
                ]
        randomdir = randint(0,7)
        if framecount%self.limiter == 0:
            return moves[randomdir](screen)
        else:
            return self.stay(screen)    

class Monster(Enemy):
    def __init__(self, xcoord = randint(20,480) , ycoord = randint(20,460)):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.image = pygame.image.load("images/monster.png")
        self.limiter = 15

class Goblin(Enemy):
    def __init__(self, xcoord = randint(20,480) , ycoord = randint(20,460)):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.image = pygame.image.load("images/goblin.png")
        self.limiter = 20