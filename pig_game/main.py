import random

from unicode_pig.pig import Pig

from pig_game.game import PigGame


def play():
    game = PigGame()
    print("\n")
    Pig().run()
    print("Welcome! Do you want to play *Pig*? [yes|no]")
    answer = input()
    if answer.lower() in {"yes", "y", "z", "zes", ""}:
        start_player = random.choice(["human", "computer"])
        print(f"Start player: {start_player}")
        game.run_game(start_player)
        winner = game.get_winner()
        if winner == "human":
            print("Congratulations! You won!")
        else:
            print("You lost.")

    print("Goodbye. Oink.")
    print("\n")
    Pig().run(reversed=True)


if __name__ == "__main__":
    play()
