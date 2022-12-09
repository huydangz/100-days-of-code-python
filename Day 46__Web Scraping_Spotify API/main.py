import requests
from bs4 import BeautifulSoup
import spotipy


# ================== Steo 1: Get list songs ============================
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# date = "2002-04-08"
url = f"https://www.billboard.com/charts/hot-100/{date}"
rsp = requests.get(url=url)
soup = BeautifulSoup(rsp.text, "html.parser")
song_names = []
for tag in soup.find_all(name="h3", id="title-of-a-story"):
    if "a-no-trucate" in tag.get("class"):
        song_names.append(tag.getText().replace('\n', '').replace('\t', ''))

# ================= Step 2: Authen with Spotify ========================
sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="3879cdae7dbd46a29ddcbd55ff9f39ea",
        client_secret="46481ef5e20c4f8694b627b8d54ab0d7",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# ================= Step 3: Search and get list song_uri by songs ======================
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_uris.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f'Song: "{song}" does not exist in Spotify. Skipped.')
print(len(song_uris))

# ================== Step 4: Create playlist and add song to playlist ===================
playlist = sp.user_playlist_create(
    user=user_id,
    name=f'{date} Billboard 100',
    public=False
)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
