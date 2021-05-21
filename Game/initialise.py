import pygame

from .constants import const

cs = const()
BG = pygame.image.load(cs.resource_dir + '\\bg.jpg')
P1 = pygame.image.load(cs.resource_dir + '\\P1.jpg')
P2 = pygame.image.load(cs.resource_dir + '\\P2.jpg')
AI = pygame.image.load(cs.resource_dir + '\\AI.jpg')
UNIT = pygame.image.load(cs.resource_dir + '\\unit.png')
C1 = pygame.image.load(cs.resource_dir + '\\chip1.png')
C2 = pygame.image.load(cs.resource_dir + '\\chip2.png')

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', cs.FONT_SIZE)

def form_board(window):
    x = 100
    y = 50
    for X in range(cs.WIDTH):
        for Y in range(cs.HEIGHT):
            window.blit(UNIT, (x, y))
            y += 100
        x += 100
        y = 50

def initialise(window, name = ["Player1", "Player2"]):
    P1_n = myfont.render(name[0], False, (0, 0, 0))
    P2_n = myfont.render(name[1], False, (0, 0, 0))
    log = pygame.font.SysFont('Comic Sans MS', 50)
    LOGO = log.render("Connect4", False, (255, 0, 0))
    text_rect_p1 = P1_n.get_rect(center = (50, 215))
    text_rect_p2 = P2_n.get_rect(center = (cs.WIDTH_DISPLAY - 50, 215))
    text_rect_logo = LOGO.get_rect(center = (cs.WIDTH_DISPLAY // 2, 20))
    window.blit(BG, (0, 0))
    window.blit(P1 if name[0] != "AI" else AI, (25, 150))
    window.blit(P2 if name[1] != "AI" else AI, (cs.WIDTH_DISPLAY - 75, 150))
    window.blit(P1_n, text_rect_p1)
    window.blit(P2_n, text_rect_p2)
    window.blit(LOGO, text_rect_logo)
    window.blit(C1, (0, 230))
    window.blit(C2, (cs.WIDTH_DISPLAY - 100, 230))
    pygame.draw.circle(window, (0, 255, 0), (50, 400), 25)
    pygame.draw.circle(window, (255, 0, 0), (cs.WIDTH_DISPLAY - 50, 400), 25)
    form_board(window)
