# pig-game
The dice game "Pig" for the command line

## Usage
Install from github with

```sh
pip install git+https://github.com/knit-bee/pig-game.git
```

Start the game by entering ```pig-game```

### Rules
- You play against the computer, the player who first reaches 100 points wins.
- Each turn, the current player rolls a die. The number of spots is added to their current turn score. After each throw, the player can decide to continue rolling the die or the keep the points. As long as they don't roll a 1, the player can continue to roll and increase their turn score.
- If the player decides to hold the points, they are added to their total score, and the other player continues.
- If a player rolls a 1, they lose all their turn score points and the other player continues.
