import jieba
from wordcloud import WordCloud,STOPWORDS
import numpy as np
from PIL import Image
# image= np.array(Image.open('./img/1.jpg'))
wc = WordCloud(background_color='white',
               max_words=1000,
               max_font_size=100,
                # mask=image,
               font_path='C:\Windows\Fonts\STXINGKA.TTF',
               random_state=42,
               )
text = open('./doc/JieTang.txt', encoding='utf-8').read()
# text = open('./doc/song.txt', encoding='utf-8').read()
def stop_words(texts):
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)
    for word in word_generator:
        words_list.append(word)

    return ' '.join(words_list)
# text = stop_words(text)
wc.generate(text)

wc.to_file('./img/tang.png')
