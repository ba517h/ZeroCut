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
    index = [0,0,0,0]
    #row conversion
    if 0<=value[0]<=163:
        index[0] = 0
        if 0<=value[0]<=51:
            index[2] = 0
        elif 56<=value[0]<=107:
            index[2] = 1
        elif 112<=value[0]<=163:
            index[2] = 2
        else:
            return None
    elif 174<=value[0]<=337:
        index[0] = 1
        if 174<=value[0]<=225:
            index[2] = 0
        elif 230<=value[0]<=281:
            index[2] = 1
        elif 286<=value[0]<=337:
            index[2] = 2
        else:
            return None
    elif 348<=value[0]<=511:
        index[0] = 2
        if 348<=value[0]<=399:
            index[2] = 0
        elif 404<=value[0]<=455:
            index[2] = 0
        elif 460<=value[0]<=511:
            index[2] = 0
        else:
            return None
    else:
        return None

    #column conversion
    if 0<=value[1]<=163:
        index[1] = 0
        if 0 <= value[1] <= 51:
            index[3] = 0
        elif 56 <= value[1] <= 107:
            index[3] = 1
        elif 112 <= value[1] <= 163:
            index[3] = 2
        else:
            return None
    elif 174 <= value[1] <= 337:
        index[1] = 1
        if 174 <= value[1] <= 225:
            index[3] = 0
        elif 230 <= value[1] <= 281:
            index[3] = 1
        elif 286 <= value[1] <= 337:
            index[3] = 2
        else:
            return None
    elif 348 <= value[1] <= 511:
        index[1] = 2
        if 348 <= value[1] <= 399:
            index[3] = 0
        elif 404 <= value[1] <= 455:
            index[3] = 0
        elif 460 <= value[1] <= 511:
            index[3] = 0
        else:
            return None
    else:
        return None

#Function to check whether the given matrix is clickable
def is_active(value):
    index = get_index(value)
    if index is None:
        return False
    if (Active_Matrix[index[0]][index[1]] == False):
        return False
    if (164<=value[0]<=173) or (338<=value[0]<=347) or (52<=value[0]<=55) or (108<=value[0]<=111) or (226<=value[0]<=229) or (282<=value[0]<=285) or (400<=value[0]<=403) or (456<=value[0]<=459):
        return False
    if (164<=value[1]<=173) or (338<=value[1]<=347) or (52<=value[1]<=55) or (108<=value[1]<=111) or (226<=value[1]<=229) or (282<=value[1]<=285) or (400<=value[1]<=403) or (456<=value[1]<=459):
        return False
    return True

#Function to check whether a 3x3 matrix has got 3 in a row
def check(matrix):
    ret = {'O':False,'X':False}
    i=j=f1=f2=0
    for i in range(3):
        if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]:
            if matrix[i][j] == False:
                f1 = 1
            else:
                f2 = 1
        break

    for j in range(3):
        if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]:
            if matrix[i][j] is False:
                f1 = 1
            else:
                f2 = 1
        break

    if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2]:
        if matrix[i][j] is False:
            f1 = 1
        else:
            f2 = 1

    j=2
    if matrix[i][j] == matrix[i+1][j-1] == matrix[i+2][j-2]:
        if matrix[i][j] is False:
            f1 = 1
        else:
            f2 = 1

    if f1 == 1:
        ret['O']=True
    if f2 == 1:
        ret['X']=True
    return ret


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
    global Active_Matrix

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
                if is_active(pos) == False or (is_active(pos) == True and Game_Matrix[index[0]*3+index[2]][index[1]*3+index[3]] is not None):
                    '''make sound that this click is not possible'''
                else :
                    '''valid movement'''
                    Game_Matrix[index[0] * 3 + index[2]][index[1] * 3 + index[3]] = player
                    status = check([row[index[0]*3:index[0]*3+3] for row in Game_Matrix[index[1]*3:index[1]*3+1]]) #'O','X'
                    Active_Matrix = [[False for x in range(3)] for y in range(3)]
                    Active_Matrix[index[0]][index[1]] = True
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
    #IMAGES['X'] = pygame.image.load('assets/images/x.png').convert()
    #IMAGES['O'] = pygame.image.load('assets/images/o.png').convert()

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