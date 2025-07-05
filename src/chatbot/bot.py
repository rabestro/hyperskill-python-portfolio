import textwrap

BOT_NAME = "Aid"
BIRTH_YEAR = 2020
QUIZ_CORRECT_ANSWER = 2
QUIZ_PROMPT = textwrap.dedent("""
    Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
""")


def show_bot_info(bot_name: str, birth_year: int) -> None:
    intro_message = textwrap.dedent(f"""
        Hello! My name is {bot_name}.
        I was created in {birth_year}.
    """)
    print(intro_message)


def ask_for_name() -> None:
    name = input("Please, remind me your name.")
    print(f"What a great name you have, {name}!")


def guess_age() -> None:
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a good time to start programming!")


def count_to_number() -> None:
    print("Now I will prove to you that I can count to any number you want.")

    target_number = int(input())
    for current_count in range(target_number + 1):
        print(current_count, "!")


def quiz_programming_concepts() -> None:
    """Tests the user's programming knowledge."""
    print("\nLet's test your programming knowledge.")
    print(QUIZ_PROMPT)
    while True:
        try:
            answer = int(input("Enter your choice: "))
            if answer == QUIZ_CORRECT_ANSWER:
                break
            else:
                print("Please, try again.")
        except ValueError:
            print("That's not a valid number. Please try again.")


def show_congratulations_message() -> None:
    print("Congratulations, have a nice day!")
