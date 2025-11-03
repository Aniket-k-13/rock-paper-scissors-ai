

def player(prev_play, opponent_history=[]):
    import random

    # Store opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # Start with a default
    guess = "R"

    # Strategy: Pattern matching using last 3 opponent moves
    # Try to predict the next move based on history
    n = 3
    if len(opponent_history) > n:
        # Take last n moves as a sequence
        recent_pattern = "".join(opponent_history[-n:])
        # Build a dictionary of sequences -> next move frequency
        patterns = {}
        for i in range(len(opponent_history) - n):
            pattern = "".join(opponent_history[i:i + n])
            next_move = opponent_history[i + n]
            if pattern not in patterns:
                patterns[pattern] = {"R": 0, "P": 0, "S": 0}
            patterns[pattern][next_move] += 1

        # Predict next move based on most frequent following move
        if recent_pattern in patterns:
            prediction = max(patterns[recent_pattern], key=patterns[recent_pattern].get)
        else:
            prediction = random.choice(["R", "P", "S"])
    else:
        prediction = random.choice(["R", "P", "S"])

    # Choose move to beat predicted opponent move
    beats = {"R": "P", "P": "S", "S": "R"}
    guess = beats[prediction]

    return guess
