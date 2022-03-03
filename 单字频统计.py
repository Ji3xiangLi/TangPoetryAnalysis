from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.pyplot as pyplot
import numpy as np
from wordcloud import WordCloud,STOPWORDS


exword = {'一一', '/', '一', '!', ' ', '，', '。', '：', '（', '）', '？', '！', '(', ')', '·', '\n', '　', '；', '、', '\u3000',
          ' ', '[', ']'}


def read_file(file):
    l = []
    with open(file, 'r', encoding='utf-8') as f:
        for sentense in f:
            l.append(sentense)
    print('wancheng ')
    return l


def clean_note(l):  # 清除原文中包含的括号
    txt = ''
    for r, line in enumerate(l):
        if '（' in line:
            l[r] = line.split('（')[0]
        elif '(' in line:
            l[r] = line.split('(')[0]
        txt += l[r]
    return txt


def clean_word(l):
    for r, word in enumerate(l):
        if word in exword:
            del l[r]
        # else:
        #    for ex in exword:
        #       l[r] = word.strip(ex)


def dic_to_tuple(dic):
    l = []
    for word in dic:
        l.append((dic[word], word))
    l = sorted(l, reverse=True)
    return l


def process_unique_set(s, d):  # 将set生成字典
    l, w, c = [], [], []
    for word in s:
        if len(word) == 1:
            continue
        l.append((d[word], word))

    l = sorted(l, reverse=True)
    for word in l:
        w.append(word[1])
        c.append(word[0])
    return l, w, c


def process_common_set(s, dic1, dic2):
    l, w, c = [], [], []
    for word in s:
        if len(word) == 1:
            continue
        l.append((dic1[word] + dic2[word], word))
    l = sorted(l, reverse=True)
    for word in l:
        w.append(word[1])
        c.append(word[0])
    return l, w, c


def get_count(l, d):
    c = []
    for word in l:
        c.append(d[word[1]])
    return c


def get_single_word(sentence, s):
    # single_word_list = []
    # for sentense in l:
        for zi in sentence:
            if '\u4e00' < zi < '\u9fa5':
                s.append(zi)


def draw_dounct(title,dict,label):
    pyplot.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.rcParams['axes.unicode_minus'] = False

    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    wedges, texts = ax.pie(dict.values(), wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(label[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                    horizontalalignment=horizontalalignment, **kw)

    ax.set_title(title)

    plt.show()

def draw_wordcloud(text,aim_file):
    wc = WordCloud(
        background_color='white',
        font_path="C:/Windows/Fonts/STFANGSO.ttf",
        # stopwords=STOPWORDS.add(stopword),
        width=500,
        height=366,
        margin=2
    ).generate(text)
    # to_file 输出到文件
    wc.to_file(aim_file)



if __name__ == '__main__':
    file_name = 'tang'
    file_dict = {'tang' :'全唐诗','song':'全宋词'}
    file = './doc/{}.txt'.format(file_name)

    text = open(file, 'r', encoding='utf-8').read()
    # pattern = re.compile()

    single_word_list = []
    get_single_word(text, single_word_list)





    # print(single_word_list)
    # clean_word(single_word_list)

    single_word_count = dict(Counter(single_word_list))


    a =sorted(dic_to_tuple(single_word_count),key =  lambda x:x[0],reverse = True)
    print(a[:20])
    single_word = [x[1]for x in a]
    single_count = [x[0] for x in a]


    seasons_dict = {'春': single_word_count['春'], '夏': single_word_count['夏'], '秋': single_word_count['秋'], '冬':single_word_count['冬']}
    seasons_label = list(seasons_dict.keys())
    for i,label in enumerate(seasons_label):
        seasons_label[i] += ':'+ str(seasons_dict[label])

    pyplot.rcParams['font.sans-serif'] = ['SimHei']
    pyplot.rcParams['axes.unicode_minus'] = False
    title = "{}中四季词频统计".format(file_name)
    # draw_dounct(title,seasons_dict,seasons_label)




    plt.figure(figsize=(20, 6))

    plt.bar(single_word[:30], single_count[:30],label=file_name, color='yellow')
    plt.title('{}中出现的高频单字 top30'.format(file_dict[file_name]), fontsize=14)
    plt.show()






