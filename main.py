import win32com.client
import time
from qqmusic import *
from lrc import *
from tkmusic import *

itunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")

mainLibrary = itunes.LibraryPlaylist
Track = win32com.client.CastTo(itunes.CurrentTrack, 'IITTrack')
track_converted = win32com.client.CastTo(Track, "IITFileOrCDTrack")

track_artist = Track.Artist
track_name = Track.Name

lyrics_incode = search_lyric_main(track_name, track_artist)
lyrics_decode = decode_lrc(lyrics_incode)

lyrics = convert_lrc(lyrics_decode)


def main():
    global track_name,track_artist,lyrics
    lyrics_tk_tmp = ""
    while(True):
        Track = win32com.client.CastTo(itunes.CurrentTrack, 'IITTrack')
        if(track_name != Track.Name):
            track_name = Track.Name
            track_artist = Track.Artist
            lyrics_incode = search_lyric_main(track_name, track_artist)
            lyrics_decode = decode_lrc(lyrics_incode)
            lyrics = convert_lrc(lyrics_decode)
            if(lyrics_incode == ""):
                update_label("")
        time.sleep(0.5)
        position = itunes.PlayerPosition
        for i in range(len(lyrics)-1):
            if(lyrics[i+1][0] > position):
                try:
                    lyrics_tk = f'{lyrics[i][1]}\n{lyrics[i+1][1]}'
                    if(lyrics_tk != lyrics_tk_tmp):
                        update_label(lyrics_tk)
                        lyrics_tk_tmp = lyrics_tk
                    break
                except:
                    break

window.after(1,main)
window.mainloop()