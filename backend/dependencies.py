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

def verify_password(password: str = None):
    if password != "shady@@321":
        raise HTTPException(detail="Invalid password", status_code=403)