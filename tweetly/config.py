from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    feed_url: str = "http://some.feed/url.xml"
    db_url: str = "sqlite:///./tweetly.db"
    shorty_url: str = "http://127.0.0.1:8000/url"
    consumer_key: str = ""
    consumer_secret: str = ""
    access_token: str = ""
    access_token_secret: str = ""
    mastodon_url: str = "https://fosstodon.org"
    mastodon_token: str = ""

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
