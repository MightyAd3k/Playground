import requests
from bs4 import BeautifulSoup

#date_input = input("Choose which year do you want to travel? Provide date in format: YYYY-MM-DD\n:")

response = requests.get("https://www.billboard.com/charts/hot-100/2022-08-20")
page_with_playlist = response.text

soup = BeautifulSoup(page_with_playlist, "html.parser")
element_with_songs = soup.select(selector="div ul li ul li h3")
titles_list = [title.getText().strip() for title in element_with_songs]
print(titles_list)
