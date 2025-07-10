def main() -> None:
    earned_amount = {
        "Bubblegum": 202,
        "Toffee": 118,
        "Ice cream": 2250,
        "Milk chocolate": 1680,
        "Doughnut": 1075,
        "Pancake": 80,
    }

    income = sum(earned_amount.values())

    print("Earned amount:")
    for name, amount in earned_amount.items():
        print(f"{name}: ${amount}")
    print(f"Income: ${income}")

    staff_expenses = int(input("Staff expenses: "))
    other_expenses = int(input("Other expenses: "))
    net_income = income - staff_expenses - other_expenses
    print(f"Net income: ${net_income}")


if __name__ == "__main__":
    main()
