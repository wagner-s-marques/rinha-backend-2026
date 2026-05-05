from msgspec import Struct


class Transaction(Struct):
    amount: float
    installments: int
    requested_at: str


class Customer(Struct):
    avg_amount: float
    tx_count_24h: int
    known_merchants: list[str]


class Merchant(Struct):
    id: str
    mcc: str
    avg_amount: float


class Terminal(Struct):
    is_online: bool
    card_present: bool
    km_from_home: float


class LastTransaction(Struct):
    timestamp: str
    km_from_current: float


class FraudScoreRequest(Struct):
    id: str
    transaction: Transaction
    customer: Customer
    merchant: Merchant
    terminal: Terminal
    last_transaction: LastTransaction | None = None
