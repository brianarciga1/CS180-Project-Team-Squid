from scrape import UrlManager
import json
from getMALid import getMALid
from addAnime import addAnime
from addSong import addSong

url = "https://www.crunchyroll.com/watch/GRMGQX55R/izuku-midoriya-origin"
url1 ="https://www.crunchyroll.com/watch/G4VUQZ7MX/the-new-threat"
url2 = "https://tubitv.com/tv-shows/395405/s01-e01-end-and-beginning?start=true"


urls=[]
urls.append(url)
urls.append(url1)
get_id = getMALid()
get_id.ID=get_id.get_ID(urls)

add_anime=addAnime()
add_anime.open_token()
add_anime.addAnime(get_id.ID)

ops = add_anime.get_op_ed()[0]
eds =add_anime.get_op_ed()[1] 
print(ops)
print(eds)

add_song=addSong()
add_song.open_token()
add_song.create_list()