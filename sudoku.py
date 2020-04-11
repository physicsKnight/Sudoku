import pygame
import sys
import time

import config as cf
from rendering import *
from threading import Thread

def events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            cf.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cf.selected = [cf.mousePos[0] // cf.CELLSIZE, cf.mousePos[1] // cf.CELLSIZE]
        elif event.type == pygame.KEYDOWN:

            if cf.selected != None:
                global threads
                if event.key in cf.NUMKEYCODES:
                    cf.board.placeNum(cf.selected[0], cf.selected[1], event.key - 48)
                elif event.key == pygame.K_BACKSPACE:
                    cf.board.placeNum(cf.selected[0], cf.selected[1], 0)
                elif event.key == pygame.K_SPACE:
                    cf.board.solvingData = [0, False]
                    threadExecutor(cf.board.solve)
                elif event.key == pygame.K_RETURN:
                    if cf.board.checkBoard():
                        threadExecutor(createNewPuzzle)
                elif event.key == pygame.K_RIGHT:
                    threadExecutor(createNewPuzzle)
                elif event.key == pygame.K_ESCAPE:
                    cf.board.reset()

def update():
    cf.mousePos = pygame.mouse.get_pos()
    clock.tick(cf.FPS)

# handles graphics
def draw(window):
    window.fill(cf.BG)
    if cf.selected != None:
        drawSelected(window)
        highlightCell(window)
    drawNum(window, font)
    drawGridLines(window)
    pygame.display.update()

# handles multiple executions of threads
def threadExecutor(function):
    global threads
    if threads: threads.pop() # we only need to run one background thread at a time
    threads.append(Thread(target=function))
    threads[0].daemon = True # stops execution of thread when it is removed
    threads[0].start()

# keeps generating new puzzles until a solvable one is found
def createNewPuzzle():
    while not cf.board.generatePuzzle():
        continue


# game setup
pygame.init()
window = pygame.display.set_mode((cf.WIDTH, cf.HEIGHT))
pygame.display.set_caption("Sudoku Solver")
font = pygame.font.Font(None, 50)
cf.board.window = window
clock = pygame.time.Clock()
threads = []

# game loop
while cf.running:
    events()
    update()
    draw(window)
pygame.quit()
sys.exit()
