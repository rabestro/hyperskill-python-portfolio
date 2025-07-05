def introduce_bot(bot_name: str, birth_year: int) -> None:
    print(f"""
    Hello! My name is {bot_name}.
    I was created in {birth_year}.
    """)


def remind_name() -> None:
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
    print("Let's test your programming knowledge.")
    while True:
        answer = int(
            input("""Why do we use methods?
        1. To repeat a statement multiple times.
        2. To decompose a program into several small subroutines.
        3. To determine the execution time of a program.
        4. To interrupt the execution of a program.""")
        )
        if answer == 2:
            break
    print("Completed, have a nice day!")


def print_congratulations() -> None:
    print("Congratulations, have a nice day!")
