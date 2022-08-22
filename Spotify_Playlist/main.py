import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

USER_ID = "hljbp90lu97w3m4bbuxz038iq"

#date_input = input("Choose which year do you want to travel? Provide date in format: YYYY-MM-DD\n:")

response = requests.get("https://www.billboard.com/charts/hot-100/2022-08-20")
page_with_playlist = response.text

soup = BeautifulSoup(page_with_playlist, "html.parser")
element_with_songs = soup.select(selector="div ul li ul li h3")
titles_list = [title.getText().strip() for title in element_with_songs]
print(titles_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="5357f52de3074e29847d7da56afbc6f3",
        client_secret="42eedc90a8024555b41e43cc73d41eef",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]