import random
import os

# Two players, 0 and 1
# 0 = human
# 1 = computer

scores = [0, 0]  # players' scores

def show_scores():
    print("-" * 20)
    print(f"Human: {scores[0]}")
    print(f"Computer: {scores[1]}")
    print("-" * 20)


def choice(round_score, my_score, opponent_score):
    # TODO: return True if the player wants to roll again
    #       return False if the player wants to hold
    # example (bad) strategy:
    return round_score <= 12


def take_turn(player):
    round_score = 0
    while True:
        roll = random.randint(1, 6)
        print(f"Roll: {roll}")
        if roll == 1:
            round_score = 0
            break
        else:
            round_score += roll
            print(f"Current total: {round_score}")
            if player == 0:
                c = input("Roll again? (y/n)").lower()
                if c != "y":
                    break
            else:
                if not choice(round_score, scores[1], scores[0]):
                    break

    print(f"Points earned this turn: {round_score}")
    input("Turn is over. Press  to continue.")
    return round_score

turn = 0  # whose turn is it?
# This loop will alternate between players taking turns
playing = True  # this becomes False when the game ends at 100 pts
while playing:
    os.system("clear")
    show_scores()
    scores[turn] += take_turn(turn)
    if max(scores) >= 100:
        playing = False
    turn = 1 if turn == 0 else 0

print("Final scores:")
show_scores()
