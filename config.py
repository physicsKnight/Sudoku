import pygame
from board import *

board = Board()
running = True
solving = False
mousePos = None
selected = None
CELLSIZE = 70
WIDTH = 9 * CELLSIZE
HEIGHT = 9 * CELLSIZE
BG = (5, 15, 25)
GRIDCOLOUR = (0, 191, 255)
FPS = 60
CELLSOLVED = pygame.event.Event(pygame.USEREVENT, attr1='Event1')
NUMKEYCODES = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]
