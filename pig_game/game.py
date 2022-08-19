import random
import time

from pig_game.computer_player import ComputerPlayer


class PigGame:
    scores = {"human": 0, "computer": 0}
    _winner = None
    next_player = {"human": "computer", "computer": "human"}
    opponent = ComputerPlayer()
    die_values = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}

    def new_round(self, player):
        print(
            f"Scores:\n Human: {self.scores['human']}, Computer: {self.scores['computer']}"
        )
        print("-" * 30)
        current_score = 0
        if player == "computer":
            aim = self.opponent.get_aim(self.scores)
            while current_score < aim:
                time.sleep(0.2)
                throw = self.roll_die()
                current_score += throw
                self._print_dice_value(throw)
                if throw == 1:
                    print("0 points!")
                    print("-" * 30)
                    return
                print(f"Turn score: {current_score}")
                if self.scores[player] + current_score >= 100:
                    self._winner = player
                    return
            else:
                self.scores[player] += current_score
        else:
            print("Your turn!")
            time.sleep(0.5)
            while True:
                throw = self.roll_die()
                self._print_dice_value(throw)
                if throw == 1:
                    print("O points!")
                    print("-" * 30)
                    return
                current_score += throw
                print(f"Turn score: {current_score}")
                if self.scores[player] + current_score >= 100:
                    self._winner = player
                    return
                answer = input("Roll again or hold? [roll|hold]").lower()
                if answer in {"hold", "h"}:
                    self.scores[player] += current_score
                    return

    def roll_die(self):
        return random.randint(1, 6)

    def _print_dice_value(self, throw):
        print(f"🎲 {self.die_values[throw]}")

    def get_rules(self):
        return "rules"

    def get_winner(self):
        return self._winner

    def run_game(self, start_player):
        player = start_player
        while self._winner is None:
            self.new_round(player)
            player = self.next_player[player]
