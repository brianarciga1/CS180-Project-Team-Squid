from addSong import addSong

from rq.worker import Worker

def background_task(form, themes, add_song):
    playlist_ID = add_song.create_list(form['playlistTitle'], form['playlistDesc'])
    add_song.add_Song(add_song.search(themes.get_themes(form)))
    return playlist_ID
