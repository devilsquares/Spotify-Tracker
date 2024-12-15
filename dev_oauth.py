import json
from typing import Annotated
from urllib.parse import urlencode
import os

from fastapi import FastAPI, Query
import requests

SPOTIFY_REDIRECT_URI = "http://localhost:8000/spotify-authenticated"

with open("spotify-credentials.json", "r") as spotify_credentials_file:
    spotify_credentials = json.load(spotify_credentials_file)

    SPOTIFY_CLIENT_ID: str = spotify_credentials["client_id"]
    SPOTIFY_CLIENT_SECRET: str = spotify_credentials["client_secret"]


def build_spotify_redirect_url() -> str:
    url = "https://accounts.spotify.com/authorize"
    scopes = ["user-read-recently-played", "user-top-read", "user-read-playback-position"]

    params = {
        "response_type": "code",
        "client_id": SPOTIFY_CLIENT_ID,
        "scope": " ".join(scopes),
        "redirect_uri": SPOTIFY_REDIRECT_URI,
    }

    return f"{url}?{urlencode(params)}"


async def lifespan(app: FastAPI):
    print(build_spotify_redirect_url())
    os.system(f"open \"{build_spotify_redirect_url()}\"")

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/spotify-authenticated")
def spotify_authenticated_callback(code: Annotated[str, Query()]):
    token_response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "code": code,
            "redirect_uri": SPOTIFY_REDIRECT_URI,
            "grant_type": "authorization_code",
            "client_id": SPOTIFY_CLIENT_ID,
            "client_secret": SPOTIFY_CLIENT_SECRET,
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )

    with open('spotify-oauth-response.json', 'w+') as spotify_oauth_response_file:
        json.dump(token_response.json(), spotify_oauth_response_file, indent=4)

    return "Success! Saved credentials to file: spotify-oauth-response.json"


