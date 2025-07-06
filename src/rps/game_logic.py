import random
from dataclasses import dataclass

DEFAULT_OPTIONS = ("rock", "paper", "scissors")


@dataclass(frozen=True)
class GameRules:
    """
    Represents the rules of a Rock-Paper-Scissors style game.

    This class is immutable; a new instance should be created for new rules.
    """

    options: tuple[str, ...] = DEFAULT_OPTIONS

    def is_valid_option(self, option: str) -> bool:
        return option in self.options

    def get_random_option(self) -> str:
        return random.choice(self.options)

    def compare(self, player_1_choice: str, player_2_choice: str) -> int:
        """
        Compares two choices.
        Returns:
             1 if player_1_choice wins
             0 if it's a draw
            -1 if player_2_choice wins
        """
        if player_1_choice == player_2_choice:
            return 0
        length = len(self.options)
        half = length // 2
        first_index = self.options.index(player_1_choice)
        delta = half - first_index
        first_index = (first_index + delta) % length
        second_index = (self.options.index(player_2_choice) + delta) % length
        return -1 if first_index < second_index else 1


def create_rules_from_input(options_str: str) -> GameRules:
    if not options_str:
        return GameRules()

    options_tuple = tuple(options_str.strip().lower().split(","))
    return GameRules(options=options_tuple)
