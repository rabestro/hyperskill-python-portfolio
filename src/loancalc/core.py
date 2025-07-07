from math import ceil, log, pow

from .models import LoanInput, LoanResult


def calculate_annuity_payment(inp: LoanInput) -> LoanResult:
    """Calculates the fixed monthly annuity payment."""
    i = inp.interest / (12 * 100)
    compound = pow(1 + i, inp.periods)
    payment = ceil(inp.principal * (i * compound) / (compound - 1))
    overpayment = payment * inp.periods - inp.principal
    return LoanResult(payment=payment, overpayment=overpayment)


def calculate_annuity_principal(inp: LoanInput) -> LoanResult:
    """Calculates the loan principal based on an annuity payment."""
    # principal = payment / (
    #         (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1)
    #     )
    i = inp.interest / (12 * 100)
    compound = pow(1 + i, inp.periods)
    principal = inp.payment / ((i * compound) / (compound - 1))
    overpayment = inp.payment * inp.periods - principal
    return LoanResult(principal=int(principal), overpayment=ceil(overpayment))


def calculate_annuity_periods(inp: LoanInput) -> LoanResult:
    """Calculates the number of periods to repay an annuity loan."""
    i = inp.interest / (12 * 100)
    n = ceil(log(inp.payment / (inp.payment - i * inp.principal), 1 + i))
    years, months = divmod(n, 12)

    parts = []
    if years:
        parts.append(f"{years} year{'s' if years != 1 else ''}")
    if months:
        parts.append(f"{months} month{'s' if months != 1 else ''}")

    description = " and ".join(parts)
    overpayment = inp.payment * n - inp.principal
    return LoanResult(periods=n, overpayment=overpayment, description=description)


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
