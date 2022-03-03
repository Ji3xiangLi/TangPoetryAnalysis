#将唐诗和宋词分别进行jieba分词，由于文本量大分词时间很长，所以将分词和清洗好以后的结果放到./doc/JieTang.txt 和./doc/JieSong.txt

import jieba


exword = { '一一','/', '一','!',' ','，','。','：','（','）','？','！','(',')','·','\n','　','；','、','\u3000',' '}


def read_file(file):
    with open(file,'r',encoding='utf-8') as f:
        l = f.read()
    return l

def clean_word(l):
    for r,word in enumerate(l):
        print((r/len(l) * 100))
        if word in exword or len(word) == 1:
            del l[r]
        else:
            for ex in exword:
                l[r] = word.strip(ex)


tang_txt = read_file('./doc/tang.txt')
song_txt = read_file('./doc/song.txt')

tang_list = jieba.lcut(tang_txt)     #此时list中包含可jieba分词以后的结果，都是一个个词
song_list = jieba.lcut(song_txt)
# print(tang_list[:20])
print(len(tang_list))

clean_word(tang_list)
clean_word(song_list)

with open('./doc/JieTang.txt','w',encoding='utf-8') as f:
    for word in tang_list:
        f.write(word)
        f.write('  ')

with open('./doc/JieSong.txt','w',encoding='utf-8') as f:
    for word in song_list:
        f.write(word)
        f.write('  ')