from fastapi import HTTPException
import requests

from config import settings

def verify_turnstile(turnstile_token: str = None):
    body = {
        "secret": settings.TURNSTILE_SECRET_KEY,
        "response": turnstile_token,
    }
    r = requests.post("https://challenges.cloudflare.com/turnstile/v0/siteverify", json=body)
    if not r.json()["success"]:
        raise HTTPException(detail=r.json()["error-codes"], status_code=403)

def verify_api_secret(api_secret: str = None):
    if api_secret != "3tmQBbpNbP":
        raise HTTPException(detail="Invalid API secret", status_code=403)