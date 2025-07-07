import argparse
import math
import sys

# --- Custom Types for Validation ---


def non_negative_float(value: str) -> float:
    """
    Parse a string as a non-negative float for argument validation.
    
    Raises:
        argparse.ArgumentTypeError: If the value cannot be converted to float or is negative.
    
    Returns:
        float: The parsed non-negative float value.
    """
    try:
        f_value = float(value)
    except ValueError:
        # Raise the new exception, suppressing the original ValueError context.
        raise argparse.ArgumentTypeError(f"invalid float value: '{value}'") from None
    if f_value < 0:
        raise argparse.ArgumentTypeError(f"value must be non-negative: {f_value}")
    return f_value


def non_negative_int(value: str) -> int:
    """
    Parse a string as a non-negative integer for argument validation.
    
    Raises:
        argparse.ArgumentTypeError: If the value is not a valid integer or is negative.
    
    Returns:
        int: The parsed non-negative integer.
    """
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
    """
    Calculate and display the monthly annuity payment and overpayment for a loan.
    
    Parameters:
        principal (int): The initial loan amount.
        interest (float): The monthly interest rate as a decimal (e.g., 0.01 for 1%).
        periods (int): The total number of monthly payments.
    
    Prints:
        The calculated monthly payment (rounded up) and the total overpayment.
    """
    payment = math.ceil(
        principal
        * (interest * pow(1 + interest, periods))
        / (pow(1 + interest, periods) - 1)
    )
    overpayment = (payment * periods) - principal
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def calculate_principal(payment: int, interest: float, periods: int) -> None:
    """
    Calculate and display the loan principal based on monthly payment, interest rate, and number of periods.
    
    Prints the calculated principal (rounded down) and the overpayment (rounded up).
    """
    principal = payment / (
        (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)
    )
    overpayment = (payment * periods) - principal
    print(f"Your loan principal = {math.floor(principal)}!")
    print(f"Overpayment = {math.ceil(overpayment)}")


def calculate_periods(payment: int, interest: float, principal: int) -> None:
    """
    Calculate and display the number of months required to repay a loan given the monthly payment, interest rate, and principal.
    
    Prints the repayment duration in years and months, as well as the total overpayment.
    """
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
    """
    Calculate and print the differentiated monthly payments for a loan, along with the total overpayment.
    
    Parameters:
        principal (int): The initial loan amount.
        interest (float): The monthly interest rate as a decimal (e.g., 0.01 for 1%).
        periods (int): The total number of monthly payments.
    
    Each month's payment is calculated and printed individually. After all payments, the function prints the total overpayment compared to the principal.
    """
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
    """
    Handles the 'diff' command by converting the annual interest rate to a monthly rate and calculating differentiated loan payments.
    
    Parameters:
        args (argparse.Namespace): Parsed command-line arguments containing principal, periods, and interest.
    """
    i = args.interest / (12 * 100)
    calculate_diff_payment(args.principal, i, args.periods)


def handle_annuity(args: argparse.Namespace) -> None:
    """
    Handles the 'annuity' command by determining and calculating the missing loan parameter (payment, principal, or periods) based on provided arguments.
    
    Validates that exactly one of payment, principal, or periods is omitted, converts the annual interest rate to a monthly rate, and invokes the appropriate calculation function. Exits with an error if argument validation fails.
    """
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
    """
    Entry point for the loan calculator CLI application.
    
    Sets up command-line argument parsing for differentiated and annuity loan calculations, validates input, and dispatches to the appropriate calculation handler based on user input.
    """
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
