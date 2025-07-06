from file_handler import get_user_score
from game_logic import GameOptions


def main():
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


if __name__ == "__main__":
    main()
