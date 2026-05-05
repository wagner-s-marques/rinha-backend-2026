import json
from datetime import datetime
from pathlib import Path

from models import FraudScoreRequest

_RES = Path(__file__).parent / "resources"
_NORM = json.loads((_RES / "normalization.json").read_text())
_MCC_RISK = json.loads((_RES / "mcc_risk.json").read_text())


def _clamp(x: float) -> float:
    return min(max(x, 0.0), 1.0)


def embed(body: FraudScoreRequest) -> list[float]:
    tx = body.transaction
    cust = body.customer
    merch = body.merchant
    term = body.terminal
    last = body.last_transaction
    requested_at = datetime.fromisoformat(tx.requested_at)

    if last is None:
        minutes_since = -1.0
        km_from_last = -1.0
    else:
        delta_min = (requested_at - datetime.fromisoformat(last.timestamp)).total_seconds() / 60
        minutes_since = _clamp(delta_min / _NORM["max_minutes"])
        km_from_last = _clamp(last.km_from_current / _NORM["max_km"])

    return [
        _clamp(tx.amount / _NORM["max_amount"]),
        _clamp(tx.installments / _NORM["max_installments"]),
        _clamp((tx.amount / cust.avg_amount) / _NORM["amount_vs_avg_ratio"]),
        requested_at.hour / 23,
        requested_at.weekday() / 6,
        minutes_since,
        km_from_last,
        _clamp(term.km_from_home / _NORM["max_km"]),
        _clamp(cust.tx_count_24h / _NORM["max_tx_count_24h"]),
        1.0 if term.is_online else 0.0,
        1.0 if term.card_present else 0.0,
        0.0 if merch.id in cust.known_merchants else 1.0,
        _MCC_RISK.get(merch.mcc, 0.5),
        _clamp(merch.avg_amount / _NORM["max_merchant_avg_amount"]),
    ]


def score(body: FraudScoreRequest) -> dict:
    vec = embed(body)
    print(vec, flush=True)
    return {"approved": False, "fraud_score": 0.8}
