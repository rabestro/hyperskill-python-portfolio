from loancalc.core import (
    calculate_annuity_payment,
    calculate_annuity_periods,
    calculate_annuity_principal,
    calculate_diff,
)
from loancalc.models import LoanInput


def test_annuity_payment():
    """Tests the calculation of a fixed monthly annuity payment."""
    res = calculate_annuity_payment(
        LoanInput(principal=1000000, periods=12, interest=10)
    )
    assert res.payment == 87916
    assert res.overpayment == 54992


def test_annuity_principal():
    """Tests the calculation of the loan principal for an annuity loan."""
    res = calculate_annuity_principal(
        LoanInput(payment=8722, periods=120, interest=5.6)
    )
    assert res.principal == 800018
    assert res.overpayment == 246622


def test_annuity_periods():
    """Tests the calculation of the repayment period for an annuity loan."""
    res = calculate_annuity_periods(
        LoanInput(principal=500000, payment=23000, interest=7.8)
    )
    assert res.periods == 24
    assert "year" in res.description
    assert res.overpayment == 52000


def test_diff():
    """Tests the calculation of differentiated payments."""
    res = calculate_diff(LoanInput(principal=1000000, periods=10, interest=10))
    assert len(res.payments) == 10
    assert res.payments[0] > res.payments[-1]
    assert res.overpayment == sum(res.payments) - 1000000
