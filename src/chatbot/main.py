from . import bot


def main() -> None:
    """Initializes and runs the game."""

    bot.show_bot_info(bot.BOT_NAME, bot.BIRTH_YEAR)
    bot.ask_for_name()
    bot.guess_age()
    bot.count_to_number()
    bot.quiz_programming_concepts()
    bot.show_congratulations_message()


if __name__ == "__main__":
    main()
