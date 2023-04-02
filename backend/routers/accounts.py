from fastapi import APIRouter, Body
from typing import Literal

from database import Session

router = APIRouter(tags=["Accounts"], prefix="/accounts")

@router.get("/instagram")
def get_instagram_accounts(session: Session, filter: Literal["failed"] = None, limit: int = -1, offset: int = 0):
    if filter == "failed":
        return session.lrange("accounts:instagram:failed", offset, limit)
    return session.lrange("accounts:instagram", offset, limit)

@router.post("/instagram")
def add_instagram_accounts(session: Session, body: str = Body(media_type="text/plain")):
    return session.rpush("accounts:instagram", *body.splitlines())