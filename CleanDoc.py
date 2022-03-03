import re

file = './doc/全唐诗.txt'
text = open(file,'r',encoding='utf-8').readlines()
new_text = ''
with open('./doc/tang.txt','w',encoding='utf-8')as f:
    for line in text:
        if '◎' not in line and re.search('第.*卷',line) == None:
                f.write(line.split('-')[0])


file = './doc/全宋词.txt'
text = open(file,'r',encoding='utf-8').read()
text_list = text.split('""')
new_text = ''
with open('./doc/song.txt','w',encoding='utf-8')as f:
    for text in text_list:
        if ('（'  not in text or '（' not in text) and len(text) > 3:
            f.writelines(text)










