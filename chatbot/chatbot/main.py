from .bot import (
    count_to_number,
    guess_age,
    introduce_bot,
    print_congratulations,
    quiz_programming_concepts,
    remind_name,
)


def main() -> None:
    """Initializes and runs the game."""

    introduce_bot(bot_name="Aid", birth_year=2020)
    remind_name()
    guess_age()
    count_to_number()
    quiz_programming_concepts()
    print_congratulations()


if __name__ == "__main__":
    main()
