import Game.setup as GS

difficulty_levels = ['beginner', 'very easy', 'easy', 'medium', 'hard', 'very hard', 'master']
difficulty_level = 3

'''Difficulty is level of AI you want to play with needed if you want to against AI should be between 0 - 6
Player1 and player2 name if you want to play against AI then replace name with 'AI'
name = ['AI', 'Akshat'] AI will act as player 1 and Akshat (human player) as player 2
name = ['Akshat', 'AI'] AI will act as player 2 and Akshat (human player) as player 1
name = ['AI', 'AI'] AI will act as player 2 as well as player 1 a match between 2 AIs
name = ['Akshat', 'Aryan'] a match between two human players i.e. Akshat vs Aryan'''
name = ["Akshat", "AI"]

GS.Initialise(name = name)
GS.set_difficulty(level = difficulty_levels[difficulty_level])
GS.match()
GS.end()
while GS.restart:
    GS.Initialise(name = name)
    GS.match()
    GS.end()
