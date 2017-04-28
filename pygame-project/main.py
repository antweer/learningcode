#!/usr/bin/env python3

import pygame
from random import randint
from math import sqrt, fabs
from characters import *
    
def main():
    #Game initialization
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
    level = 0
    hero = Hero()
    goblins = {1:Goblin(), 2:Goblin(), 3:Goblin()}
    enemies = {1:Monster(), 2:goblins[1], 3:goblins[2], 4:goblins[3]}
    framecount = 0
    stop_game = False
    playing = True
    winorloss = ""

    while not stop_game:
        leveltext = font.render("Level {}".format(level), True, black_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_game = True
        if level > 0:      
            for x in range(0, level+1):
                goblins[x+3] = Goblin()
                enemies[x+4] = Goblin()
        else:
            for x in range(3, len(goblins)):
                del goblins[x] 
                del enemies[x+1]
        while playing:
            song.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
            screen.blit(background, (0, 0))
            screen.blit(leveltext, (20,20))
            hero.move(screen,framecount)
            for x in enemies:
                if sqrt((hero.ycoord-enemies[x].ycoord)**2 + (hero.xcoord-enemies[x].xcoord)**2) <= 32:
                    winorloss = enemies[x]
                    song.stop()
                    playing = False
                else:
                    enemies[x].movemonster(screen, framecount)  
            pygame.display.update()
            clock.tick(60)
            framecount += 1  

        screen.blit(background, (0, 0))
        hero.stay(screen)   

        if winorloss == enemies[1]:
            winsound.play()
            screen.blit(wintext, (75, 230))
        else:
            losesound.play()
            screen.blit(losetext, (30, 230))
            level = 0
        
        pygame.display.update()

        if winorloss == enemies[1] and pygame.key.get_pressed()[pygame.K_RETURN]:
            level += 1

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            playing = True
            for x in enemies:
                enemies[x].xcoord = randint(20,490)
                enemies[x].ycoord = randint(20,460)

    pygame.quit()

if __name__ == '__main__':
    main()