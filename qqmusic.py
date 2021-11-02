from QQMusicAPI import QQMusic
import sys,os
import pathlib

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(os.path.abspath("."), relative_path)
    return os.path.join(pathlib.Path(__file__).parent.absolute(),relative_path)

def write_lyric(SongName,SingerName,lyric):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(resource_path("lyrics"), filename)
    f = open(pathname, "w",encoding='utf-8')
    f.write(lyric)
    f.close()

def search_lyric_file(SongName,SingerName):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(resource_path("lyrics"), filename)
    try:
        f = open(pathname, "r",encoding='utf-8')
        lyric = f.read()
        return lyric
    except:
        return ""

def search_lyric_byQQ(SongName,SingerName):
    music_list = QQMusic.search(SongName)
    for song in music_list.data:
        if(song.name.lower() == SongName.lower() and song.singer[0].name.lower().__contains__(SingerName.lower())):
            lyric = song.lyric
            lyric.extract()
            if(lyric.lyric != None):
                write_lyric(SongName,SingerName,lyric.lyric) 
                print("搜索成功")
            else:
                write_lyric(SongName,SingerName,"")
                continue
            return lyric.lyric
    print("搜索失敗")
    return ""

def search_lyric_main(SongName,SingerName):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(resource_path("lyrics"), filename)
    print(pathname)
    response = search_lyric_file(SongName,SingerName) if(os.path.isfile(pathname)) else search_lyric_byQQ(SongName,SingerName)
    return response


if __name__ == "__main__":
    print(search_lyric_main('Treasure Pleasure','GRANRODEO'))