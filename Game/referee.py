import cython
import copy

from .constants import const

cs = const()
DIRECTIONS = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1,-1]]

class environment:
    def __init__(self):
        self.board = [0 for i in range(cs.WIDTH * cs.HEIGHT)]
    
    def Line(self, x, y, id):
        line = -1
        LINEMARK = []
        for d in DIRECTIONS:
            thisLine = 1
            thismark = [[x, y]]
            a = x + d[0]
            b = y + d[1]
            while a < cs.WIDTH and a > -1 and b < cs.HEIGHT and b > -1 and self.board[(b * cs.WIDTH) + a] == id:
                thisLine += 1
                thismark.append([a, b])
                a += d[0]
                b += d[1]
            if thisLine > line:
                line = thisLine
                LINEMARK = copy.deepcopy(thismark)
        return LINEMARK

    def lineLenght(self, x, y, id):
        line = -1
        for d in DIRECTIONS:
            thisLine = 1
            a = x + d[0]
            b = y + d[1]
            while a < cs.WIDTH and a > -1 and b < cs.HEIGHT and b > -1 and self.board[(b * cs.WIDTH) + a] == id:
                thisLine += 1
                a += d[0]
                b += d[1]
            if thisLine > line:
                line = thisLine
        return line

    def winner(self, id):
        for x in range(cs.WIDTH):
            for y in range(cs.HEIGHT):
                if self.board[(y * cs.WIDTH) + x] == id:
                    if self.lineLenght(x, y, id) >= cs.TIMES:return self.Line(x, y, id)
        return []

    def valids(self):
        return [i for i in range(cs.WIDTH) if self.board[i] == 0]

    def play(self, m, id):
        for y in range(cs.HEIGHT):
            if self.board[(y * cs.WIDTH)+m] != 0:
                self.board[((y - 1) * cs.WIDTH) + m] = id
                return y - 1
            if y == cs.HEIGHT - 1:
                self.board[(y * cs.WIDTH) + m] = id
                return y
