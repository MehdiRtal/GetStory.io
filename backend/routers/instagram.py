from fastapi import APIRouter, HTTPException, status, Depends
from instagram import Instagram, UserIsPrivate
from instagrapi.exceptions import UserNotFound, MediaNotFound, PrivateError, ChallengeError
from pydantic import constr, AnyUrl
import random
import re

from dependencies import verify_turnstile
from database import Session


router = APIRouter(tags=["Instagram"], prefix="/instagram", dependencies=[Depends(verify_turnstile)])

@router.get("/post")
def get_post(url: AnyUrl, session: Session):
    accounts = session.lrange("accounts:instagram", 0, -1)
    proxies = session.lrange("proxies", 0, -1)
    for account in accounts:
        try:
            proxy = random.choice(proxies) if not "||" in account else account.split("||")[1]
            ig = Instagram(proxy=proxy, authorization=re.findall(r"Authorization=(.*?);", account)[0])
            posts = ig.get_post(url)
        except MediaNotFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Media not found")
        except (PrivateError, ChallengeError):
            print("[FAILED]", account.split("|")[0])
            session.lrem("accounts:instagram", 0, account)
            session.rpush("accounts:instagram:failed", account)
        else:
            print("[SUCCESS]", account.split("|")[0])
            session.lrem("accounts:instagram", 0, account)
            if not "||" in account:
                account = f"{account}||{proxy}"
            session.rpush("accounts:instagram", account)
            return posts

@router.get("/stories")
def get_stories(username: constr(regex="^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$"), session: Session):
    accounts = session.lrange("accounts:instagram", 0, -1)
    proxies = session.lrange("proxies", 0, -1)
    for account in accounts:
        try:
            proxy = random.choice(proxies) if not "||" in account else account.split("||")[1]
            ig = Instagram(proxy=proxy, authorization=re.findall(r"Authorization=(.*?);", account)[0])
            user_id = ig.get_user_id(username)
        except UserIsPrivate:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is private")
        except UserNotFound:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        except (PrivateError, ChallengeError):
            print("[FAILED]", account.split("|")[0])
            session.lrem("accounts:instagram", 0, account)
            session.rpush("accounts:instagram:failed", account)
        else:
            print("[SUCCESS]", account.split("|")[0])
            session.lrem("accounts:instagram", 0, account)
            if not "||" in account:
                account = f"{account}||{proxy}"
            session.rpush("accounts:instagram", account)
            stories = ig.get_stories(user_id)
            if not stories:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User has no stories")
            return {"status": "success", "stories": stories}