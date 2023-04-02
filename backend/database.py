from fastapi import Depends
from redis import from_url, Redis
from typing import Annotated

from config import settings

def get_session():
    with from_url(settings.REDIS_URL, decode_responses=True) as session:
        yield session

Session = Annotated[Redis, Depends(get_session)]