
# WordDivideClean中分好并且清洗好的文本进行分析，画图
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplot
import numpy as np




def dic_to_tuple(dic):
    l = []
    for word in dic:
        l.append((dic[word],word))
    l =sorted(l,reverse = True)
    return l

def process_unique_set(s,d): #将set生成字典
    l,w,c = [],[],[]
    for word in s:
        if len(word) == 1:
            continue
        l.append((d[word],word))

    l = sorted(l,reverse = True)
    for word in l:
        w.append(word[1])
        c.append(word[0])
    return l,w,c

def process_common_set(s,dic1, dic2):
    l,w,c = [],[],[]
    for word in s:
        if len(word) ==1:
            continue
        l.append((dic1[word]+dic2[word], word))
    l = sorted(l,reverse = True)
    for word in l:
        w.append(word[1])
        c.append(word[0])
    return l, w, c

def get_count(l,d):
    c = []
    for word in l:
        c.append(d[word[1]])
    return c
if __name__ == '__main__':

    tang_list = open('./doc/JieTang.txt','r',encoding='utf-8').read().split()
    song_list = open('./doc/JieSong.txt', 'r', encoding='utf-8').read().split()

    tang_dic = dict(Counter(tang_list))
    song_dic = dict(Counter(song_list))

    tang_set = set(tang_list)
    song_set = set(song_list)

    tang_list = dic_to_tuple(tang_dic)
    song_list = dic_to_tuple(song_dic)
    #print(song_list[:20])

    common_set = tang_set & song_set
    tang_unique_set = tang_set-common_set
    song_unique_set = song_set-common_set

    tang_unique_list,tang_word_list,tang_word_count = process_unique_set(tang_unique_set,tang_dic)
    song_unique_list,song_word_list,song_word_count = process_unique_set(song_unique_set, song_dic)

    common_list,common_word_list,common_word_count = process_common_set(common_set,tang_dic, song_dic)
    # common_list,  common_li_word_list,  common_li_word_count = process_unique_set(common_set, li_dic)
    # common_list, common_song_word_list, common_song_word_count = process_unique_set(common_set, song_dic)
    common_tang_word_count = get_count(common_list,tang_dic)
    common_song_word_count = get_count(common_list,song_dic)

    print(common_list[:20])
    print(common_word_list[:20])


    # print(sorted(tang_dic, reverse = True)[:20])
    # print(sorted(song_dic, reverse =True)[:20])

    '''画图'''
    num = 30
    pyplot.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.rcParams['axes.unicode_minus'] = False
    # plt.figure(figsize=(20, 6))

    plt.bar(tang_word_list[:num],tang_word_count[:num], label='全唐诗', color='yellow')
    plt.title('全唐诗单独出现的高频词 top{}'.format(num), fontsize=14)
    plt.show()

    plt.bar(song_word_list[:num],song_word_count[:num], label='全宋词', color='orange')
    plt.title('全宋词单独出现的高频词 top{}'.format(num), fontsize=14)
    plt.show()

    labels = common_word_list[:num]
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, common_tang_word_count[:num], width, label='唐诗')
    rects2 = ax.bar(x + width / 2, common_song_word_count[:num], width, label='宋词')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('出现次数')
    ax.set_title('唐诗宋词共同词频统计top {}'.format(num))
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()
    plt.show()
