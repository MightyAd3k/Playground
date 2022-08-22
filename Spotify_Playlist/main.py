import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#date_input = input("Choose which year do you want to travel? Provide date in format: YYYY-MM-DD\n:")
year = 2022

response = requests.get("https://www.billboard.com/charts/hot-100/2022-08-20")
page_with_playlist = response.text

soup = BeautifulSoup(page_with_playlist, "html.parser")
element_with_songs = soup.select(selector="div ul li ul li h3")
titles_list = [title.getText().strip() for title in element_with_songs]

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "http://example.com",
        client_id = os.environ['CLIENT_ID'],
        client_secret = os.environ['CLIENT_SECRET'],
        show_dialog = True,
        cache_path = "token.txt"
    )
)

user_id = sp.current_user()["id"]


songs_uris = []
for title in titles_list:
    song = sp.search(q=f"track:{title} year:{year}", type="track")

    try:
        uri = song['tracks']['items'][0]['uri']
        songs_uris.append(uri)
    except IndexError:
        print(f"No songs found for track: {title}")

print(songs_uris)