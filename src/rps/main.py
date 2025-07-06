import logging

from file_handler import DEFAULT_RATING_FILE, get_user_score
from game_logic import create_rules_from_input

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main() -> None:
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    options = create_rules_from_input(input())
    print("Okay, let's start")

    try:
        score = get_user_score(user_name, file_path=DEFAULT_RATING_FILE)
    except FileNotFoundError:
        logging.info(f"{DEFAULT_RATING_FILE} not found. Starting with a score of 0.")
        score = 0
    except ValueError as e:
        logging.warning(
            f"Could not retrieve score for {user_name}: {e}. Starting with 0."
        )
        score = 0

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


if __name__ == "__main__":
    main()
