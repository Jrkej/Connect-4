# Complete game setup using the PyGame Lib.
import pygame
import os
import sys
import copy
import time
from pygame.locals import *

from .initialise import initialise as board
from .referee import environment as env
from .constants import const
from .AI import minimax as DEFAULT
from .SubProcesser import MASTER as master_AI

AI = [False, False]
cs = const()
pygame.init()
window = pygame.display.set_mode((cs.WIDTH_DISPLAY, cs.HEIGHT_DISPLAY))
TEXT = pygame.font.SysFont('Comic Sans MS', 100)
RTEXT = pygame.font.SysFont('Comic Sans MS', 90)

P1 = pygame.image.load(cs.resource_dir + '\\chip1.png')
P2 = pygame.image.load(cs.resource_dir + '\\chip2.png')
Mark = pygame.image.load(cs.resource_dir + '\\winMark.png')
CHIPS = [P1, P2]

MAX_DEPTH = 4
DEPTHS = {'beginner' : 2, 'very easy': 3, 'easy': 4, 'medium': 5, 'hard': 6, 'very hard': 7}
PLAYERS = ["Player1", "Player2"]

restart = False
close = False
MASTER = False

def set_difficulty(level = "easy"):
    global MAX_DEPTH
    global MASTER
    if level == 'master':
        MASTER = True
    else:
        MAX_DEPTH = DEPTHS[level]

def Initialise(name = ["Player1", "Player2"]):
    print(name)
    global window
    global PLAYERS
    global restart
    global close
    restart = False
    close = False
    PLAYERS = name
    board(window, name = name)
    pygame.display.update()
    if name[0] == "AI":
        AI[0] = True
    if name[1] == "AI":
        AI[1] = True

def end():
    global restart
    global close
    while not close:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
        key_input = pygame.key.get_pressed()
        if key_input[114] == 1:
            print("restarting")
            restart = True
            break
    if close:pygame.quit()

def match():
    turns = 0
    game = env()
    run = True
    global close
    MATCH_STATUS = "DRAW"
    while run:
        valids = game.valids()
        if len(valids) == 0:
            break
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                close = True
        keys = pygame.mouse.get_pressed()
        Id = (turns % 2) + 1
        move = -1
        if AI[turns % 2]:
            start = time.time()
            if MASTER:
                sboard = ""
                for i in game.board:sboard += str(i)
                move = master_AI(id = Id, board = sboard)
            else:
                move = DEFAULT(game.board, MAX_DEPTH, Id, 0, True)
            time.sleep(max(0, 3 - (time.time() - start)))
        x = mx - 100
        if keys[0] == 1 and mx < 800 and mx > 100 and my < 640 and my > 10 and 20 < x % 100 < 80 and AI[turns % 2] == False:
            move = x // 100
        if move in valids:
            y_ax = game.play(move, Id)
            window.blit(CHIPS[Id - 1], ((move * 100) + 100, (y_ax * 100) + 50))
            pygame.draw.circle(window, (0, 255, 0), (50 if turns % 2 == 1 else cs.WIDTH_DISPLAY - 50, 400), 25)
            pygame.draw.circle(window, (255, 0, 0), (50 if turns % 2 == 0 else cs.WIDTH_DISPLAY - 50, 400), 25)
            turns += 1
            line = game.winner(Id)
            if len(line) >= cs.TIMES:
                for block in line:
                    bx = block[0]
                    by = block[1]
                    window.blit(Mark, ((bx* 100) + 100, (by * 100) + 50))
                MATCH_STATUS = f"{PLAYERS[Id - 1]} WON!!!!!"
                break
        pygame.display.update()
        time.sleep(.1)
    
    if not close:
        pygame.draw.circle(window, (255, 0, 0), (50, 400), 25)
        pygame.draw.circle(window, (255, 0, 0), (cs.WIDTH_DISPLAY - 50, 400), 25)
        endScreen = TEXT.render(MATCH_STATUS, False, (0, 0, 255))
        place = endScreen.get_rect(center = (cs.WIDTH_DISPLAY // 2, cs.HEIGHT_DISPLAY // 2))
        window.blit(endScreen, place)
        Restart = RTEXT.render("Press 'r' to restart!", False, (255, 0, 0))
        rplace = Restart.get_rect(center = (cs.WIDTH_DISPLAY // 2, 100 + (cs.HEIGHT_DISPLAY // 2)))
        window.blit(Restart, rplace)
        pygame.display.update()
    
