from games import TicTacToe
from search import *

game = TicTacToe()

game.board = [

    "X","X"," ",
    "O","O"," ",
    " "," "," "

]

print("BOARD")

game.print_board()

print("MINIMAX")

print(
    minimax(
        game,
        0,
        True
    )
)

print("\nALPHA BETA")

print(
    alphabeta(
        game,
        0,
        -999,
        999,
        True
    )
)

print("\nHEURISTIC ALPHA BETA")

print(
    heuristic_alphabeta(
        game,
        0,
        -999,
        999,
        True
    )
)

print("\nMCTS")

print(
    mcts(
        game,
        300
    )
)