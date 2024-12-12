import requests
token = "BQCrGjgbvnVv363SumfTTrF42NvzCBwkNqnGROD5heiew6umRvl0UiCGGxKHLt_BNGMWoPa3SSoaFEzhI6EduQcXnq8p0uhtzXBvMDJ-JQz-KJ-x1HcQk_lnd8yMEP26NoN1D0E_CqOFzGh5USpDD6YhASgBpcua7-EcrPc0okBYs5cNf45rep8kjbtN2GJeEhGDe7Zyc5st_DERiieqOzg5zSIzhoqI1KDlXbTUJSKHMadmzkFv-j0wCUUg3D87s4F_PUKsJwQ-RA0SPFgEaK2lqj6yFT2l"
headers = {"Authorization": f"Bearer {token}"}
response = requests.get("https://api.spotify.com/v1/me/player/recently-played/", headers=headers)
data = response.json()
print(data)
print("Your recent 50 tracks on Spotify:")
for index, track in enumerate(data['items'], start=1):
    track_name = track['name']
    artists = ", ".join(artist['name'] for artist in track['artists'])
    print(f"{index}: {track_name} by {artists}")
#milo wants me to ; for each item (song), print out it's ranking number. (1. name of the song, 2. NOTS)(bonus is print the artwork)
#figure out how to get the most recently listened to 50 tracks