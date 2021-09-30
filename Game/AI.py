import copy
import time
import cython

# Game board, rules, moves and other functions setup.
WIDTH = 7
HEIGHT = 6
TIMES = 4
DIRECTIONS = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1,-1]]
WIN = 1000000
DRAW = 0
GAMMA = .99
WEIGHT_LENGHT = 2
WEIGHT_PLACE = 2
TT = {}

# Getting the length of line.
def lineLenght(board, x, y, id):
    line = -1
    for d in DIRECTIONS:
        thisLine = 1
        a = x + d[0]
        b = y + d[1]
        while a < WIDTH and a > -1 and b < HEIGHT and b > -1 and board[(b*WIDTH)+a] == id:
            thisLine += 1
            a += d[0]
            b += d[1]
        if thisLine > line:
            line = thisLine
    return line
        
     
# Checking for the winner on every move.
def winner(board, id):#If game ended means if someone won
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[(y*WIDTH)+x] == id:
                if lineLenght(board, x, y, id) >= TIMES:return True
    return False

# Getting valid moves.
def valids(board):
    a = [move for move in range(WIDTH) if board[move] == 0]
    a.sort(key = lambda a: abs(WIDTH // 2 - a))
    return a

# Evaluating value using minimax algo.
def value(board, id)
    val = 0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[(y*WIDTH)+x] != 0:
                val += (lineLenght(board, x, y, board[(y*WIDTH)+x]) * WEIGHT_LENGHT) * (1 if board[(y*WIDTH)+x] == id else -1)
                val += (WIDTH - (abs(WIDTH // 2 - x))) * WEIGHT_PLACE * (1 if board[(y*WIDTH)+x] == id else -1)
    return val

# Playing the move.
def play(board, m, id):
    for y in range(HEIGHT):
        if board[(y*WIDTH)+m] != 0:
            board[((y-1)*WIDTH)+m] = id
            break
        if y == HEIGHT - 1:
            board[(y*WIDTH)+m] = id

# Main Minimax algo. implementation.
def minimax(board, depth, id, beta, root):
    global TT
    if depth == 0:
        return value(board, id)
    mask = str(board)
    try:
        return TT[mask]
    except:
        pass
    MAXVAL = -WIN
    BEST = 0
    save = copy.deepcopy(board)
    valid = valids(board)
    oppId = 2 if id == 1 else 1
    if len(valid) == 0:return DRAW
    add = True
    for move in valid:
        board = copy.deepcopy(save)
        play(board, move, id)
        if winner(board, id):
            if root:
                return move
            MAXVAL = WIN
            break
        thisValue = -minimax(board, depth - 1, oppId, MAXVAL, False) * GAMMA
        if thisValue > MAXVAL:
            MAXVAL = thisValue
            BEST = move
        if -MAXVAL * GAMMA <= beta and not root:
            add = False
            break
    if add:TT[mask] = MAXVAL
    if root:
        TT.clear()
    return BEST if root else MAXVAL
