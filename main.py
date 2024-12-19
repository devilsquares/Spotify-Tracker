import requests
import json
with open("spotify-oauth-response.json", "r") as file:
    file_contents = file.read()
    print(file_contents)
oauth_data = json.loads(file_contents)
token = oauth_data["access_token"]

headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://api.spotify.com/v1/me/player/recently-played/", headers=headers)
data = response.json()
print(data)
print("Your recent 50 tracks on Spotify:")
for index, track in enumerate(data["items"], start=1):
    track_name = track["name"]
    artists = ", ".join(artist["name"] for artist in track["artists"])
    print(f"{index}: {track_name} by {artists}")
#milo wants me to ; for each item (song), print out it"s ranking number. (1. name of the song, 2. NOTS)(bonus is print the artwork)
#figure out how to get the most recently listened to 50 tracks
