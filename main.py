import win32com.client
import time
from qqmusic import *
from lrc import *
from tkmusic import *

itunes = win32com.client.gencache.EnsureDispatch("iTunes.Application")

mainLibrary = itunes.LibraryPlaylist

def get_track(track):
    try:
        Track = win32com.client.CastTo(itunes.CurrentTrack, 'IITTrack')
        track['position'] = itunes.PlayerPosition
        if(track['track_name'] != Track.Name):
            track['track_artist'] = Track.Artist
            track['track_name'] = Track.Name
            lyrics_incode = search_lyric_main(track['track_name'], track['track_artist'])
            lyrics_decode = decode_lrc(lyrics_incode)
            track['lyrics'] = convert_lrc(lyrics_decode)
        return track
    except:
        update_label("沒有播放音樂")
        return track

def main(): 
    while(True):
        track_dict = get_track( {'position':0, 'track_artist':"", 'track_name':"", 'lyrics':""} )
        if(not track_dict['lyrics']):
            update_label("")
        while(track_dict['lyrics']):
            track_dict = get_track(track_dict) or track_dict
            time.sleep(0.5)
            for index,(lyrics_time,lyrics) in enumerate(track_dict['lyrics']):
                if(index+1 < len(track_dict['lyrics'])):
                    nxt_lyric = track_dict['lyrics'][index+1]
                else:
                    break
                if(nxt_lyric[0] > track_dict['position']):
                    try:
                        lyrics_tk_used = get_label_value()
                        lyrics_tk = f'{lyrics}\n{nxt_lyric[1]}'
                        if(lyrics_tk != lyrics_tk_used):
                            update_label(lyrics_tk)
                            lyrics_tk_used = lyrics_tk
                        break
                    except:
                        break         
        

if __name__ == "__main__":
    window.after(1,main)
    window.mainloop()