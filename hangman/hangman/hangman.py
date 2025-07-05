import dataclasses
import enum
import random
from dataclasses import field
from typing import Final  # For constants

# --- Core Data Structures (Excellent as they were) ---


class Status(enum.Enum):
    HIT = "You hit!"  # Giving HIT a value makes logic slightly more uniform
    MISS = "That letter doesn't appear in the word."
    SAME = "You've already guessed this letter."


@dataclasses.dataclass
class HangmanSession:
    word: str
    guesses: set[str] = field(default_factory=set)
    _unique_word_letters: frozenset[str] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        """Cache the unique letters of the word for efficient checking."""
        self._unique_word_letters = frozenset(self.word)

    def make_guess(self, letter: str) -> Status:
        if letter in self.guesses:
            return Status.SAME
        self.guesses.add(letter)
        return Status.HIT if letter in self.word else Status.MISS

    def get_current_progress(self) -> str:
        return "".join(c if c in self.guesses else "-" for c in self.word)

    def is_word_solved(self) -> bool:
        """Check if all unique letters in the word have been guessed."""
        return self._unique_word_letters.issubset(self.guesses)


@dataclasses.dataclass
class GameStatistics:
    wins: int = 0
    losses: int = 0


class MenuOption(enum.Enum):
    PLAY = "play"
    RESULTS = "results"
    EXIT = "exit"


# --- Main Game Controller Class ---


class Game:
    """Manages the application flow and state."""

    WORD_BANK: Final[tuple[str, ...]] = ("python", "java", "swift", "javascript")
    MAX_ATTEMPTS: Final[int] = 8

    def __init__(self) -> None:
        self.statistics = GameStatistics()

    def run(self) -> None:
        """Start the main game loop."""
        print("H A N G M A N")
        while True:
            command = self._get_menu_command()
            if command == MenuOption.EXIT:
                break
            elif command == MenuOption.PLAY:
                self._play_one_game()
            elif command == MenuOption.RESULTS:
                self._show_results()

    def _play_one_game(self) -> None:
        """Manages the logic for a single round of Hangman."""
        random_word = random.choice(self.WORD_BANK)
        session = HangmanSession(random_word)
        remaining_attempts = self.MAX_ATTEMPTS

        while remaining_attempts > 0 and not session.is_word_solved():
            print()
            print(session.get_current_progress())

            letter = self._get_letter_from_user()
            if not letter:
                continue

            status = session.make_guess(letter)

            # More explicit status checks
            if status == Status.MISS:
                print(status.value)
                remaining_attempts -= 1
            elif status == Status.SAME:
                print(status.value)

        print()
        if session.is_word_solved():
            print(session.word)  # The word is fully revealed
            print(f"You guessed the word {session.word}!")
            print("You survived!")
            self.statistics.wins += 1
        else:
            print("You lost!")
            self.statistics.losses += 1

    def _show_results(self) -> None:
        """Prints the current game statistics."""
        print(f"You won: {self.statistics.wins} times.")
        print(f"You lost: {self.statistics.losses} times.")

    @staticmethod
    def _get_letter_from_user() -> str | None:
        """Gets a valid single lowercase letter from the user."""
        char = input("Input a letter: ")
        if len(char) != 1:
            print("Please, input a single letter.")
            return None
        if not char.isascii() or not char.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            return None
        return char

    @staticmethod
    def _get_menu_command() -> MenuOption:
        """Gets a valid menu command from the user."""
        command_map = {opt.value: opt for opt in MenuOption}

        while True:
            prompt = (
                'Type "play" to play the game, "results" to show the scoreboard, '
                'and "exit" to quit:'
            )
            raw_input = input(prompt).lower()
            command = command_map.get(raw_input)
            if command:
                return command

            print("Invalid command. Please, try again.")


# --- Script Entry Point ---
if __name__ == "__main__":
    game = Game()
    game.run()
