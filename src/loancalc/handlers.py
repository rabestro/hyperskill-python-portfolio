import sys

from loancalc.core import (
    calculate_annuity_payment,
    calculate_annuity_periods,
    calculate_annuity_principal,
    calculate_diff,
)
from loancalc.models import LoanInput


def handle_annuity(args) -> None:
    """
    Handles the 'annuity' command.

    Validates arguments, dispatches to the correct annuity calculation function,
    and prints the result.
    """
    known = [args.principal, args.payment, args.periods]
    if known.count(None) != 1:
        print(
            "Error: Exactly one of --principal, "
            "--payment, or --periods must be omitted.",
            file=sys.stderr,
        )
        sys.exit(1)

    input_data = LoanInput(
        principal=args.principal,
        payment=args.payment,
        periods=args.periods,
        interest=args.interest,
    )
    interest = args.interest / (12 * 100)
    if args.payment is None:
        result = calculate_annuity_payment(interest, args.periods, args.principal)
        print(f"Your monthly payment = {result.payment}!")
    elif args.principal is None:
        result = calculate_annuity_principal(interest, args.periods, args.payment)
        print(f"Your loan principal = {result.principal}!")
    else:  # args.periods is None
        result = calculate_annuity_periods(input_data)
        print(f"It will take {result.description} to repay this loan!")

    print(f"Overpayment = {result.overpayment}")


def handle_diff(args) -> None:
    """

    Handles the 'diff' (differentiated) command.

    Validates arguments, calls the differentiated calculation function,
    and prints the monthly payments and total overpayment.
    """
    if args.payment is not None:
        print(
            "Error: --payment is not allowed with 'diff' calculation mode.",
            file=sys.stderr,
        )
        sys.exit(1)

    input_data = LoanInput(
        principal=args.principal,
        periods=args.periods,
        interest=args.interest,
    )

    result = calculate_diff(input_data)
    for month, payment in enumerate(result.payments, start=1):
        print(f"Month {month}: payment is {payment}")
    print(f"\nOverpayment = {result.overpayment}")
