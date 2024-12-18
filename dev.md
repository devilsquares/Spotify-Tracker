# Development Instructions
## Running `dev_oauth.py` / Getting User Credentials For Dev
1. Install the project with `poetry install`
2. Put your Spotify client ID & secret into `spotify-credentials.json` (You can get these from the Spotify developer dashboard)
  - Ex: `{"client_id": "...", "client_secret": "..."}
3. Run the following command to run the dev server: `poetry run fastapi dev dev_oauth.py`
4. A web browser should be opened automatically, then log in
5. The credentials will be saved in `spotify-oauth-response.json`