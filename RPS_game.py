
import random

def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    p1_score = 0
    p2_score = 0

    for i in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        result = winner(p1_play, p2_play)
        if result == 1:
            p1_score += 1
        elif result == -1:
            p2_score += 1

        if verbose:
            print(f"Game {i+1}:")
            print(f"Player 1: {p1_play}  Player 2: {p2_play}")
            print(f"Score -> Player 1: {p1_score}  Player 2: {p2_score}")
            print("")

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    print(f"Final Score - Player 1: {p1_score} / Player 2: {p2_score}")
    print(f"Player 1 Win Rate: {p1_score / num_games * 100:.2f}%")
    print(f"Player 2 Win Rate: {p2_score / num_games * 100:.2f}%")

    return p1_score / num_games

def winner(p1, p2):
    if p1 == p2:
        return 0
    elif (p1 == "R" and p2 == "S") or (p1 == "P" and p2 == "R") or (p1 == "S" and p2 == "P"):
        return 1
    else:
        return -1


# Opponent Bots

def quincy(prev_play, opponent_history=[]):
    options = ["R", "P", "S", "R", "P"]
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    return options[len(opponent_history) % len(options)]

def abbey(prev_play, opponent_history=[]):
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)

    last_two = opponent_history[-2:]
    guess = "R"
    if len(last_two) == 2:
        if last_two[0] == last_two[1]:
            guess = counter_move(last_two[0])
        else:
            guess = last_two[-1]
    return guess

def kris(prev_play):
    if prev_play == "":
        prev_play = "R"
    if prev_play == "R":
        return "P"
    if prev_play == "P":
        return "S"
    if prev_play == "S":
        return "R"

def mrugesh(prev_play, opponent_history=[]):
    if prev_play == "":
        prev_play = "R"
    opponent_history.append(prev_play)
    if len(opponent_history) > 5:
        recent = opponent_history[-5:]
        most_frequent = max(set(recent), key=recent.count)
        return counter_move(most_frequent)
    else:
        return "R"

def counter_move(move):
    if move == "R":
        return "P"
    if move == "P":
        return "S"
    if move == "S":
        return "R"
