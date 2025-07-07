from dataclasses import dataclass


@dataclass
class LoanInput:
    principal: int | None = None
    payment: int | None = None
    periods: int | None = None
    interest: float = 0.0


@dataclass
class LoanResult:
    payments: list[int] | None = None
    payment: int | None = None
    periods: int | None = None
    principal: int | None = None
    overpayment: int = 0
    description: str | None = None
