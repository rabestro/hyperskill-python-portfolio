import random

DEFAULT_OPTIONS = ("rock", "paper", "scissors")


class GameOptions:
    def __init__(self, options: str) -> None:
        if not options:
            self.options = DEFAULT_OPTIONS
        else:
            self.options = tuple(options.strip().lower().split(","))

    def is_valid_option(self, option: str) -> bool:
        return option in self.options

    def get_random_option(self) -> str:
        return random.choice(self.options)

    def compare(self, user_choice: str, computer_choice: str) -> int:
        if user_choice == computer_choice:
            return 0
        length = len(self.options)
        half = length // 2
        first_index = self.options.index(user_choice)
        delta = half - first_index
        first_index = (first_index + delta) % length
        second_index = (self.options.index(computer_choice) + delta) % length
        return -1 if first_index < second_index else 1
