import sys
import pygame
from pygame.locals import *

SCREENWIDTH = SCREENHEIGHT = 512

#The game matrix initialized with None, False for O and True for X, Posession_Matrix stores which all submatrices is possessed by O and X
Game_Matrix = [[None for x in range(9)] for y in range(9)]
Posession_MatrixO = [None for x in range(3) for y in range (3)]
Posession_MatrixX = [None for x in range(3) for y in range (3)]
Active_Matrix = [[True for x in range(3)] for y in range(3)]

IMAGES = {}

def get_index(value):
    '''Return index [][] for the corresponding mouse click'''

def is_active(value):
    '''returns if the current matrix is clickable'''
    return Active_Matrix[value[0]][value[1]]

def playgame():
    '''Test'''
    print 'inside play'
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.exit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                index = get_index(pos)
                if is_active(index) == False:
                    '''make sound that this click is not possible'''
                else :
                    '''valid movement'''




def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('Tic Toc')

    IMAGES['background'] = pygame.image.load('assets/images/bg.png').convert()


    #Overall game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.exit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if  200 < pos[0] <250 and 200 < pos [1] < 250 :
                    playgame()

        SCREEN.blit(IMAGES['background'], (0, 0))
        pygame.display.update()

if __name__ == '__main__':
        main()