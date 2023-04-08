from fastapi import APIRouter, Body
from typing import Literal

from database import Session

router = APIRouter(tags=["Proxies"], prefix="/proxies")

@router.get("/")
def get_proxies(session: Session, filter: Literal["failed"] = None, limit: int = -1, offset: int = 0):
    if filter == "failed":
        return session.lrange("proxies:failed", offset, limit)
    return session.lrange("proxies", offset, limit)

@router.post("/")
def add_proxies(session: Session, body: str = Body(media_type="text/plain")):
    return session.rpush("proxies", *body.splitlines())