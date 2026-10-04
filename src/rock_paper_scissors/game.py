"""Rock, Paper, Scissors: play against the computer."""

import os
import random
import sys

TITLE = r"""
 ____   ___   ____ _  __
|  _ \ / _ \ / ___| |/ /
| |_) | | | | |   | ' /
|  _ <| |_| | |___| . \
|_| \_\\___/ \____|_|\_\
 ____   _    ____  _____ ____
|  _ \ / \  |  _ \| ____|  _ \
| |_) / _ \ | |_) |  _| | |_) |
|  __/ ___ \|  __/| |___|  _ <
|_| /_/   \_\_|   |_____|_| \_\
 ____   ____ ___ ____ ____   ___  ____  ____
/ ___| / ___|_ _/ ___/ ___| / _ \|  _ \/ ___|
\___ \| |    | |\___ \___ \| | | | |_) \___ \
 ___) | |___ | | ___) |__) | |_| |  _ < ___) |
|____/ \____|___|____/____/ \___/|_| \_\____/
"""

RESET = "\033[0m"
# One colour per word of the title: ROCK, PAPER, SCISSORS.
TITLE_COLORS = ["\033[91m", "\033[93m", "\033[96m"]
TITLE_LINES_PER_WORD = 5


def supports_color() -> bool:
    """Return True if ANSI colours should be used on stdout."""
    return sys.stdout.isatty() and "NO_COLOR" not in os.environ


def colorize_title(title: str = TITLE, enabled: bool | None = None) -> str:
    """Return the title with each word coloured, or unchanged if colour is off."""
    if enabled is None:
        enabled = supports_color()
    if not enabled:
        return title
    lines = title.strip("\n").split("\n")
    coloured = [
        f"{TITLE_COLORS[i // TITLE_LINES_PER_WORD]}{line}{RESET}"
        for i, line in enumerate(lines)
    ]
    return "\n" + "\n".join(coloured) + "\n"


ROCK = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

CHOICES = [ROCK, PAPER, SCISSORS]
NAMES = ["Rock", "Paper", "Scissors"]

WIN = "win"
LOSE = "lose"
DRAW = "draw"


def determine_result(user: int, computer: int) -> str:
    """Return WIN, LOSE or DRAW from the user's point of view.

    Choices are 0 = rock, 1 = paper, 2 = scissors.
    """
    if user == computer:
        return DRAW
    # Each choice beats the one before it (paper > rock, scissors > paper, rock > scissors).
    if (user - computer) % 3 == 1:
        return WIN
    return LOSE


def parse_choice(text: str) -> int | None:
    """Convert raw input to a choice index, or None if invalid."""
    try:
        value = int(text.strip())
    except ValueError:
        return None
    return value if 0 <= value < len(CHOICES) else None


def main() -> None:
    os.system("")  # enables ANSI escape handling on Windows consoles
    print(colorize_title())
    raw = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    user = parse_choice(raw)
    if user is None:
        print("You typed an invalid number. You lose!")
        return

    computer = random.randint(0, len(CHOICES) - 1)
    print(f"You chose {NAMES[user]}:{CHOICES[user]}")
    print(f"Computer chose {NAMES[computer]}:{CHOICES[computer]}")

    result = determine_result(user, computer)
    if result == WIN:
        print("You win!")
    elif result == LOSE:
        print("You lose!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
