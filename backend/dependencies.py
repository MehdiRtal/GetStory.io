from fastapi import Request, HTTPException
import requests

from config import settings

def verify_turnstile(request: Request, turnstile_token: str = None):
    params = {
        "secret": settings.TURNSTILE_SECRET_KEY,
        "url": turnstile_token,
        "remoteip": request.client.host,
    }
    r = requests.post("https://challenges.cloudflare.com/turnstile/v0/siteverify", params=params)
    if r.status_code != 200:
        raise HTTPException(detail=r.json()["error-codes"], status_code=403)