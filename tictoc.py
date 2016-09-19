import sys
import pygame
from pygame.locals import *

SCREENWIDTH = SCREENHEIGHT = 512

#The game matrix initialized with None, False for O and True for X, Posession_Matrix stores which all submatrices is possessed by O and X
Game_Matrix = [[None for x in range(9)] for y in range(9)]
Posession_MatrixO = [[None for x in range(3)] for y in range (3)]
Posession_MatrixX = [[None for x in range(3)] for y in range (3)]
Active_Matrix = [[True for x in range(3)] for y in range(3)]
IMAGES = {}
player = True

#Function to convert pixel coordinates into game coordinates -- matrix indices
def get_index(value):
    ''''''

#Function to check whether the given matrix is clickable
def is_active(value):
    return Active_Matrix[value[0]][value[1]]

#Function to check whether a 3x3 matrix has got 3 in a row
def check(matrix):
    '''Return {'O': ,'X': }'''

#Function to display the winning
def won(player):
    if player == True:
        SCREEN.blit(IMAGES['X'],(0,0))
    else:
        SCREEN.blit(IMAGES['O'],(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.exit()
            sys.exit()
        if event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
            return

def playgame():
    #game loop
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
                if is_active(index) == False or Game_Matrix[index[0]*3+index[2]][index[1]*3+index[3]] is not None:
                    '''make sound that this click is not possible'''
                else :
                    '''valid movement'''
                    Game_Matrix[index[0] * 3 + index[2]][index[1] * 3 + index[3]] = player
                    status = check([row[index[0]*3:index[0]*3+3] for row in Game_Matrix[index[1]*3:index[1]*3+1]]) #'O','X'
                    if status['O'] == True and player == False:
                        Posession_MatrixO[index[0]][index[1]] = True
                        win_status = check(Posession_MatrixO)
                        if win_status['X'] == True:
                            '''O won the game'''
                            won(False)
                            return
                        continue
                    if status['X'] == True and player == True:
                        Posession_MatrixX[index[0]][index[1]] = True
                        win_status = check(Posession_MatrixX)
                        if win_status['X'] == True:
                            '''X won the game'''
                            won(True)
                            return
                        continue
                    #do all operations and change player
                    player = not player



def main():
    global SCREEN, FPSCLOCK
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('Tic Toc')

    IMAGES['background'] = pygame.image.load('assets/images/bg.png').convert()
    IMAGES['X'] = pygame.image.load('assets/images/x.png').convert()
    IMAGES['O'] = pygame.image.load('assets/images/o.png').convert()

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