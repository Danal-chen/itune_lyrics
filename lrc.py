import sys,os
from qqmusic import search_lyric_file

def decode_lrc(lyric):
    lrc_list = lyric.split("\n")
    lrc_dict = {}
    for i in lrc_list:
        lrc_word = i.replace("[", "]").strip().split("]")
        for j in range(len(lrc_word) - 1):
            if lrc_word[j]:
                lrc_dict[lrc_word[j]] = lrc_word[-1]
    return lrc_dict

def convert_lrc(lrc_dict):
    ftr = [60,1]
    lrc_list = []
    for key in sorted(lrc_dict.keys()):
        try:
            if(lrc_dict[key] == ""):
                continue
            lrt_sec = sum([a*b for a,b in zip(ftr, map(float,key.split(':')))])
            lrc_list.append([lrt_sec, lrc_dict[key]])
        except:
            continue
    return lrc_list

if __name__ == "__main__":
    lrc_dict = decode_lrc(search_lyric_file('orion','米津玄師'))
    print(convert_lrc(lrc_dict))