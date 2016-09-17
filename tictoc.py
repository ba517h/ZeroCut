import pygame

SCREENWIDTH = SCREENHEIGHT = 512

#check whether a matrix is owned by someone
def check(matrix):
    print "Test"


#The game matrix initialized with None, False for O and True for X, Posession_Matrix stores which all submatrices is possessed by O and X
Game_Matrix = [[None for x in range(9)] for y in range(9)]
Posession_MatrixO = [None for x in range(3) for y in range (3)]
Posession_MatrixX = [None for x in range(3) for y in range (3)]


def main():
    pygame.init()
    SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
    pygame.display.set_caption('Tic Toc')
    #main game loop
    while True:
           print 'hi'


if __name__ == '__main__':
        main()