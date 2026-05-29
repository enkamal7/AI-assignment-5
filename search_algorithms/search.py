import math
import random

# --------------------
# MINIMAX
# --------------------

def minimax(game, depth, maximizing):

    winner = game.winner()

    if winner == "X":
        return 10 - depth

    if winner == "O":
        return depth - 10

    if game.is_full():
        return 0

    if maximizing:

        best = -math.inf

        for move in game.available_moves():

            game.make_move(move, "X")

            score = minimax(
                game,
                depth + 1,
                False
            )

            game.undo_move(move)

            best = max(best, score)

        return best

    else:

        best = math.inf

        for move in game.available_moves():

            game.make_move(move, "O")

            score = minimax(
                game,
                depth + 1,
                True
            )

            game.undo_move(move)

            best = min(best, score)

        return best


# --------------------
# ALPHA BETA
# --------------------

def alphabeta(
    game,
    depth,
    alpha,
    beta,
    maximizing
):

    winner = game.winner()

    if winner == "X":
        return 10 - depth

    if winner == "O":
        return depth - 10

    if game.is_full():
        return 0

    if maximizing:

        value = -math.inf

        for move in game.available_moves():

            game.make_move(move, "X")

            value = max(
                value,
                alphabeta(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    False
                )
            )

            game.undo_move(move)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in game.available_moves():

            game.make_move(move, "O")

            value = min(
                value,
                alphabeta(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    True
                )
            )

            game.undo_move(move)

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# --------------------
# HEURISTIC FUNCTION
# --------------------

def heuristic(game):

    score = 0

    lines = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for line in lines:

        x = 0
        o = 0

        for pos in line:

            if game.board[pos] == "X":
                x += 1

            elif game.board[pos] == "O":
                o += 1

        if x == 2 and o == 0:
            score += 10

        if o == 2 and x == 0:
            score -= 10

    return score


# --------------------
# HEURISTIC ALPHABETA
# --------------------

def heuristic_alphabeta(
    game,
    depth,
    alpha,
    beta,
    maximizing,
    limit=3
):

    winner = game.winner()

    if winner == "X":
        return 100

    if winner == "O":
        return -100

    if game.is_full():
        return 0

    if depth >= limit:
        return heuristic(game)

    if maximizing:

        value = -math.inf

        for move in game.available_moves():

            game.make_move(move, "X")

            value = max(
                value,
                heuristic_alphabeta(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    False,
                    limit
                )
            )

            game.undo_move(move)

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:

        value = math.inf

        for move in game.available_moves():

            game.make_move(move, "O")

            value = min(
                value,
                heuristic_alphabeta(
                    game,
                    depth + 1,
                    alpha,
                    beta,
                    True,
                    limit
                )
            )

            game.undo_move(move)

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# --------------------
# MONTE CARLO TREE SEARCH
# --------------------

def random_playout(game, player):

    current = player

    while True:

        winner = game.winner()

        if winner == "X":
            return 1

        if winner == "O":
            return -1

        if game.is_full():
            return 0

        move = random.choice(
            game.available_moves()
        )

        game.make_move(move, current)

        current = (
            "O"
            if current == "X"
            else "X"
        )


def mcts(game, simulations=500):

    best_move = None
    best_score = -999

    for move in game.available_moves():

        wins = 0

        for _ in range(simulations):

            game.make_move(move, "X")

            result = random_playout(
                game,
                "O"
            )

            game.undo_move(move)

            wins += result

        if wins > best_score:

            best_score = wins
            best_move = move

    return best_move