import random


def get_friend_names(count: int) -> list[str]:
    """Gets a list of names from user input."""
    print("Enter the name of every friend (including you), each on a new line:")
    return [input() for _ in range(count)]


def main() -> None:
    """Main function to run the bill splitter."""
    try:
        n_friends = int(input("Enter the number of friends joining (including you):"))
    except ValueError:
        print("Please enter a valid number.")
        return

    if n_friends <= 0:
        print("No one is joining for the party")
        return

    names = get_friend_names(n_friends)

    try:
        bill_value = float(input("Enter the total bill value:"))
    except ValueError:
        print("Invalid bill amount. Please enter a numeric value.")
        return

    wants_lucky_feature = (
        input('Do you want to use the "Who is lucky?" feature? Write Yes/No:').lower()
        == "yes"
    )

    if wants_lucky_feature and names:
        lucky_friend = random.choice(names)
        print(f"{lucky_friend} is the lucky one!")

        # Payers are everyone except the lucky one
        num_payers = n_friends - 1
        split_value = round(bill_value / num_payers, 2) if num_payers > 0 else 0

        final_bill = {
            name: (0 if name == lucky_friend else split_value) for name in names
        }
    else:
        print("No one is going to be lucky")
        split_value = round(bill_value / n_friends, 2)
        final_bill = dict.fromkeys(names, split_value)

    print(f"\n{final_bill}")


if __name__ == "__main__":
    main()
