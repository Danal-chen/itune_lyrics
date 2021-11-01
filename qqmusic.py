from QQMusicAPI import QQMusic

import sys,os

def write_lyric(SongName,SingerName,lyric):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lyrics", filename)
    f = open(pathname, "w",encoding='utf-8')
    f.write(lyric)
    f.close()

def search_lyric_file(SongName,SingerName):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lyrics", filename)
    try:
        f = open(pathname, "r",encoding='utf-8')
        lyric = f.read()
        return lyric
    except:
        return False

def search_lyric_byQQ(SongName,SingerName):
    music_list = QQMusic.search(SongName)
    for song in music_list.data:
        if(song.name == SongName and song.singer[0].name.__contains__(SingerName)):
            lyric = song.lyric
            lyric.extract()
            if(lyric.lyric != None):
                write_lyric(SongName,SingerName,lyric.lyric) 
                print("搜索成功")
            else:
                continue
            return lyric.lyric
    print("搜索失敗")
    return ""

def search_lyric_main(SongName,SingerName):
    filename = SongName + '_' + SingerName + '.lrc'
    pathname = os.path.join(os.path.dirname(os.path.realpath(__file__)), "lyrics", filename)
    response = search_lyric_file(SongName,SingerName) if(os.path.isfile(pathname)) else search_lyric_byQQ(SongName,SingerName)
    return response


if __name__ == "__main__":
    print(search_lyric_main('Treasure Pleasure','GRANRODEO'))