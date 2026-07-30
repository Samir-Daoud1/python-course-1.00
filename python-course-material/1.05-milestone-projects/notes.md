# 1.5 — Milestone Projects

Time to put everything from sections 1.1–1.4 together. Don't worry if it
seems tricky at first — break each project into small pieces and tackle
one step at a time.

## 🎯 Project 1 — Number Guessing Game

A game that picks a random number and lets the player guess it.

**Step-by-step plan**

| Step | What it does |
|---|---|
| 1 | Generate a random number between 1 and 100 |
| 2 | Write a function that checks if the player's input is a valid digit |
| 3 | Start an infinite loop that keeps asking the player to guess |
| 4 | If the input is not a valid number, tell the player and ask again |
| 5 | Convert the valid input into an integer |
| 6 | Compare the guess to the random number: too low, too high, or correct |
| 7 | If correct, congratulate the player and end the game |

**Hints to get you started**

To generate a random number, Python has a built-in library called
`random`. A library is a collection of pre-written code you can use in
your own programs by importing it:

```python
import random  # gives you access to random number tools

# randint(a, b) gives a random whole number between a and b, inclusive
answer = random.randint(1, 100)
```

Remember the `.isdigit()` check from earlier? You'll need a function like
`check_isdigit()` to validate the player's guess before turning it into an
integer. And remember: `input()` always returns a string, even if the
player typed numbers!

**Things to think about**
- How do you keep asking the player to guess until they get it right?
  (Hint: `while True` + `break`)
- What should happen if the player types something that isn't a number?
- How do you tell the player if their guess is too high or too low?

👉 Working code: [`project-1-guessing-game/guessing_game.py`](project-1-guessing-game/guessing_game.py)

---

## 🎯 Project 2 — Simplified Tic Tac Toe

Two players take turns placing X and O on a 3×3 grid in the terminal. This
project is a bit harder — take it one function at a time!

**Step-by-step plan**

| Step | What it does |
|---|---|
| 1 | Create the board as a list, with numbers 1–9 as placeholders |
| 2 | Display the board as a 3×3 grid using `print()` |
| 3 | Ask the current player to choose a spot (1–9) |
| 4 | Validate the input: is it a digit? Is it 1–9? Is the spot free? |
| 5 | Place the player's marker (X or O) on the board |
| 6 | Switch to the other player |
| 7 | Check if the board is completely full to end the game |

**Hint: how the board works**

The board is just a regular Python list with 9 elements, written out like
a grid so it's easier to picture (but it's really one flat list of 9
items):

```python
board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]
```

Each position starts out holding its own number as a placeholder (so the
player can see which number to type for that spot). When a player picks a
spot, you replace that number with `"X"` or `"O"`. Remember: list indexes
start at 0, so position 1 on the board is actually `board[0]`, position 2
is `board[1]`, and so on — you'll need to subtract 1 from the player's
choice!

To print the board as a 3×3 grid, you access groups of 3 items at a time:

```python
print(board[0], "|", board[1], "|", board[2])
print(board[3], "|", board[4], "|", board[5])
print(board[6], "|", board[7], "|", board[8])
```

To know when the game should stop, you need a function that checks every
cell in the board and returns `True` only if no numbers remain (meaning
every spot has been replaced by `"X"` or `"O"`). Think about how you would
loop through the board and check each cell — what should happen the
moment you find a number still there?

**Things to think about**
- How do you alternate the `player` variable between `"X"` and `"O"`
  after each turn?
- How do you stop a player from picking a spot that's already taken?
- How would you check if a player has won? (This is optional — a great
  challenge!)

👉 Working code: [`project-2-tic-tac-toe/tic_tac_toe.py`](project-2-tic-tac-toe/tic_tac_toe.py)
