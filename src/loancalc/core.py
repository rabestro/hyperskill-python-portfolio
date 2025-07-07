from math import ceil, log, pow

from .models import LoanInput, LoanResult

MONTHS_IN_YEAR = 12


def calculate_annuity_payment(
    interest: float, periods: int, principal: int
) -> LoanResult:
    """Calculates the fixed monthly annuity payment."""
    compound = pow(1 + interest, periods)
    payment = ceil(principal * (interest * compound) / (compound - 1))
    overpayment = payment * periods - principal
    return LoanResult(payment=payment, overpayment=overpayment)


def calculate_annuity_principal(
    interest: float, periods: int, payment: int
) -> LoanResult:
    """Calculates the loan principal based on an annuity payment."""
    compound = pow(1 + interest, periods)
    principal = payment / ((interest * compound) / (compound - 1))
    overpayment = payment * periods - principal
    return LoanResult(principal=int(principal), overpayment=ceil(overpayment))


def calculate_annuity_periods(
    interest: float, principal: int, payment: int
) -> LoanResult:
    """Calculates the number of periods to repay an annuity loan."""
    periods = ceil(log(payment / (payment - interest * principal), 1 + interest))
    years, months = divmod(periods, MONTHS_IN_YEAR)

    parts = []
    if years:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months:
        parts.append(f"{months} month{'s' if months != 1 else ''}")

    description = " and ".join(parts)
    overpayment = payment * periods - principal
    return LoanResult(periods=periods, overpayment=overpayment, description=description)


def calculate_diff(inp: LoanInput) -> LoanResult:
    """Calculates all monthly payments for a differentiated loan."""
    i = inp.interest / (12 * 100)
    total_payment = 0
    payments: list[int] = []

    for m in range(1, inp.periods + 1):
        # Simplified the formula for clarity
        principal_paid = inp.principal * (m - 1) / inp.periods
        remaining_principal = inp.principal - principal_paid

        diff_payment = ceil((inp.principal / inp.periods) + (i * remaining_principal))

        payments.append(diff_payment)
        total_payment += diff_payment

    overpayment = total_payment - inp.principal
    return LoanResult(payments=payments, overpayment=overpayment)
