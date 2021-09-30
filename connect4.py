import Game.setup as GS # the main module create by Jrke which runs the complete game

difficulty_levels = ['beginner', 'very easy', 'easy', 'medium', 'hard', 'very hard', 'master'] # difficulty levels to play the game
difficulty_level = 3

'''Difficulty is level of AI you want to play with needed if you want to against AI should be between 0 - 6
Player1 and player2 name if you want to play against AI then replace name with 'AI'
name = ['AI', 'Akshat'] AI will act as player 1 and Akshat (human player) as player 2
name = ['Akshat', 'AI'] AI will act as player 2 and Akshat (human player) as player 1
name = ['AI', 'AI'] AI will act as player 2 as well as player 1 a match between 2 AIs
name = ['Akshat', 'Aryan'] a match between two human players i.e. Akshat vs Aryan'''
name = ["Akshat", "AI"]

# Game Initialisation
GS.Initialise(name = name)
# Setting game difficulty
GS.set_difficulty(level = difficulty_levels[difficulty_level])
# Starting the game
GS.match()
# Ending the Game  
GS.end()
# Restart Procedure
while GS.restart:
    GS.Initialise(name = name)
    GS.match()
    GS.end()
