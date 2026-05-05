from litestar import Litestar, MediaType, get, post

from fraud_score import score
from models import FraudScoreRequest


@get("/status", status_code=204)
async def status() -> None:
    return None


@get("/ready", media_type=MediaType.TEXT)
async def ready() -> str:
    return "Up and Running"


@post("/fraud-score")
async def fraud_score(data: FraudScoreRequest) -> dict:
    return score(data)


app = Litestar(route_handlers=[status, ready, fraud_score])
