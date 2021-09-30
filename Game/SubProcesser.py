# Importing necessary modules to run the bot playing the game.
from subprocess import Popen, PIPE
from .constants import const

cs = const()

# Executing the bot executable file.
def MASTER(id = 1, board = ("0"*42)):
    AI = Popen([cs.directory + '\\Master.exe'], shell=True, stdout=PIPE, stdin=PIPE)
    AI.stdin.write(bytes(f'{id}\n', 'UTF-8'))
    AI.stdin.flush()
    AI.stdin.write(bytes(board + '\n', 'UTF-8'))
    AI.stdin.flush()
    result = AI.stdout.readline().strip()
    return int(result)
