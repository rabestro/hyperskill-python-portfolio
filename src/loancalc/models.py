from dataclasses import dataclass, field


@dataclass
class LoanResult:
    payments: list[int] = field(default_factory=list)
    payment: int | None = None
    periods: int | None = None
    principal: int | None = None
    overpayment: int = 0
    description: str | None = None
