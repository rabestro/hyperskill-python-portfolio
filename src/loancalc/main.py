import argparse
import math
import sys

# --- Custom Types for Validation ---


def non_negative_float(value: str) -> float:
    """Custom argparse type for non-negative floats."""
    try:
        f_value = float(value)
    except ValueError:
        # Raise the new exception, suppressing the original ValueError context.
        raise argparse.ArgumentTypeError(f"invalid float value: '{value}'") from None
    if f_value < 0:
        raise argparse.ArgumentTypeError(f"value must be non-negative: {f_value}")
    return f_value


def non_negative_int(value: str) -> int:
    """Custom argparse type for non-negative integers."""
    try:
        i_value = int(value)
    except ValueError:
        # Do the same for the integer version.
        raise argparse.ArgumentTypeError(f"invalid int value: '{value}'") from None
    if i_value < 0:
        raise argparse.ArgumentTypeError(f"value must be non-negative: {i_value}")
    return i_value


# --- Calculation Logic (Pure Functions) ---
# These functions remain largely the same, as they are pure calculation logic.


def calculate_payment(principal: int, interest: float, periods: int) -> None:
    payment = math.ceil(
        principal
        * (interest * pow(1 + interest, periods))
        / (pow(1 + interest, periods) - 1)
    )
    overpayment = (payment * periods) - principal
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def calculate_principal(payment: int, interest: float, periods: int) -> None:
    principal = payment / (
        (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)
    )
    overpayment = (payment * periods) - principal
    print(f"Your loan principal = {math.floor(principal)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def calculate_periods(payment: int, interest: float, principal: int) -> None:
    months = math.ceil(
        math.log(payment / (payment - interest * principal), 1 + interest)
    )
    years, remaining_months = divmod(months, 12)
    output_parts = []
    if years > 0:
        output_parts.append(f"{years} year{'s' if years > 1 else ''}")
    if remaining_months > 0:
        output_parts.append(
            f"{remaining_months} month{'s' if remaining_months > 1 else ''}"
        )
    overpayment = (payment * months) - principal
    print("It will take " + " and ".join(output_parts) + " to repay this loan!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def calculate_diff_payment(principal: int, interest: float, periods: int) -> None:
    total_payment = 0
    for month in range(1, periods + 1):
        diff_payment = math.ceil(
            principal / periods
            + interest * (principal - principal * (month - 1) / periods)
        )
        total_payment += diff_payment
        print(f"Month {month}: payment is {diff_payment}")
    print(f"\nOverpayment = {math.ceil(total_payment - principal)}")


# --- Command Handlers ---
# These functions connect the parsed arguments to the calculation logic.


def handle_diff(args: argparse.Namespace) -> None:
    """Handler for the 'diff' command."""
    i = args.interest / (12 * 100)
    calculate_diff_payment(args.principal, i, args.periods)


def handle_annuity(args: argparse.Namespace) -> None:
    """Handler for the 'annuity' command."""
    # The logic to determine which value to calculate is now inside the
    # command handler, making the main function cleaner.
    known_args = [args.payment, args.principal, args.periods]
    if known_args.count(None) != 1:
        # This error should theoretically not be hit if arguments are defined correctly,
        # but it's good practice for robustness.
        print(
            "Error: For annuity, exactly one of --payment, --principal,"
            " or --periods must be omitted.",
            file=sys.stderr,
        )
        sys.exit(1)

    i = args.interest / (12 * 100)

    if args.payment is None:
        calculate_payment(args.principal, i, args.periods)
    elif args.principal is None:
        calculate_principal(args.payment, i, args.periods)
    else:  # args.periods is None
        calculate_periods(args.payment, i, args.principal)


# --- Main Application Logic ---


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A versatile loan calculator.",
        formatter_class=argparse.RawTextHelpFormatter,  # Improves help text formatting
    )
    # Create the sub-parser container
    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # --- 'diff' command parser ---
    parser_diff = subparsers.add_parser(
        "diff", help="Calculate differentiated payments"
    )
    parser_diff.add_argument("--principal", type=non_negative_float, required=True)
    parser_diff.add_argument("--periods", type=non_negative_int, required=True)
    parser_diff.add_argument("--interest", type=non_negative_float, required=True)
    parser_diff.set_defaults(func=handle_diff)  # Link to handler function

    # --- 'annuity' command parser ---
    parser_annuity = subparsers.add_parser("annuity", help="Calculate annuity payments")
    parser_annuity.add_argument("--principal", type=non_negative_float)
    parser_annuity.add_argument("--periods", type=non_negative_int)
    parser_annuity.add_argument("--payment", type=non_negative_float)
    parser_annuity.add_argument("--interest", type=non_negative_float, required=True)
    parser_annuity.set_defaults(func=handle_annuity)  # Link to handler function

    args = parser.parse_args()

    # Call the function that was set by set_defaults()
    args.func(args)


if __name__ == "__main__":
    main()
