import json
from addSong import addSong
from getThemes import getThemes
from getMALtoken import getMALtoken
from getSptoken import get_sp_token

get_mal_token = getMALtoken()
get_mal_token.get_token()

get_SP_token = get_sp_token()
get_SP_token.get_sp_token()

themes = getThemes()
themes.open_token()
opseds = themes.get_themes()
print(opseds)

add_song=addSong()
add_song.open_token()
add_song.create_list()
add_song.add_Song(add_song.search(opseds))
