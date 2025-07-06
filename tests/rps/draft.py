import random


class GameOptions:
    def __init__(self, options: str) -> None:
        if not options:
            self.options = ("rock", "paper", "scissors")
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


def get_user_score(username):
    """
    Reads 'rating.txt' to find and return a user's score.
    Returns 0 if the user is not found or the file doesn't exist.
    """
    try:
        with open("rating.txt") as file:
            for line in file:
                # Split each line into name and score
                parts = line.strip().split()
                if len(parts) == 2:
                    name, score = parts
                    if name == username:
                        # Found the user, return their score as an integer
                        return int(score)
    except FileNotFoundError:
        # The file doesn't exist, so we can't have a score.
        print("rating.txt not found. Starting with a score of 0.")
        return 0
    except ValueError:
        # This handles cases where the score in the file isn't a valid number.
        print("Error reading score from rating.txt. Starting with a score of 0.")
        return 0

    # If the loop finishes and the user was not found
    return 0


def game():
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    options = GameOptions(input())
    print("Okay, let's start")
    score = get_user_score(user_name)

    while True:
        match input().lower():
            case "!exit":
                break
            case "!rating":
                print(f"Your rating: {score}")
            case user_choice if options.is_valid_option(user_choice):
                computer_choice = options.get_random_option()
                match options.compare(user_choice, computer_choice):
                    case 1:
                        score += 100
                        print(
                            f"Well done. The computer chose {
                                computer_choice
                            } and failed"
                        )
                    case 0:
                        score += 50
                        print(f"There is a draw ({user_choice})")
                    case -1:
                        print(f"Sorry, but the computer chose {computer_choice}")
            case _:
                print("Invalid input")

    print("Bye!")


game()
