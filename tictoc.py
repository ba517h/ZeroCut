import sys
import pygame
from pygame.locals import *

FPS = 30
SCREENWIDTH = SCREENHEIGHT = 512

#The game matrix initialized with None, False for O and True for X, Posession_Matrix stores which all submatrices is possessed by O and X
Game_Matrix = [[None for x in range(9)] for y in range(9)]
Posession_MatrixO = [[None for x in range(3)] for y in range (3)]
Posession_MatrixX = [[None for x in range(3)] for y in range (3)]
Active_Matrix = [[True for x in range(3)] for y in range(3)]
IMAGES, SOUNDS = {},{}
player = True

#Function to convert pixel coordinates into game coordinates -- matrix indices
def get_index(value):
    index = [0,0,0,0]
    #row conversion
    if 0<=value[1]<=163:
        index[0] = 0
        if 0<=value[1]<=51:
            index[2] = 0
        elif 56<=value[1]<=107:
            index[2] = 1
        elif 112<=value[1]<=163:
            index[2] = 2
        else:
            return None
    elif 174<=value[1]<=337:
        index[0] = 1
        if 174<=value[1]<=225:
            index[2] = 0
        elif 230<=value[1]<=281:
            index[2] = 1
        elif 286<=value[1]<=337:
            index[2] = 2
        else:
            return None
    elif 348<=value[1]<=511:
        index[0] = 2
        if 348<=value[1]<=399:
            index[2] = 0
        elif 404<=value[1]<=455:
            index[2] = 1
        elif 460<=value[1]<=511:
            index[2] = 2
        else:
            return None
    else:
        return None

    #column conversion
    if 0<=value[0]<=163:
        index[1] = 0
        if 0 <= value[0] <= 51:
            index[3] = 0
        elif 56 <= value[0] <= 107:
            index[3] = 1
        elif 112 <= value[0] <= 163:
            index[3] = 2
        else:
            return None
    elif 174 <= value[0] <= 337:
        index[1] = 1
        if 174 <= value[0] <= 225:
            index[3] = 0
        elif 230 <= value[0] <= 281:
            index[3] = 1
        elif 286 <= value[0] <= 337:
            index[3] = 2
        else:
            return None
    elif 348 <= value[0] <= 511:
        index[1] = 2
        if 348 <= value[0] <= 399:
            index[3] = 0
        elif 404 <= value[0] <= 455:
            index[3] = 1
        elif 460 <= value[0] <= 511:
            index[3] = 2
        else:
            return None
    else:
        return None

    return index

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


#Function to display the winner
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
    global player
    coord = [None,None]
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
                print index
                if is_active(pos) == False or (is_active(pos) == True and Game_Matrix[index[0]*3+index[2]][index[1]*3+index[3]] is not None):
                    '''make sound that this click is not possible'''
                else :
                    #valid movement
                    Game_Matrix[index[0] * 3 + index[2]][index[1] * 3 + index[3]] = player
                    status = check([row[index[0]*3:index[0]*3+3] for row in Game_Matrix[index[1]*3:index[1]*3+1]]) #'O','X'
                    Active_Matrix = [[False for x in range(3)] for y in range(3)]
                    Active_Matrix[index[0]][index[1]] = True
                    if status['O'] == True and player == False:
                        Posession_MatrixO[index[0]][index[1]] = True
                        win_status = check(Posession_MatrixO)
                        if win_status['X'] == True:
                            won(False)
                            return
                        continue
                    if status['X'] == True and player == True:
                        Posession_MatrixX[index[0]][index[1]] = True
                        win_status = check(Posession_MatrixX)
                        if win_status['X'] == True:
                            won(True)
                            return
                        continue
                    #do all operations and change player
                    player = not player
        #drawing the screen
        SCREEN.blit(IMAGES['gamebg'],(0,0))
        for i in range(9):
           for j in range(9):
                if Game_Matrix[i][j] is not None:
                    if i == 0:
                        coord[0]=0
                    elif i == 1:
                        coord[0]=56
                    elif i == 2:
                        coord[0]=112
                    elif i == 3:
                        coord[0]=174
                    elif i == 4:
                        coord[0]=230
                    elif i == 5:
                        coord[0]=286
                    elif i == 6:
                        coord[0]=348
                    elif i == 7:
                        coord[0]=404
                    else:
                        coord[0]=460
                    
                    if j == 0:
                        coord[1]=0
                    elif j == 1:
                        coord[1]=56
                    elif j == 2:
                        coord[1]=112
                    elif j == 3:
                        coord[1]=174
                    elif j == 4:
                        coord[1]=230
                    elif j == 5:
                        coord[1]=286
                    elif j == 6:
                        coord[1]=348
                    elif j == 7:
                        coord[1]=404
                    else:
                        coord[1]=460
                if Game_Matrix[i][j] == True:
                    SCREEN.blit(IMAGES('X'),(coord[0],coord[1]))
                else:
                    SCREEN.blit(IMAGES('O'), (coord[0], coord[1]))
                    

        #setting the shadow for inactive matrices
        if all(Active_Matrix) == False:
            if(index[0] == 1 and index[1] == 1):
                SCREEN.blit(IMAGES['c_shad'],(0,0))
            elif index[0] == 1 or index[1] == 1:
                shad = 'm_shad'
                if index[0] == 1 and index[1] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad],270),(0,0))
                elif index[0] == 2 and index[1] == 1:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 180), (0, 0))
                elif index[0] == 1 and index[1] == 0:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 90), (0, 0))
                else:
                    SCREEN.blit(IMAGES[shad], (0, 0))
            else:
                shad = 's_shad'
                if index[0] == 0 and index[1] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 270), (0, 0))
                elif index[0] == 2 and index[1] == 2:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 180), (0, 0))
                elif index[0] == 2 and index[1] == 0:
                    SCREEN.blit(pygame.transform.rotate(IMAGES[shad], 90), (0, 0))
                else:
                    SCREEN.blit(IMAGES[shad], (0, 0))


        #SCREEN.blit(pygame.transform.rotate(IMAGES['shadow'],90),(0,0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def main():
    global SCREEN, FPSCLOCK,Game_Matrix,Posession_MatrixO,Posession_MatrixX,Active_Matrix
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))#,pygame.NOFRAME)
    pygame.display.set_caption('Tic Toc')

    IMAGES['gamebg'] = pygame.image.load('assets/images/game.png').convert()
    IMAGES['welcome'] = pygame.image.load('assets/images/bg.png').convert()
    IMAGES['shadow'] = pygame.image.load('assets/images/shadow.png').convert_alpha()
    IMAGES['O'] = pygame.image.load('assets/images/O.png').convert()
    IMAGES['X'] = pygame.image.load('assets/images/X.png').convert()

    #sounds
    if 'win' in sys.platform:
        soundExt = '.wav'
    else:
        soundExt = '.ogg'

    SOUNDS['win'] = pygame.mixer.Sound('assets/audio/win1'+soundExt)

    #Overall game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.exit()
                sys.exit()
            if event.type == MOUSEBUTTONUP:
                Game_Matrix = [[None for x in range(9)] for y in range(9)]
                Posession_MatrixO = [[None for x in range(3)] for y in range(3)]
                Posession_MatrixX = [[None for x in range(3)] for y in range(3)]
                Active_Matrix = [[True for x in range(3)] for y in range(3)]
                pos = pygame.mouse.get_pos()
                if  100 < pos[0] <250 and 100 < pos [1] < 250 :
                    playgame()

        SCREEN.blit(IMAGES['welcome'], (0, 0))
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
        main()