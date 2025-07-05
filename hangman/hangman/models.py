import dataclasses
import enum


class Status(enum.Enum):
    HIT = "You hit!"
    MISS = "That letter doesn't appear in the word."
    SAME = "You've already guessed this letter."


class MenuOption(enum.Enum):
    PLAY = "play"
    RESULTS = "results"
    EXIT = "exit"


@dataclasses.dataclass
class GameStatistics:
    wins: int = 0
    losses: int = 0


@dataclasses.dataclass
class HangmanSession:
    """Represents a single game session of Hangman."""

    word: str
    guesses: set[str] = dataclasses.field(default_factory=set)
    _unique_word_letters: frozenset[str] = dataclasses.field(init=False, repr=False)

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
