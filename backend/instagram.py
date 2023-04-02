from instagrapi import Client
from instagrapi.exceptions import UserError
from datetime import datetime, timezone


class UserIsPrivate(UserError):
    pass


class Instagram:
    def __init__(self, proxy=None, authorization=None, session_id=None, settings=None):
        if settings:
            self.ig = Client(proxy=f"http://{proxy}" if proxy else None, settings=settings)
        else:
            self.ig = Client(proxy=f"http://{proxy}" if proxy else None)
        if authorization:
            self.ig.private.headers.update({"Authorization": authorization})            
        if session_id:
            self.ig.login_by_sessionid(session_id)

    def get_user_id(self, username):
        user = self.ig.user_info_by_username_v1(username)
        if user.is_private:
            raise UserIsPrivate
        return user.pk

    def get_stories(self, user_id):
        stories = []
        media = self.ig.user_stories_v1(user_id)
        for story in media:
            if story.media_type == 1:
                stories.append({"type": "Image", "added": datetime.now(timezone.utc) - story.taken_at, "thumbnail": story.thumbnail_url, "url": story.thumbnail_url})
            else:
                stories.append({"type": "Video", "added": datetime.now(timezone.utc) - story.taken_at, "duration": story.video_duration, "thumbnail": story.thumbnail_url, "url": story.video_url})
        return stories

    def get_post(self, url):
        posts = []
        media_pk = self.ig.media_pk_from_url(url)
        media = self.ig.media_info_v1(media_pk)
        if media.media_type == 1:
            posts.append({"media": media.thumbnail_url, "type": "Image", "thumbnail": media.thumbnail_url})
        elif media.media_type == 8:
            for resource in media.resources:
                if resource.media_type == 2:
                    posts.append({"media": resource.video_url, "type": "Video", "thumbnail": resource.thumbnail_url})
                else:
                    posts.append({"media": resource.thumbnail_url, "type": "Image", "thumbnail": resource.thumbnail_url})
        else:
            posts.append({"media": media.video_url, "type": "Video", "thumbnail": media.thumbnail_url})
        return posts