import logging

from .file_handler import DEFAULT_RATING_FILE, get_user_score
from .game_logic import GameRules, create_rules_from_input

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def handle_game_turn(user_input: str, current_score: int, rules: GameRules) -> int:
    """
    Handles a single user input during the game.

    Args:
        user_input: The command or move entered by the user.
        current_score: The user's current score.
        rules: The rules for the current game.

    Returns:
        The updated score after the turn.
    """
    if not rules.is_valid_option(user_input):
        print("Invalid input")
        return current_score

    computer_choice = rules.get_random_option()
    result = rules.compare(user_input, computer_choice)

    match result:
        case 1:
            print(f"Well done. The computer chose {computer_choice} and failed")
            return current_score + 100
        case 0:
            print(f"There is a draw ({user_input})")
            return current_score + 50
        case _:
            print(f"Sorry, but the computer chose {computer_choice}")
            return current_score


def game_loop(initial_score: int, rules: GameRules) -> None:
    """
    Runs the main interactive game loop.

    Args:
        initial_score: The player's starting score.
        rules: The rules for the current game.
    """
    score = initial_score
    while True:
        user_input = input().lower()
        match user_input:
            case "!exit":
                break
            case "!rating":
                print(f"Your rating: {score}")
            case _:
                score = handle_game_turn(user_input, score, rules)

    print("Bye!")


def main() -> None:
    """Sets up the game and runs the main loop."""
    # --- 1. Setup Phase ---
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")

    rules = create_rules_from_input(
        input(
            "Enter game options (e.g., rock,paper,scissors) or leave empty for default:"
        )
    )
    print("Okay, let's start")

    try:
        initial_score = get_user_score(user_name, file_path=DEFAULT_RATING_FILE)
    except FileNotFoundError:
        logging.info(f"{DEFAULT_RATING_FILE} not found. Starting with a score of 0.")
        initial_score = 0
    except ValueError as e:
        logging.warning(
            f"Could not retrieve score for {user_name}: {e}. Starting with 0."
        )
        initial_score = 0

    # --- 2. Game Loop Phase ---
    game_loop(initial_score, rules)


if __name__ == "__main__":
    main()
