import pygame
import config as cf
from pygame import gfxdraw

def drawGridLines(window):
    for i in range(1, 9):
        for j in range(1, 10):
            pygame.draw.line(window, (88, 120, 152, 5),
                             [i * cf.CELLSIZE, (j * cf.CELLSIZE) - 60],
                             [i * cf.CELLSIZE, (j * cf.CELLSIZE) - 10], 1)
            pygame.draw.line(window, (88, 120, 152, 5),
                             [j * cf.CELLSIZE - 60, i * cf.CELLSIZE],
                             [j * cf.CELLSIZE - 10, i * cf.CELLSIZE], 1)

    for i in range(3, 9, 3):
        pygame.draw.line(window, (cf.GRIDCOLOUR),
                         [i * cf.CELLSIZE, 0],
                         [i * cf.CELLSIZE, cf.HEIGHT], 2)
        pygame.draw.line(window, (cf.GRIDCOLOUR),
                         [0,     i * cf.CELLSIZE],
                         [cf.WIDTH, i * cf.CELLSIZE], 2)

def drawSelected(window):
    x = cf.selected[0] * cf.CELLSIZE + 35
    y = cf.selected[1] * cf.CELLSIZE + 35
    pygame.gfxdraw.filled_circle(window, x, y, 25, (3, 148, 177))
    pygame.gfxdraw.aacircle(window, x, y, 25, (3, 148, 177))

def drawNum(window, font):
    for col in range(9):
        for row in range(9):
            if cf.board.getNum(col, row) != 0:
                x = col * cf.CELLSIZE + 35
                y = row * cf.CELLSIZE + 35

                screenText = font.render(str(cf.board.getNum(col, row)),
                                         True, (159, 189, 212))
                if list(cf.board.grid[col][row].values())[0]:
                    pygame.gfxdraw.filled_circle(window, x, y, 25, (2, 83, 100))
                    pygame.gfxdraw.aacircle(window, x, y, 25, (2, 83, 100))
                else:
                    pygame.gfxdraw.filled_circle(window, x, y, 25, (22, 42, 48))
                    pygame.gfxdraw.aacircle(window, x, y, 25, (22, 42, 48))
                window.blit(screenText, (x-10, y-15))

def highlightCell(window):
    x = cf.selected[0] * cf.CELLSIZE
    y = cf.selected[1] * cf.CELLSIZE
    rect = pygame.Rect(x, y, cf.CELLSIZE+1, cf.CELLSIZE+1)
    pygame.gfxdraw.rectangle(window, rect, (10, 245, 10))
