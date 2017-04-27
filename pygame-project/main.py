#!/usr/bin/env python3

import pygame
from random import randint
from math import sqrt, fabs

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
        self.limiter = 30
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
        self.limiter = 30

class Goblin(Enemy):
    def __init__(self, xcoord = randint(20,480) , ycoord = randint(20,460)):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.image = pygame.image.load("images/goblin.png")
        self.limiter = 90
    
def main():
    width = 510
    height = 480
    black_color = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    background = pygame.image.load("images/background.png")
    screen.blit(background, (0, 0))
    winsound = pygame.mixer.Sound("sounds/win.wav")
    losesound = pygame.mixer.Sound("sounds/lose.wav")
    song = pygame.mixer.Sound("sounds/music.wav")
    font = pygame.font.Font(None, 40)
    wintext = font.render('Hit ENTER to play again!', True, black_color)
    losetext = font.render('You lose! Hit ENTER to play again', True, black_color)
    
    # Game initialization

    monster = Monster()
    hero = Hero()
    goblin1 = Goblin()
    goblin2 = Goblin()
    goblin3 = Goblin()
    enemies = {1:monster, 2:goblin1, 3:goblin2, 4:goblin3}
    goblins = {1:goblin1, 2:goblin2, 3:goblin3}
    framecount = 0
    stop_game = False
    playing = True
    winorloss = ""
    while not stop_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True

        while playing:
            song.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stop_game = True
            screen.blit(background, (0, 0))
            hero.move(screen,framecount)
            for x in enemies:
                if sqrt((hero.ycoord-enemies[x].ycoord)**2 + (hero.xcoord-enemies[x].xcoord)**2) <= 32:
                    winorloss = enemies[x]
                    playing = False
                else:
                    enemies[x].movemonster(screen, framecount)  
            pygame.display.update()
            clock.tick(60)
            framecount += 1  
        
        screen.blit(background, (0, 0))
        hero.stay(screen)   

        if winorloss == monster:
            winsound.play()
            screen.blit(wintext, (75, 230))
        else:
            losesound.play()
            screen.blit(losetext, (30, 230))
        
        pygame.display.update()

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            playing = True
            for x in enemies:
                enemies[x].xcoord = randint(20,490)
                enemies[x].ycoord = randint(20,460)

    pygame.quit()

if __name__ == '__main__':
    main()
"""                
            if sqrt((hero.ycoord-monster.ycoord)**2 + (hero.xcoord-monster.xcoord)**2) <= 32:
                winorloss = "win"
                playing = False
            elif sqrt((hero.ycoord-goblin.ycoord)**2 + (hero.xcoord-goblin.xcoord)**2) <= 32:
                winorloss = "loss"
                playing = False
"""